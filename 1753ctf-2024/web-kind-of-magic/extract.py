#!/usr/bin/env python3
import argparse
from PIL import Image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input PNG')
    args = parser.parse_args()

    img = Image.open(args.input)
    info = img.info

    for k, v in info.items():
        if 'Raw profile type' in k:
            try:
                exfil = v.strip().split('\n')
                chunks = ''.join(exfil[1:])
                print(bytes.fromhex(chunks).decode('utf-8'))
            except:
                pass


if __name__ == '__main__':
    main()

