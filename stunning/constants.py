import collections

# For tokens
ONE_OR_MORE = "+"
OR = "|"

# Reserved is a generic keyword type.
# Meant to be a builtin for the TCL syntax.
RESERVED = "RESERVED"

# Ignore is a flag for characters that don't have functional impact on the TCL source.
# We are using it quite liberally to ignore all whitespace and newline characters.
IGNORE = "IGNORE"

# Int is a flag applied on numeric tokens.
INT = "INT"

# Id is a flag applied on word tokens.
ID = "ID"

# Environment key to provide extra grammar files to parse.
#       Separated with os.pathsep.
#       Full paths are expected.
GRAMMAR_PLUGIN_ENV_KEY = "STUNNING_BNF_GRAMMAR_FILES"


# INTERNAL FLAGS
_ANIMATED_VALUE = "__animated__"
_MULTI_VALUE = "__multi__"


lexToken = collections.namedtuple("LexToken", ["name", "value", "tag", "position"])