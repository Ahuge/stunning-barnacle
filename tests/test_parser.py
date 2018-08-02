import unittest

from stunning import parser

from tests.test_utils import BaseTimingTest


t = """ColorCorrect {
 name ColorCorrect1
 selected true
 xpos -150
 ypos -609
}
set N2f02ecd0 [stack 0]
Blur {
 name Blur1
 size 66.6
 xpos -40
 ypos -614
}
push $N2f02ecd0
Grade {
 white_panelDropped true
 black_clamp false
 name Grade1
 selected true
 xpos -150
 ypos -513
}"""


t1 = """ColorCorrect {
 name ColorCorrect1
 selected true
 xpos -150
 ypos -609
}
set N2f02ecd0 [stack 0]
Blur {
 name Blur1
 size 66.6
 xpos -40
 ypos -614
}
push $N2f02ecd0
Grade {
 white {1 0.808261 0.460907 1}
 white_panelDropped true
 black_clamp false
 name Grade1
 selected true
 xpos -150
 ypos -513
}"""


class ParserTestCase(BaseTimingTest):
    @BaseTimingTest.timing
    def test_simple(self):
        nodes = parser.parse(t)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].Class, "ColorCorrect")
        self.assertEqual(nodes[1].Class, "Blur")
        self.assertEqual(nodes[2].Class, "Grade")

    @BaseTimingTest.timing
    def test_multivalue(self):
        nodes = parser.parse(t1)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].Class, "ColorCorrect")
        self.assertEqual(nodes[1].Class, "Blur")
        self.assertEqual(nodes[2].Class, "Grade")
        self.assertEqual(nodes[2].knobs["white_panelDropped"], True)
        self.assertEqual(nodes[2].knobs["white"].r, 1)
        self.assertEqual(nodes[2].knobs["white"], (1, 0.808261, 0.460907, 1))


if __name__ == "__main__":
    unittest.main()
