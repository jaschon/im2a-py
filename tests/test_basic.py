#!/usr/bin/env python3

import os
import unittest
import tempfile
from im2a import core
from PIL import Image

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


class TestScanImageWhite(unittest.TestCase):
    """Test White Image"""

    start_color = (255, 255, 255)
    size = (100, 100)
    test_color = 255
    test_char = " "

    def test_image(self):
        """Test Solid Image"""
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "test.png")
            image = Image.new('RGB', self.size, self.start_color)
            image.save(path)
            im = core.Im2Scan(path)
            for row in im.color_map:
                for col in row:
                    self.assertEqual(col, self.test_color)
            for row in im.char_map:
                for col in row:
                    self.assertEqual(col, self.test_char)

class TestScanImageBlack(TestScanImageWhite):
    """Test Black Image"""
    start_color = (0, 0, 0)
    test_color = 0
    test_char = "#"

class TestScanImageGray(TestScanImageWhite):
    """Test Gray Image"""
    test_color = 128 
    start_color = (128, 128, 128)
    test_char = "*"

class TestScanImageDkGray(TestScanImageWhite):
    """Test Dark Gray Image"""
    test_color = 50 
    start_color = (50, 50, 50)
    test_char = "$"

class TestScanImageLargeRange(TestScanImageWhite):
    """Test Large Color Range"""
    test_color = 255 
    start_color = (300, 400, 500)
    test_char = " "

class TestScanImageLargeSize(TestScanImageWhite):
    """Test Large Image"""
    test_color = 128 
    start_color = (128, 128, 128)
    size = (500, 1000)
    test_char = "*"


class TestBlockOutput(unittest.TestCase):
    """Test Block Output"""

    size = (100, 100)
    start_color = (0, 0, 0)

    def test_image(self):
        """Test Block Image"""
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "test.png")
            image = Image.new('RGB', self.size, self.start_color)
            image.save(path)
            im = core.Im2Scan(path)
            block = core.Im2Block(im)
            block.save()
            self.assertTrue(os.path.isfile(block.name))


class TestTextOutputBlack(unittest.TestCase):
    """Test Text Output Black"""

    size = (100, 100)
    start_color = (0, 0, 0)
    text_char = "#"

    def test_image(self):
        """Test Text File"""
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "test.png")
            image = Image.new('RGB', self.size, self.start_color)
            image.save(path)
            im = core.Im2Scan(path)
            text = core.Im2Ascii(im)
            text.save()
            self.assertTrue(os.path.isfile(text.name))

            with open(text.name) as fs:
                for row in fs.readlines():
                    self.assertEqual(row.rstrip("\n"), 
                            "".join([self.text_char for char in \
                                    range(int(self.size[0]/im.block_size))]))

class TestTextOutputGray(TestTextOutputBlack):
    """Test Text Output Gray"""

    size = (1000, 100)
    start_color = (128, 128, 128)
    text_char = "*"

class TestTextOutputWhite(TestTextOutputBlack):
    """Test Text Output White"""

    size = (500, 100)
    start_color = (255, 255, 255)
    text_char = " "


if __name__ == "__main__":
    unittest.main()
