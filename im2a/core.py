#!/usr/bin/env python3

"""Total Rewrite of im2a"""

from PIL import Image, ImageDraw, ImageFont
from os import path

__author__ = "Jason Rebuck"
__copyright__ = "2011-2021"
__version__ = "v.3"

class Im2Scan:
    """Scan Image Pixels and Build Color and Character Maps"""

    img = None #pil image instance

    block_size = 10 #pixel block size
    char_list = ("#", "$", "*", "!", "'", " ") #list used when mapping [light -> dark]

    char_map = [] #final character map
    color_map = [] #final color map

    def __init__(self, img=None, block_size=None, char_list=None):
        self._setup(img, block_size, char_list)
        self._run()

    def _setup(self, img, block_size, char_list):
        self.block_size = block_size or self.block_size
        self.char_list = char_list or self.char_list
        self._load_img(img)

    def _load_img(self, img):
        try:
            if img:
                self.img = Image.open(img).convert("L") #open image and convert to b&w
        except (IOError, AttributeError) as error:
            print(error)
            raise

    def _color_avg(self, pixels):
        """Get Average Color in Pixel Block"""
        try:
            return round(float(sum(pixels))/len(pixels)) #return average color value
        except (TypeError, ZeroDivisionError):
            return 255 #if out of range or no pixel values, return white

    def _map_char(self, num):
        """Map Color Value to List Value""" 
        for c in range(1, len(self.char_list)+1):
            if num <= round(c*(255.0/len(self.char_list))):
                return str(self.char_list[c-1]) #return char (make sure it is a string!)
        return self.char_list[-1] #if nothing found, give the first value

    def _run(self):
        """Translate Pixel Values to Characters and Color Maps"""
        if not self.img: return
        self.char_map = [] #clear char map
        self.color_map = [] #clear color map
        y_break = False
        try:
            img_x, img_y = self.img.size #get image size
            for y_pos in range(0, img_y+self.block_size, self.block_size): #loop through height
                y_max = y_pos + self.block_size
                x_break = False
                self.char_map.append([]) #new row in output
                self.color_map.append([]) #new row in output
                if y_max >= img_y: #if value is more than height, give height and flag for loop break
                    y_max = img_y
                    y_break = True
                for x_pos in range(0, img_x, self.block_size): #loop through width
                    x_max = x_pos + self.block_size
                    if x_max >= img_x: #if value is more than width, give width and flag for loop break
                        x_max = img_x
                        x_break = True
                    # remember: cropbox is (left, upper, right, bottom)
                    region = self.img.crop((x_pos, y_pos, x_max, y_max)) #crop region box
                    # get average color in block, map char and add char to char_map
                    color_avg = self._color_avg(list(region.getdata()))
                    self.char_map[-1].append(self._map_char(color_avg))
                    self.color_map[-1].append(color_avg)
                    if x_break: #break when you reach the max width
                        break
                if y_break: #break when you reach the max height
                    break
        except IndexError as error:
            print(error)


if __name__ == "__main__":
    pass

