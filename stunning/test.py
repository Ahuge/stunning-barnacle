import unittest

import lexer


test_simple_with_merge_text = """set cut_paste_input [stack 0]
version 11.1 v4
push $cut_paste_input
ColorCorrect {
 name ColorCorrect1
 selected true
 xpos -150
 ypos -609
}
set N2f02ecd0 [stack 0]
Blur {
 name Blur1
 selected true
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
}
set N8c39100 [stack 0]
Transform {
 scale 0.6
 center {1079 1136}
 filter Lanczos4
 shutteroffset centred
 name Transform1
 selected true
 xpos -260
 ypos -513
}
push $N8c39100
Merge2 {
 inputs 2
 name Merge1
 selected true
 xpos -150
 ypos -369
}
Merge2 {
 inputs 2
 name Merge2
 selected true
 xpos -40
 ypos -297
}"""



class LexerTestCase(unittest.TestCase):
    def test_simple_with_merge(self):
        tokens = lexer.lex(test_simple_with_merge_text)
        self.assertEqual(len(tokens), 42)  # Don't know how many tokens right now.


if __name__ == "__main__":
    unittest.main()
