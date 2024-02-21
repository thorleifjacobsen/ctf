"""
    DeEncryptinator 9000
    Crypto: easy, medium
    Toffe / UiTHack 2024
"""

KEY = "s3CR3Tk3Y".swapcase()

import sys, os
import random


def abcd() -> int:
    return ((((~(random.randint(0, 255))) << 2) ^ 0b10101010) & 0b01010101)

def efgh(x:int) -> int:
    return (((((~(random.randint(0, 4096)))) & 0b10101010) ^ x) | 0b01010101) % 256

def descrambleinator(x:bytes) -> bytes:
    random.seed(8008135)
    for i in range(len(x := bytearray(x))):
        x[i] ^= abcd() ^ efgh(i) ^ KEY.encode("utf-8")[i % len(KEY)]
    return bytes(x)


with open("Stardust-reckoning.txt.enc", "rb") as f:
    c = f.read()
    data = descrambleinator(c)
    print(data)