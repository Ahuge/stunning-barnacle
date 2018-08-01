import os
import re
import sys

__all__ = ("TOKEN_NAMES", "lex")

TOKENS_FP = "tokens.tok"
TOKEN_NAMES = {}


def _read_tokens():
    with open(os.path.join(os.path.dirname(__file__), TOKENS_FP), "r") as fh:
        for line in fh.readlines():
            line = line.strip("\n")
            if line:
                yield line.split("\t")[:3]


def __lex(characters):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for name, pattern, tag in _read_tokens():
            TOKEN_NAMES[name] = pattern
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (name, text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens


def lex(characters):
    return __lex(characters)
