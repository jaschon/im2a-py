# im2a
__Image to Ascii text converter with various other output options....__

## Requirements

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

1. Scan Image with Im2Scan Class
2. Add scan to Output Class
    * Im2Block (Image as Blocks of Gray)
    * Im2Dots (Image as Dots of Gray)
    * Im2Text (Image as Text Characters)
    * Im2Ascii (Ascii Text File)
3. Run _save()_ Method

### Example

```
scan = Im2Scan(img=[path location], 
               block_size=[size of blocks (default 10)], 
               char_list=[ascii char map used for output (optional)])
output = Im2Block(scan)
output.save()
```


