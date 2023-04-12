import math
import base64


def forward_engineering(flagg):
    p1 = int("000".join([str(ord(c)) for c in flagg[:math.ceil(len(flagg)/3)]])) ^\
        int("000".join([str(ord(c)) for c in flagg[math.ceil(len(flagg)*2/3):]]))

    p2 = int("000".join([str(ord(c)) for c in flagg[math.ceil(len(flagg)/3):math.ceil(len(flagg)*2/3)]])) ^\
        int("000".join([str(ord(c) << 2) for c in flagg[math.ceil(len(flagg)*2/3):]]))

    p3 = p1 ^ int("000".join([str(ord(c)) for c in flagg[math.ceil(len(flagg)*2/3):]]))

    jx = base64.b64encode("123456789".join([str(p1), str(p2), str(p3)]).encode("ascii"))

    with open("encoded.bin", "wb") as file:
        file.write(jx)

