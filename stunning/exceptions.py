class StunningError(Exception):
    """Stunning base class for exceptions"""


class ParsingError(StunningError, BufferError):
    """General Error while parsing."""


class ResolvingError(ParsingError):
    """General Error while Resolving a set of tokens to a node."""


class LexerError(StunningError, BufferError):
    """General Error while tokenizing."""


class KeyFrameError(StunningError):
    """Error related to keyframe values"""
