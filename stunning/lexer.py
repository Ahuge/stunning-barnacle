import os
import re
import sys

from stunning.exceptions import LexerError

__all__ = ("TOKEN_NAMES", "lex")

TOKENS_FP = "tokens.tok"
TOKEN_NAMES = {}
__tokens = None


def _read_tokens():
    with open(os.path.join(os.path.dirname(__file__), TOKENS_FP), "r") as fh:
        for line in fh.readlines():
            line = line.strip("\n")
            if line:
                yield line.split("\t")[:3]


def _tokens():
    global __tokens
    if not __tokens:
        __tokens = list(_read_tokens())
    return __tokens


def __lex(characters):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        match_name, match_tag = None, None
        for name, pattern, tag in _tokens():
            TOKEN_NAMES[name] = pattern
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                match_name = name
                match_tag = tag
                break
        if not match:
            _msg = "Illegal character: %s at pos: %d" % (characters[pos], pos)
            sys.stderr.write(_msg + "\n")
            raise LexerError(_msg)
        else:
            text = match.group(0)
            token = (match_name, text, match_tag, (pos, match.end(0)))
            tokens.append(token)
            pos = match.end(0)
    return tokens


def lex(characters):
    return __lex(characters)
