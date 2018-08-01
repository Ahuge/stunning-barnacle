import os
import re
import sys


from stunning import lexer
from stunning.objects import NodeObject, KnobObject, SetTCLObject, PushTCLObject

ONE_OR_MORE = "+"
OR = "|"

_PROCESSED = ""


class Token(object):
    _SUB_TYPES = {}
    _TokenClasses = {}

    def __init__(self, name, values):
        super(Token, self).__init__()
        self.name = name
        self.values = values
        self.greedy = False

    @classmethod
    def _get_tok(cls, obj):
        o = obj
        while isinstance(o, list):
            if len(o) == 1:
                o = o[0]
            else:
                break
        return o

    @classmethod
    def factory(cls, name, values):
        if name in cls._SUB_TYPES:
            _t = cls._SUB_TYPES[name]
        else:
            klass = Token
            if name in cls._TokenClasses:
                klass = cls._TokenClasses[name]
            _t = klass(name, values)
            cls._SUB_TYPES[name] = _t
        return _t

    def __repr__(self):
        return "<Token({name}){greed}>".format(name=self.name, greed=" [Greedy]" if self.greedy else "")

    def _resolve(self, tokstream, value):
        if isinstance(value, list):
            return self._resolve_list(tokstream, value)
        elif isinstance(value, Token):
            return self._resolve_token(tokstream, value)
        else:
            return self._resolve_regex(tokstream, value)

    def resolve(self, tokstream):
        backup_tokstream = tokstream[:]

        for each_option in self.values:
            try:
                result = self._resolve(tokstream, each_option)
                if result:
                    self.result = result
                    return result
            except:
                tokstream = backup_tokstream
        raise ValueError("Could not resolve %s token" % self.name)

    def _resolve_list(self, tokstream, list_value):
        values = []
        for value in list_value:
            result = self._resolve(tokstream, value)
            if not result:
                return False
            values.append(result)
        return values

    def _resolve_token(self, tokstream, token_value):
        results = []
        if token_value.greedy:
            while True:
                try:
                    r = token_value.resolve(tokstream)
                    if r:
                        results.append(r)
                    else:
                        break
                except:
                    # import traceback
                    # traceback.print_exc()
                    break
        else:
            results = [token_value.resolve(tokstream)]
        if all(results) and any(results):
            return results
        return False

    def _resolve_regex(self, tokstream, regex_value):
        # '[A-Za-z][A-Za-z0-9_]*'
        # tok from tokstream = (NAME, text, TYPE)
        try:
            tok_name, tok_text, tok_type = tokstream[0]
            if re.match(regex_value, tok_text):
                t = tokstream.pop(0)
                global _PROCESSED
                _PROCESSED += " "
                _PROCESSED += t[1]
                sys.stdout.write(" %s" % t[1])
                return t
        except:
            raise ValueError("Parsing Error!\nExpected %s got %s" % (regex_value, tokstream[0][:-1]))


class OrToken(Token):
    def __init__(self, name):
        super(OrToken, self).__init__(name, [None])

    def resolve(self, tokstream):
        for each_option in self.values:
            try:
                result = self._resolve(tokstream, each_option)
                if result:
                    return result
            except ValueError:
                continue
        raise ValueError("Could not resolve %s token" % self.name)


class OneOrMoreToken(Token):
    def __init__(self, name):
        super(OneOrMoreToken, self).__init__(name, [None])


class NodeToken(Token):
    def resolve(self, tokstream):
        result = super(NodeToken, self).resolve(tokstream)
        name_tok = self.result.pop(0)
        _ = self.result.pop(0)
        knobs_list = self.result.pop(0)
        _ = self.result.pop(0)
        tcl_node = None
        if self.result:
            tcl_code = self._get_tok(self.result.pop(0))
            tcl_klass = None

            if self._get_tok(tcl_code[0])[1] == SetTCLObject.COMMAND:
                tcl_klass = SetTCLObject
            elif self._get_tok(tcl_code[0])[1] == PushTCLObject.COMMAND:
                tcl_klass = PushTCLObject

            args = [self._get_tok(arg)[1] for arg in tcl_code[1:]]
            tcl_node = tcl_klass(
                self._get_tok(tcl_code[0])[1],
                *args
            )
        knobs = self._get_tok(knobs_list)
        return NodeObject(
            self._get_tok(name_tok)[1],
            tcl_node,
            *knobs
        )


class KnobToken(Token):
    def resolve(self, tokstream):
        result = super(KnobToken, self).resolve(tokstream)
        key = self._get_tok(result.pop(0))
        value = self._get_tok(result.pop(0))
        return KnobObject(name=key[1], value=value[1])


Token._TokenClasses["node"] = NodeToken
Token._TokenClasses["knob"] = KnobToken


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
            else:
                created_token = Token.factory(name=part, values=[lexer.TOKEN_NAMES.get(part)])
        created_tokens.append(created_token)
    return _merge_complex_tokens(created_tokens)


def _build_grammar():
    token_names = {}
    with open(os.path.join(os.path.dirname(__file__), "grammar.bnf"), "r") as fh:
        data = fh.readlines()

    _TOK = ": "

    for line in data:
        line = line.strip().rstrip("\n")
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

    resolved_tokens = {}
    for token_name in token_names:
        if token_name not in resolved_tokens:
            resolved_tokens[token_name] = []
        expression_options = token_names[token_name][:]
        for expr_parts in expression_options:
            resolved_parts = _resolve_grammar(token_names, expr_parts)
            resolved_tokens[token_name].append(resolved_parts)

    return resolved_tokens


def parse(text):
    tokens = list(filter(lambda t: t[0] != "WHITESPACE", lexer.lex(text)))

    grammar = _build_grammar()

    main_grammar = grammar["main"][0]
    results = []
    for token in main_grammar:
        result = Token._get_tok(token.resolve(tokens))
        results.append(result)
    tree = None
    print(tree)


# grammar = _build_grammar()
# from pprint import pprint
# pprint(grammar)


t = """ColorCorrect {
 name ColorCorrect1
 selected true
 xpos -150
 ypos -609
}
set N2f02ecd0 [stack 0]
Blur {
 name Blur1
 size 66.6
 xpos -40
 ypos -614
}
push $N2f02ecd0
Grade {
 white_panelDropped true
 black_clamp false
 name Grade1
 selected true
 xpos -150
 ypos -513
}"""
try:
    parse(t)
finally:
    print("")
    print("")
    print(_PROCESSED)
    print("")
    print("")
