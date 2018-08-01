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


class TCLObject(ParseObject):
    def __init__(self, command, *args):
        super(TCLObject, self).__init__()
        self.command = command
        self.args = args


class SetTCLObject(TCLObject):
    def __init__(self, command, *args):
        super(SetTCLObject, self).__init__(command, *args)
        # self.args = <var> [ stack <pos> ]
        self.varname = self.args[0]
        self.stackpost = self.args[-2]


class PushTCLObject(TCLObject):
    def __init__(self, command, *args):
        super(PushTCLObject, self).__init__(command, *args)
        self.varname = self.args[-1]
