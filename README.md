# im2a
__Image to Ascii text converter with various other output options.__

## Requirements

- Argparse
- Pillow

## Script Usage

```
im2a [path] --size (optional)
    --block
    --ascii (default)
    --dots
    --text
```

## Class Usage

1. Make a scan object with Im2Scan.
2. Add scan object to one of the output classes.
    * Im2Block (Image as Blocks of Gray)
    * Im2Dots (Image as Dots of Gray)
    * Im2Text (Image as Text Characters)
    * Im2Ascii (Ascii Text File)
3. Run _save()_.

### Example

```
from im2a import core
scan = core.Im2Scan(img=<path location>, 
               block_size=<size (default 10)>, 
               char_list=[array of characters (optional)])
output = core.Im2Block(scan)
output.save()
```

### Options

1. Image Path <String Path Location>
    * Any image file that can be read with Pillow.
2. Block Size <Int>
    * Size of pixel area that is scanned.
    * Default 10 (10px by 10px).
3. Character List
    * Optional Array or Tuple of characters arranged from dark to light.
    * Default ("#", "$", "*", "!", "'", " ").
    
### Output
* New file will be saved based on name and folder of input image.
* Format: __[folder]/[base]_[type (block|dots|text|ascii)].[png (for images)|txt (for ascii)]__
    


