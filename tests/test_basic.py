#!/usr/bin/env python3

import unittest
from context import im2a
from im2a import core

class TestImgLoad(unittest.TestCase):
    """Test Image Load"""

    def test_load_none(self):
        im = core.Im2Scan()
        self.assertFalse(im.img)

class TestMap(unittest.TestCase):
    """Test Char Map"""

    def setUp(self):
        """Setup Class"""
        self.im = core.Im2Scan()

    def test_map(self):
        """Test List of Values"""
        for itm in (
                (-255, "#"),
                (-1, "#"),
                (0, "#"),
                (1, "#"),
                (2.3, "#"),
                (50, "$"),
                (128, "*"),
                (150, "!"),
                (200, "'"),
                (254, " "),
                (254.3, " "),
                (255, " "),
                (256, " "),
                (43243214231, " "),
            ):
            self.assertEqual(self.im._map_char(itm[0]), itm[1])

class TestAvg(unittest.TestCase):
    """Test Average"""

    def setUp(self):
        """Setup Class"""
        self.im = core.Im2Scan()

    def test_white(self):
        """Test All White"""
        colors = [255 for col in range(100)]
        self.assertEqual(self.im._color_avg(colors), 255)

    def test_gray(self):
        """Test Between White and Black (128)"""
        white = [255 for col in range(100)]
        black = [0 for col in range(100)]
        self.assertEqual(self.im._color_avg(white+black), 128)

    def test_black(self):
        """Test All Black"""
        colors = [0 for col in range(100)]
        self.assertEqual(self.im._color_avg(colors), 0)

    def test_fail(self):
        """Test Fallback to White"""
        #test blank
        self.assertEqual(self.im._color_avg([]), 255)
        self.assertEqual(self.im._color_avg(()), 255)
        #test wrong type
        self.assertEqual(self.im._color_avg(""), 255)
        self.assertEqual(self.im._color_avg("error"), 255)


if __name__ == "__main__":
    unittest.main()
