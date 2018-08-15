import collections

from stunning.exceptions import KeyFrameError
from stunning.token import Token
from stunning.constants import lexToken


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


class KnobValue(object):
    def __init__(self, value):
        super(KnobValue, self).__init__()
        self.value = value


class KeyFrameCollection(collections.Sequence, KnobValue):
    def __init__(self, keyframes):
        self.keyframes = self._build_keyframes(keyframes)
        super(KeyFrameCollection, self).__init__(value=self.keyframes)
        self.mapping = self.keyframes_dict()

    def _build_keyframes(self, keys):
        values = []
        for keyframe_token in keys:
            key_time = Token._get_tok(keyframe_token[0])
            value = Token._get_tok(keyframe_token[1])
            key_frame_object = KeyFrame(key_time, value)
            values.append(key_frame_object)
        return values

    def keyframes_dict(self):
        d = {}
        for keyframe in self.keyframes:
            d[keyframe.frame] = keyframe.value
        return d

    def valueAt(self, frame):
        if frame in self.mapping:
            return self.mapping.get(frame)
        raise KeyFrameError("Could not find a keyframe on frame %d" % frame)

    def __getitem__(self, item):
        return self.keyframes[item]

    def __len__(self):
        return len(self.keyframes)

    def __repr__(self):
        return "Keys: {a}{keys}{b}".format(
            a="{",
            b="}",
            keys=", ".join([repr(key) for key in self.keyframes])
        )


class MultiValue(KnobValue):
    _labels = ["r", "g", "b", "a"]

    def __init__(self, values):
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
        super(MultiValue, self).__init__(value=_values)
        self.values = self.value


class KeyFrame(object):
    def __init__(self, frame_token, value_token):
        super(KeyFrame, self).__init__()
        if frame_token.value[0] == "x":
            value = frame_token.value[1:]
            new_token = lexToken("FLOAT", value, *frame_token[2:])
            self.frame = Token._cast(new_token).value
        self.value = Token._cast(value_token).value

    def __repr__(self):
        return "@{frame}: {value}".format(frame=self.frame, value=self.value)
