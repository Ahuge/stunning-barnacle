import traceback


from stunning import lexer
from stunning import constants
from stunning.exceptions import ParsingError
from stunning.token import Token
from stunning.objects import NodeObject, KnobObject, SetTCLObject, PushTCLObject, MultiValueKnobObject
from stunning.grammar import build_grammar

_PROCESSED = ""


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


def parse(text):
    tokens = list(filter(lambda t: t.tag != constants.IGNORE, lexer.lex(text)))

    grammar = build_grammar()

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

