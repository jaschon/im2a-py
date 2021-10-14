# im2a
__Image to Ascii text converter with various other output options....__

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
scan = Im2Scan(img=[path location], 
               block_size=[size of blocks (default 10)], 
               char_list=[ascii char map used for output (optional)])
output = Im2Block(scan)
output.save()
```


