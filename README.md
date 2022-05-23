# im2a
__Image to Ascii text converter with various other output options.__

## Requirements

- Argparse
- Pillow
## Install

```
python setup.py install
python setup.py test
```

## Script Usage

```
im2a [option flags] [path] 
    --ascii (default type, output to text file)
    --block (grayscale blocks)
    --dots (scaled grayscale circles)
    --text (grayscale text characters)
    --polygon (grayscale n-sides polygons with rotation. default 8 sides, no rotation)
    --size (optional, default 20)
    --sides (optional for polygon) 
    --rotation (optional for polygon)
```

### Script Examples

```
im2a ~/Desktop/tri.jpg
im2a --ascii ~/Desktop/tri.jpg
# Ascii Text File

im2a --dots ~/Desktop/tri.jpg
# Use Dots

im2a --polygon --size 40 --sides 9 --rotation 45  ~/Desktop/tri.jpg
# Block Size 40px / Use 9-Sided Polygons / Rotated 45deg
```
---

##### Ascii

![im2a example 1](https://github.com/jaschon/im2a-py/blob/main/_screenshots/tri_ascii.png?raw=true)

---

##### Dots

![im2a example 2](https://github.com/jaschon/im2a-py/blob/main/_screenshots/tri_dots.png?raw=true)

---

##### Text

![im2a example 3](https://github.com/jaschon/im2a-py/blob/main/_screenshots/tri_text.png?raw=true)

---

## Class Usage

1. Make a scan object with Im2Scan.
2. Add scan object to one of the output classes.
    * Im2Ascii (Ascii Text File)
    * Im2Block (Image as Blocks of Gray)
    * Im2Dots (Image as Dots of Gray)
    * Im2Text (Image as Text Characters)
    * Im2Polygon (Image as N-Sided Polygon with Rotation)
      * Takes 2 extra options (size and rotation)
3. Run _save()_.

### Class Example

```
import im2a
scan = im2a.Im2Scan(img=<path location>, 
               block_size=<size (default = 10)>, 
               char_list=[array of characters (optional)])
output = im2a.Im2Ascii(scan)
output.save()
```

### Scan Options

1. Image Path <String Path Location>
    * Any image file that can be read with Pillow.
2. Block Size <Int>
    * Size of pixel area that is scanned.
    * Default 10 (10px by 10px).
3. Character List
    * Optional Array or Tuple of characters arranged from dark to light.
    * Default ("#", "$", "*", "!", "'", " ").
    
    
    
    
