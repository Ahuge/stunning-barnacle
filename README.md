# stunning-barnacle
Nukescript TCL parser and lexer

![Stunning Barnacle Icon](.github/icon.jpg)


## Features
  - Parses **most** nodes
    - Read knob values
    - Read Class types
  - Plug-In based BNF parser.
    - Allows you to set `STUNNING_BNF_GRAMMAR_FILES` environment variable to provide additional bnf parser files.
      - See [stunning.constants.py](https://github.com/Ahuge/stunning-barnacle/blob/master/stunning/constants.py#L22) for usage.

## Unsupported Features
- Cannot correctly parse Roto nodes yet... See [roto.bnf](https://github.com/Ahuge/stunning-barnacle/blob/master/stunning/roto.bnf) for a WIP parser.
- I have stubbed in code for reading animated keyframe values. I thought I had included that in the source but apparently not.
- Nicer high level node/knob api similar to the first party API
