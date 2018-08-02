import collections


class ParseObject(object):
    pass


class NodeObject(ParseObject):
    def __init__(self, node_class, tcl_node=None, *knobs):
        super(NodeObject, self).__init__()
        self.Class = node_class
        self._knobs = knobs
        self.tcl_node = tcl_node

    @property
    def knobs(self):
        return dict([(k.name, k.value) for k in self._knobs])


class KnobObject(ParseObject):
    def __init__(self, name, value):
        super(KnobObject, self).__init__()
        self.name = name
        self.value = value


class MultiValueKnobObject(KnobObject):
    _labels = ["r", "g", "b", "a"]

    def __init__(self, name, values):
        labels = self._labels[:]
        count = 1
        while len(labels) < len(values):
            # Make labels longer than values:
            #   ["r", "g", "b", "a", "r1", "g1", "b1", "a1"]
            #   [ 1,   2,   3,   4,   5]
            labels.extend(
                ["%s%d" % (label, count) for label in self._labels]
            )
            count += 1

        value_names = collections.namedtuple("MultiValueKnob", labels)
        while len(values) < len(labels):
            # Pad out our values with None to make them the same length as labels:
            #   ["r", "g", "b", "a", "r1", "g1", "b1", "a1"]
            #   [ 1,   2,   3,   4,   5,   None, None, None]
            values.append(None)

        _values = value_names(*values)
        super(MultiValueKnobObject, self).__init__(name=name, value=_values)
        self.values = self.value


class TCLObject(ParseObject):
    COMMAND = None

    def __init__(self, command, *args):
        super(TCLObject, self).__init__()
        self.command = command
        self.args = args


class SetTCLObject(TCLObject):
    COMMAND = "set"

    def __init__(self, command, *args):
        super(SetTCLObject, self).__init__(command, *args)
        # self.args = <var> [ stack <pos> ]
        self.varname = self.args[0]
        self.stackpost = self.args[-2]


class PushTCLObject(TCLObject):
    COMMAND = "push"

    def __init__(self, command, *args):
        super(PushTCLObject, self).__init__(command, *args)
        self.varname = self.args[-1]
