import contextlib
import os
import re
import sys
import traceback


from stunning import lexer
from stunning import _types
from stunning.exceptions import ParsingError, ResolvingError
from stunning.objects import NodeObject, KnobObject, SetTCLObject, PushTCLObject, MultiValueKnobObject

ONE_OR_MORE = "+"
OR = "|"

_PROCESSED = ""


class Token(object):
    _SUB_TYPES = {}
    _TokenClasses = {}
    TBOOLS = ["true", "True"]
    BOOLS = ["false", "False"] + TBOOLS
    exc_stack = []

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
        return _t

    def _cast(self, lex_token):
        if lex_token.name == "FLOAT":
            value = float(lex_token.value)
        elif lex_token.name == "INT":
            value = int(lex_token.value)
        elif lex_token.name == "WORD" and lex_token.value in self.BOOLS:
            if lex_token.value in self.TBOOLS:
                value = True
            else:
                value = False
        else:
            return lex_token
        return lex_token.__class__(
            lex_token.name,
            value,
            lex_token.tag,
            lex_token.position
        )

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
        for each_option in self.values:
            Token.exc_stack.clear()

            with self.rewindable(tokstream) as rewound:
                result = self._resolve(tokstream, each_option)
                if result:
                    self.result = result
                    return result
            if rewound:
                continue
        raise ResolvingError(
            "Could not resolve %s token.\nToken stream contained: %s"
            % (self.name, tokstream)
        )

    def _resolve_list(self, tokstream, list_value):
        values = []
        for value in list_value:
            result = self._resolve(tokstream, value)
            if not result:
                return False
            values.append(result)
        return values

    @contextlib.contextmanager
    def rewindable(self, stream):
        """
        rewindable is a helpful contextmanager that will attempt to execute it's body and
            on exception will rewind the tokenstream back to it's previous state.
        It does this by reverse inserting back into the container.
        This preserves references to mutable structures but sill allows us to undo
            tokstream consuming actions.

        rewindable will also insert exceptions into the exc_stack on the Token class obj.
        This can be used at the end of parsing to see the chain of events that caused an
            incorrect parsing.

        :param stream: Mutable iterable container of tokens.
        :type stream: types.Iterable
        :yields: A mutable sentinel value that you can test the "truthy-ness" of to detect
            if the previous operation failed. If the sentinel is "truthy", it will contain
            one or more exception tuples in it that you are able to do what you want with.
        :ytype: types.Iterable
        """
        backup = stream[:]
        exception_store = []
        try:
            yield exception_store
        except Exception as err:
            index = len(stream) + 1
            while index <= len(backup):
                stream.insert(0, backup[-index])
                index += 1

            exc_type, exc_obj, exc_tb = sys.exc_info()
            Token.exc_stack.insert(0, (exc_type, exc_obj, exc_tb))
            exception_store.append(err)

    def _resolve_token(self, tokstream, token_value):
        results = []
        if token_value.greedy:
            while True:
                with self.rewindable(tokstream) as rewound:
                    r = token_value.resolve(tokstream)
                    if r:
                        results.append(r)
                    else:
                        break
                if rewound:  # An exception was thrown and we should stop.
                    break
        else:
            results = [token_value.resolve(tokstream)]
        if all(results) and any(results):
            return results
        return False

    def _resolve_regex(self, tokstream, regex_value):
        with self.rewindable(tokstream) as rewound:
            tok_name, tok_text, tok_type, tok_pos = tokstream[0]
            if re.match(regex_value, tok_text):
                t = tokstream.pop(0)
                global _PROCESSED
                _PROCESSED += " "
                _PROCESSED += t[1]
                sys.stdout.write(" %s" % t.value)
                return t
        if rewound:
            raise ParsingError("Parsing Error!\nExpected %s got %s" % (regex_value, tokstream[0][:-1]))


class LiteralToken(Token):
    def __init__(self, value):
        super(LiteralToken, self).__init__(name="LiteralToken", values=[value])


class OrToken(Token):
    def __init__(self, name):
        super(OrToken, self).__init__(name, [None])


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

            if self._get_tok(tcl_code[0]).value == SetTCLObject.COMMAND:
                tcl_klass = SetTCLObject
            elif self._get_tok(tcl_code[0]).value == PushTCLObject.COMMAND:
                tcl_klass = PushTCLObject

            args = [self._get_tok(arg).value for arg in tcl_code[1:]]
            tcl_node = tcl_klass(
                self._get_tok(tcl_code[0]).value,
                *args
            )
        knobs = self._get_tok(knobs_list)
        return NodeObject(
            self._get_tok(name_tok).value,
            tcl_node,
            *knobs
        )


class KnobToken(Token):
    def resolve(self, tokstream):
        result = super(KnobToken, self).resolve(tokstream)
        key = self._get_tok(result.pop(0))
        value = self._get_tok(result.pop(0))
        if isinstance(value, list):
            values = []
            for v in value[1]:
                tok = self._get_tok(v)
                tok = self._cast(tok)
                values.append(tok.value)
            return MultiValueKnobObject(name=key.value, values=values)

        value = self._cast(value)
        return KnobObject(name=key.value, value=value.value)


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
            elif part[0] in ["\"", "\'"] and part[-1] in ["\"", "\'"]:
                created_token = LiteralToken(value=part)
            else:
                created_token = Token.factory(name=part, values=[lexer.TOKEN_NAMES.get(part)])
        created_tokens.append(created_token)
    return _merge_complex_tokens(created_tokens)


def _build_grammar():
    token_names = {}
    with open(os.path.join(os.path.dirname(__file__), "grammar.bnf"), "r") as fh:
        data = fh.readlines()

    _TOK = "::= "

    for line in data:
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
    tokens = list(filter(lambda t: t.tag != _types.IGNORE, lexer.lex(text)))

    grammar = _build_grammar()

    main_grammar = grammar["main"][0]
    results = []
    for token in main_grammar:
        result = Token._get_tok(token.resolve(tokens))
        results.append(result)
    if len(tokens):
        for exc_t, exc_o, exc_tb in Token.exc_stack:
            traceback.print_exception(exc_t, exc_o, exc_tb)
        raise ParsingError(
            "The stunning library was unable to consume the entire text passed to it.\n"
            "This is probably due to a syntax error in the text.\n"
            "Resulting token stream contained %s..." % tokens[:3]
        )
    return Token._get_tok(results)


if __name__ == "__main__":
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
        print("Processed the following text: %s" %_PROCESSED)
        print("")
        print("")

