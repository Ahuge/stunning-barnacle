from parser_lib import _lexer


RESERVED = 'RESERVED'
IGNORE   = 'IGNORE'
INT      = 'INT'
ID       = 'ID'

expr = [
    (r'\{',                    "OPEN_BRACE", RESERVED),
    (r'\}',                    "CLOSE_BRACE", RESERVED),
    (r'\(',                    "OPEN_PARENS", RESERVED),
    (r'\)',                    "CLOSE_PARENS", RESERVED),
    (r'\[',                    "OPEN_BRACKET", RESERVED),
    (r'\]',                    "CLOSE_BRACKET", RESERVED),
    (r"\\n",                   "NEWLINE", RESERVED),
    (r"\s",                    "WHITESPACE", IGNORE),

    (r"\$",                    "TCL_VAR", RESERVED),
    (r'set',                   "TCL_SET", RESERVED),
    (r'push',                  "TCL_PUSH", RESERVED),

    (r'[-+]?[0-9]+\.[0-9]+',   "FLOAT", INT),
    (r'[-+]?[0-9]+',           "INT", INT),
    (r'[A-Za-z][A-Za-z0-9_]*', "WORD", ID),
]

TOKEN_NAMES = {}
for exp in expr:
    pattern, name, type_ = exp
    TOKEN_NAMES[name] = pattern


def imp_lex(characters):
    return _lexer.lex(characters, expr)
