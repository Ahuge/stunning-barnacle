import os

from stunning.lexer import TOKEN_NAMES
from stunning.token import Token, OrToken, OneOrMoreToken, LiteralToken
from stunning.constants import ONE_OR_MORE, OR, GRAMMAR_PLUGIN_ENV_KEY


def _merge_complex_tokens(tokens):
    output_tokens = []
    tokens_copy = tokens[:]
    join = False
    for index, token in enumerate(tokens_copy):
        if join:
            token_or = output_tokens.pop()
            p1 = output_tokens.pop()
            token_or.values = [p1, token]
            output_tokens.append(token_or)
        elif token.name == OR:
            join = True
            output_tokens.append(token)
            continue
        elif token.name == ONE_OR_MORE:
            token_to_more = output_tokens[-1]
            token_to_more.greedy = True
        else:
            output_tokens.append(token)
        join = False
    return output_tokens


def _resolve_grammar(token_names, parts):
    created_tokens = []
    for part in parts:
        if part in token_names:
            values = []
            options = token_names[part][:]
            for option in options:
                values.append(_resolve_grammar(token_names, option))
            created_token = Token.factory(name=part, values=values)
            # while values:
            #     created_token.values.append(values.pop(0))
        else:
            if part == OR:
                created_token = OrToken(name=part)
            elif part == ONE_OR_MORE:
                created_token = OneOrMoreToken(name=part)
            elif part[0] in ["\"", "\'"] and part[-1] in ["\"", "\'"]:
                created_token = LiteralToken(value=part)
            else:
                created_token = Token.factory(name=part, values=[TOKEN_NAMES.get(part)])
        created_tokens.append(created_token)
    return _merge_complex_tokens(created_tokens)


def _load_grammar():
    paths = [os.path.join(os.path.dirname(__file__), "grammar.bnf")]
    plugin_paths = os.environ.get(GRAMMAR_PLUGIN_ENV_KEY, "").split(os.pathsep)
    paths += filter(bool, plugin_paths)

    grammar = {}
    for path in paths:
        with open(path, "r") as fh:
            data = fh.readlines()
        _grammar = _build_grammar(data)
        if _grammar:
            grammar.update(_grammar)
    return grammar


def _build_grammar(grammar_lines):
    token_names = {}
    _TOK = "::= "

    for line in grammar_lines:
        line = line.strip().rstrip("\n").split("//")[0]
        if not line:
            continue
        name = line.split(_TOK)[0]
        if name not in token_names:
            token_names[name] = []
        expr = line.replace(name + _TOK, "", 1).strip()
        _expr_parts = expr.split()
        expr_parts = []
        for _exprpart in _expr_parts:
            if ONE_OR_MORE not in _exprpart and OR not in _exprpart:
                expr_parts.append(_exprpart)
                continue

            if ONE_OR_MORE in _exprpart:
                parts = _exprpart.split(ONE_OR_MORE)
                for part in parts:
                    if part:
                        expr_parts.append(part)
                        expr_parts.append(ONE_OR_MORE)

            if OR in _exprpart:
                parts = _exprpart.split(OR)
                for part in parts:
                    if part:
                        expr_parts.append(part)
                        expr_parts.append(OR)
                expr_parts.pop()

        token_names[name].append(expr_parts)
    return token_names


def build_grammar():
    token_names = _load_grammar()

    resolved_tokens = {}
    for token_name in token_names:
        if token_name not in resolved_tokens:
            resolved_tokens[token_name] = []
        expression_options = token_names[token_name][:]
        for expr_parts in expression_options:
            resolved_parts = _resolve_grammar(token_names, expr_parts)
            resolved_tokens[token_name].append(resolved_parts)

    return resolved_tokens
