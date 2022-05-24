# im2a
__Convert images to a grid of Ascii characters, dots, blocks or n-sided polygons.__

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
im2a [option flags] [one or more paths] 
    --ascii (default type, outputs to text file instead of making a PNG)
    --block (grayscale blocks)
    --dots (scaled grayscale circles)
    --text (grayscale text characters)
    --polygon (grayscale n-sides polygons with rotation. default 8 sides, no rotation)
    --size (optional pixel block size, default 10)
    --sides (optional for polygon) 
    --rotation (optional for polygon)
```

### Script Examples

##### 1. Ascii (Text File)
```
im2a ~/Desktop/tri.jpg
# NOTE: --ascii is default
```

![im2a example 1](https://github.com/jaschon/im2a-py/blob/main/_screenshots/tri_ascii.png?raw=true)

---

##### 2. Text (PNG Image)

```
im2a --text ~/Desktop/tri.jpg
```

![im2a example 2](https://github.com/jaschon/im2a-py/blob/main/_screenshots/tri_text.png?raw=true)


---

##### 3. Dots (PNG Image)

```
im2a --dots ~/Desktop/tri.jpg
```

![im2a example 3](https://github.com/jaschon/im2a-py/blob/main/_screenshots/tri_dots.png?raw=true)

---

##### 4. Polygon (PNG Image)

```
im2a --polygon --size 40 --sides 9 --rotation 45  ~/Desktop/tri.jpg
# Options: pixel block size 40px / 9-sided polygons / rotated 45deg
```

![im2a example 4](https://github.com/jaschon/im2a-py/blob/main/_screenshots/tri_polygon.png?raw=true)

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
    
    
    
    
