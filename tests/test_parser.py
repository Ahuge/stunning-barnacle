import unittest

from stunning import parser
from stunning.exceptions import KeyFrameError

from tests.test_utils import BaseTimingTest, timing


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


t2 = """Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
"""

t3 = """Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
Grade {
 white {{curve x1001 1 x1006 2}}
 black_clamp false
 name Grade4
 selected true
 xpos 6102
 ypos 2065
}
ColorCorrect {
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
}
ColorCorrect {
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
}
ColorCorrect {
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
}
"""


t4 = """ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
}ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
ColorCorrect {
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
"""


class ParserTestCase(BaseTimingTest):
    @timing
    def test_simple(self):
        nodes = parser.parse(t)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].Class, "ColorCorrect")
        self.assertEqual(nodes[1].Class, "Blur")
        self.assertEqual(nodes[2].Class, "Grade")

    @timing
    def test_multivalue(self):
        nodes = parser.parse(t1)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].Class, "ColorCorrect")
        self.assertEqual(nodes[1].Class, "Blur")
        self.assertEqual(nodes[2].Class, "Grade")
        self.assertEqual(nodes[2].knobs["white_panelDropped"], True)
        self.assertEqual(nodes[2].knobs["white"].value.r, 1)
        self.assertEqual(nodes[2].knobs["white"].value, (1, 0.808261, 0.460907, 1))

    @timing
    def test_animated_value(self):
        nodes = parser.parse(t2)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].Class, "Grade")
        self.assertEqual(nodes[0].knobs["white"].valueAt(1001), 1)
        self.assertEqual(nodes[0].knobs["white"].valueAt(1006), 2)
        with self.assertRaises(KeyFrameError):
            nodes[0].knobs["white"].valueAt(1003)

    @timing
    def test_large_script_parse(self):
        nodes = parser.parse(t3)
        self.assertEqual(len(nodes), 250)

    @timing
    def test_large_simple_script_parse(self):
        import cProfile
        p = cProfile.Profile()
        p.enable()
        nodes = parser.parse(t4)
        p.disable()
        p.dump_stats("/var/tmp/test_large_simple_script_parse")
        self.assertEqual(len(nodes), 250)


if __name__ == "__main__":
    unittest.main()
