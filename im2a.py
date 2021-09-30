#!/usr/bin/env python3

"""
./im2a.py [path] --size (optional)
    --block
    --ascii (default)
    --dots
    --text
"""

import argparse
import os
import sys
from im2a import core

def main(parser):
    """Decide what action to run."""
    args = parser.parse_args()

    try:
        im = core.Im2Scan(args.path, block_size=args.size)
    except (FileNotFoundError, OSError):
        sys.exit("Image Not Found! Check the path and try again.")

    if args.block:
        output = core.Im2Block(im)
    elif args.text:
        output = core.Im2Text(im)
    elif args.dots:
        output = core.Im2Dots(im)
    else:
        output = core.Im2Ascii(im)

    output.run()
    output.save()

def setup_parser():
    """Setup Parser"""
    parser = argparse.ArgumentParser(description="im2a Converter")
    parser.add_argument("path", help="Image Path")
    parser.add_argument("--size", "-s", help="Block Size", type=int, default=10, action="store")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--block", "-b", help="Output as Blocks", action="store_true")
    group.add_argument("--ascii", "-a", help="Output in Ascii Text", action="store_true")
    group.add_argument("--dots", "-d", help="Output in Dots", action="store_true")
    group.add_argument("--text", "-t", help="Output in Text", action="store_true")
    return parser

if __name__ == "__main__":
    main(setup_parser())


