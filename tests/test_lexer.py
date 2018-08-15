import unittest

from stunning import lexer

from tests.test_utils import BaseTimingTest, timing


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


class LexerTestCase(BaseTimingTest):
    @timing
    def test_simple_with_merge(self):
        tokens = lexer.lex(test_simple_with_merge_text)
        self.assertEqual(len(tokens), 263)

    @timing
    def test_large_text_parse(self):
        tokens = lexer.lex(t3)
        self.assertEqual(len(tokens), 9900)


if __name__ == "__main__":
    unittest.main()
