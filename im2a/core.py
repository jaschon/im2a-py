#!/usr/bin/env python3

"""Image to Ascii text converter with various other output options."""

from PIL import Image, ImageDraw, ImageFont
from os import path

__author__ = "Jason Rebuck"
__copyright__ = "2011-2021"
__version__ = "0.38"

class Im2Scan:
    """Scan Image Pixels and Build Color and Character Maps"""

    img = None #pil image instance
    name = None

    block_size = 10 #pixel block size
    char_list = ("#", "$", "*", "!", "'", " ") #mapping [dark -> light]

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
        """Load Image and make PIL Obj"""
        try:
            if img:
                self.name = img
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


class Im2Block:
    """Output to Blocks"""

    file_name = "blocks"
    ext = "png"

    def __init__(self, obj):
        """Set Size and Obj"""
        self.obj = obj
        self._setup()
        self._run()

    def _setup(self):
        """Setup Variables"""
        self._set_size() #set height and width
        self._set_img() #setup output file and other objects
        self._set_name() #setup output filename

    def _set_img(self):
        """Make new Draw Obj and PIL Output Image"""
        self.img = Image.new("L", (self.width, self.height), 255) #make output image
        self.draw = ImageDraw.Draw(self.img) #make draw object

    def _set_size(self):
        """Get Size of Output Image Based on Map"""
        self.height= len(self.obj.color_map) * self.obj.block_size #cal height
        self.width = len(self.obj.color_map[0]) * self.obj.block_size #cal width

    def _set_name(self, name=None):
        """Make Output Filename"""
        self.name = f"{path.splitext(name or self.obj.name)[0]}_" \
                f"{self.file_name}.{self.ext}" 

    def _run(self):
        """Use Map to Draw Blocks on Output Image"""
        row = 0 #var to change row in outputColor array
        for ypos in range(0, self.height, self.obj.block_size): #loop through height
            xpos = 0 #x val
            for col in range(0, len(self.obj.color_map[row])): #loop through width
                self._write(xpos, ypos, row, col) #send loop var to write function
                xpos += self.obj.block_size #inc x val
            row += 1 #inc row

    def _write(self, xpos, ypos, row, col):
        """Draw Blocks on Output Image"""
        try:
            self.draw.rectangle((xpos, ypos, xpos + self.obj.block_size, \
                    ypos + self.obj.block_size), self.obj.color_map[row][col]) #draw rectangle
        except IOError:
            print(f"Unable To Write Block Image Line! ({xpos},{ypos})")
            raise

    def save(self):
        """Save Image"""
        self.img.save(self.name) #save to file


class Im2Dots(Im2Block):
    """Output to Circles"""

    file_name = "dots"

    def _write(self, xpos, ypos, row, col):
        """Draw Blocks on Output Image"""
        try:
            adjust = round(self.obj.block_size / 2)
            xpos += adjust
            ypos += adjust
            amount = adjust - ((self.obj.color_map[row][col]/255.0) * adjust)
            self.draw.ellipse((xpos - amount, ypos - amount, xpos + amount, ypos + amount), \
                    self.obj.color_map[row][col]) 
        except IOError:
            print(f"Unable To Write Ellipse! ({xpos},{ypos} : {amount})")
            raise


class Im2Text(Im2Block):
    """Output to Text Characters"""

    file_name = "text"

    def __init__(self, obj):
        """Set Size and Obj"""
        self.obj = obj
        self._set_font()
        self._setup()
        self._run()

    def _set_font(self):
        self.obj.block_size = 11
        self.font = ImageFont.load_default()

    def _write(self, xpos, ypos, row, col):
        try:
            self.draw.text((xpos+3, ypos), self.obj.char_map[row][col], \
                    font=self.font, fill=self.obj.color_map[row][col])
        except IndexError:
            print(f"Unable To Write Image Text Line! ({xpos},{ypos})")
            raise


class Im2Ascii(Im2Block):
    """Output to Ascii Text"""

    file_name = "ascii"
    ext = "txt"

    def __init__(self, obj):
        """Set Size and Obj"""
        self.obj = obj
        self._set_name()

    def _run(self):
        """Skip Run. Everything is done in save."""
        pass

    def save(self):
        """Output to Textfile"""
        try:
            with open(self.name, 'w') as fs:
                for ch in self.obj.char_map:
                    fs.write(''.join(ch))
                    fs.write('\n')
        except OSError:
            print("Unable to Write File!")
            raise


class Im2Polygon(Im2Block):
    """Output to N-Sided Polygon"""

    file_name = "polygon"

    def __init__(self, obj, sides=8, rotation=0):
        """Set Size and Obj"""
        self.obj = obj
        self._setup()
        self.sides = sides if sides > 2 else 3
        self.rotation = rotation
        self._run()

    def _write(self, xpos, ypos, row, col):
        """Draw Blocks on Output Image"""
        try:
            adjust = round(self.obj.block_size / 2)
            xpos += adjust
            ypos += adjust
            self.draw.regular_polygon((xpos, ypos, adjust), self.sides, \
                    fill=self.obj.color_map[row][col], rotation=self.rotation) 
        except IOError:
            print(f"Unable To Write! ({xpos},{ypos})")
            raise


if __name__ == "__main__":
    pass

