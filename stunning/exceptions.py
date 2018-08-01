class ParsingError(BufferError):
    """General Error while parsing."""


class ResolvingError(ParsingError):
    """General Error while Resolving a set of tokens to a node."""


class LexerError(BufferError):
    """General Error while tokenizing."""
