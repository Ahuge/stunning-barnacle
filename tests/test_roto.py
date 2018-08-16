import os
import unittest

from stunning.constants import GRAMMAR_PLUGIN_ENV_KEY
from stunning import parser

from tests.test_utils import BaseTimingTest, timing



t = """Roto {
 output alpha
 cliptype none
 curves {{{v x3f99999a}
  {f 0}
  {n
   {layer Root
    {f 0}
    {t x4497c000 x44438000}
    {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}}}}}
 toolbox {createBezier {
  { createBezier str 1 ssx 1 ssy 1 sf 1 sb 1 tt 4 }
  { createBezierCusped str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { createBSpline str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { createEllipse str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { createRectangle str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { createRectangleCusped str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { brush str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { eraser src 2 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { clone src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { reveal src 3 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { dodge src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { burn src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { blur src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { sharpen src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { smear src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
} }
 toolbar_brush_hardness 0.200000003
 toolbar_source_transform_scale {1 1}
 toolbar_source_transform_center {1214 782}
 name Roto2
 selected true
 xpos 6111
 ypos 1956
}
"""

t2 = """Roto {
 output alpha
 cliptype none
 curves {{{v x3f99999a}
  {f 0}
  {n
   {layer Root
    {f 2097152}
    {t x4497c000 x44438000}
    {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
    {curvegroup Bezier1 512 bezier
     {{cc
       {f 8192}
       {px x4482a000
        {0 0}
        {x44614000 x44768000}
        {0 0}
        {0 0}
        {x44590000 x43c00000}
        {0 0}
        {0 0}
        {x44b72000 x43aa0000}
        {0 0}
        {0 xc0000000}
        {x449e8000 x4435c000}
        {0 x40000000}
        {0 0}
        {x44a3a000 x44872000}
        {0 0}
        {x40c00000 x41300000}
        {x44634000 x44924000}
        {xc0c00000 xc1300000}
        {0 0}
        {x4448c000 x447c4000}
        {0 0}}}     idem}
     {tx x4482a000 x448656db x444b76db}
     {a osw x41200000 osf 0 str 1 spx x4497c000 spy x44438000 sb 1 ltn x4482a000 ltm x4482a000 tt x40800000}}}}}}
 toolbox {selectAll {
  { selectAll str 1 ssx 1 ssy 1 sf 1 }
  { createBezier str 1 ssx 1 ssy 1 sf 1 sb 1 tt 4 }
  { createBezierCusped str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { createBSpline str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { createEllipse str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { createRectangle str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { createRectangleCusped str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { brush str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { eraser src 2 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { clone src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { reveal src 3 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { dodge src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { burn src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { blur src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { sharpen src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
  { smear src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
} }
 toolbar_brush_hardness 0.200000003
 toolbar_source_transform_scale {1 1}
 toolbar_source_transform_center {1214 782}
 colorOverlay {0 0 0 0}
 lifetime_type "all frames"
 lifetime_start 1045
 lifetime_end 1045
 motionblur_shutter_offset_type centred
 source_black_outside true
 name Roto2
 selected true
 xpos 6111
 ypos 1956
}
"""


class RotoTestCase(BaseTimingTest):
    def setUp(self):
        super(RotoTestCase, self).setUp()

        roto_grammar = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "stunning",
            "roto.bnf"
        )
        os.environ[GRAMMAR_PLUGIN_ENV_KEY] = roto_grammar

    @timing
    def test_simple(self):
        nodes = parser.parse(t)
        self.assertEqual(len(nodes), 1)

    @timing
    def test_one_shape(self):
        ss = t2[445:500]
        nodes = parser.parse(t2)
        self.assertEqual(len(nodes), 1)


if __name__ == "__main__":
    unittest.main()
