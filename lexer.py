import re

TOKENS = [
    ("SET_EXPRESSION", r"set\s\w+\s\[stack\s\d\]"),
    ("PUSH_EXPRESSION", r"push\s$\w+"),
    ("OPEN_BRACE", r"\{"),
    ("CLOSE_BRACE", r"\}"),
    ("OPEN_SQUARE_BRACKET", r"\["),
    ("CLOSE_SQUARE_BRACKET", r"\]"),
    ("WORD", r"\w+"),
]


__TOKENS = []  
__token_classes = {}

def __tokenClass(token_name, token_regex):
    """__tokenClass will return a classObject for a token with specified name and regex pattern.
    If one already exists matching that pattern, it will return the existing class object, otherwise it will create one.
    """
    global __token_classes
    if token_name+token_regex in __token_classes:
        return __token_classes[token_name+token_regex]
    else:
        class Token(object):
            name = token_name
            regex = token_regex

            def __init__(self, msg):
                super(self.__class__, self).__init__()
                if not self.matches(msg):
                    raise ValueError(
                        "Message {msg} does not match {rgx}".format(
                            msg=msg, rgx=self.regex
                        )
                    )
                self.msg = msg

            @classmethod
            def matches(cls, msg):
                return re.match(cls.regex, msg)

            def __repr__(self):
                return "<Token({name}, \"{msg}\")>".format(
                    name=self.name, msg=self.msg
                )

        __token_classes[token_name+token_regex] = Token
        return __token_classes[token_name+token_regex]


def _compile_tokens(token_list):
    """_compile_tokens will compile the token_tuples defined into Token objects."""
    global __TOKENS
    for name, regex in token_list:
        token_class = __tokenClass(name, regex)
        __TOKENS.append(token_class)
    return __TOKENS


def _get_token(buffer):
    """_get_token will return a Token instance of a matching Token class."""
    msg = "".join(buffer)
    for token in __TOKENS:
        if token.matches(msg):
            return token(msg)


def _matches_token(buffer):
    """Returns True if the buffer matches at least one Token"""
    return bool(_get_token(buffer))


def read_char(char_list):
    """Will yield characters from a character_list. 
    Not sure why I did this. It would be useful if it read from a stream.
    """
    while char_list:
        yield char_list.pop(0)



def lex(text):
    """lex will lex the string passed in and return a list of Token objects"""
    _compile_tokens(TOKENS)
    token_buf = []
    tokens = []

    for character in read_char(text.split()):
        token_buf.append(character)

        if _matches_token(token_buf):
            tok = _get_token(token_buf)
            tokens.append(tok)
            token_buf.clear()
    return tokens
