import contextlib
import re
import sys

from stunning.exceptions import ParsingError, ResolvingError

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

    def to_re(self):
        result_list = []
        for value in self.values:
            if isinstance(value, str):
                result_list.append(r"(?:" + value + r")")
            else:
                for part in value:
                    if isinstance(part, Token):
                        _r = part.to_re()
                        result_list.append(_r)
                    else:
                        result_list.append(part)
        return r"(?:" + (r"|".join(result_list)) + r")"

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

    @classmethod
    def _cast(cls, lex_token):
        if lex_token.name == "FLOAT":
            value = float(lex_token.value)
        elif lex_token.name == "INT":
            value = int(lex_token.value)
        elif lex_token.name == "WORD" and lex_token.value in cls.BOOLS:
            if lex_token.value in cls.TBOOLS:
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
            # Token.exc_stack.clear()   $$ Not in py2.7 :(

            with self.rewindable(tokstream) as rewound:
                result = self._resolve(tokstream, each_option)
                if result:
                    self.result = result
                    # while Token.exc_stack:
                    #     Token.exc_stack.pop()
                    return result
            if rewound:
                continue
        raise ResolvingError(
            "Could not resolve %s token.\nToken stream contained: %s"
            % (self.name, tokstream[:3])
        )

    def _resolve_list(self, tokstream, list_value):
        values = []
        for value in list_value:
            if hasattr(value, "name") and value.name == "toolbox_value":
                print("Stop Here!")
            result = self._resolve(tokstream, value)
            if not result:
                raise ResolvingError(
                    "Could not resolve %s token.\nToken stream contained: %s"
                    % (self.name, tokstream[:3])
                )
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
            import traceback
            traceback.print_exc()

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
                #global _PROCESSED
                #_PROCESSED += " "
                #_PROCESSED += t[1]
                #sys.stdout.write(" %s" % t.value)
                return t
        if rewound:
            raise ParsingError("Parsing Error!\nExpected %s got %s" % (regex_value, tokstream[0][:-1]))


def _merge_tokens(first, second):
    f_re = first.to_re()
    s_re = second.to_re()
    return RegexToken(values=[f_re + s_re])


class RegexToken(Token):
    def __init__(self, values):
        super(RegexToken, self).__init__("RegexToken", values)

    def to_re(self):
        return self.values[0]


class LiteralToken(Token):
    def __init__(self, value):
        super(LiteralToken, self).__init__(name="LiteralToken", values=[value[1:-1]])


class OrToken(Token):
    def __init__(self, name):
        super(OrToken, self).__init__(name, [None])


class OneOrMoreToken(Token):
    def __init__(self, name):
        super(OneOrMoreToken, self).__init__(name, [None])


class OpenGroupToken(Token):
    def __init__(self, name):
        super(OpenGroupToken, self).__init__(name, [None])


class CloseGroupToken(Token):
    def __init__(self, name):
        super(CloseGroupToken, self).__init__(name, [None])


class GroupToken(Token):
    def __init__(self, values):
        token = values.pop(0)
        for second_token in values:
            token = _merge_tokens(token, second_token)
        super(GroupToken, self).__init__(name="GroupToken", values=[token])
