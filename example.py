from stunning import parser
from stunning.exceptions import KeyFrameError

with open("example.nk", "r") as fh:
  nukescript_data = fh.read()

nodes = parser.parse(nukescript_data)

print("The first node's type is: {}".format(nodes[0].Class))
print("The value of the 'white' knob at frame 1001 is: {}".format(nodes[0].knobs["white"].valueAt(1001)))
print("The value of the 'white' knob at frame 1006 is: {}".format(nodes[0].knobs["white"].valueAt(1006)))
