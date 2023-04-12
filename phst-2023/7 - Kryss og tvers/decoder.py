import math
import base64


def forward_engineering(flagg):
    p1 = int("000".join([str(ord(c)) for c in flagg[:math.ceil(len(flagg)/3)]])) ^\
        int("000".join([str(ord(c)) for c in flagg[math.ceil(len(flagg)*2/3):]]))

    p2 = int("000".join([str(ord(c)) for c in flagg[math.ceil(len(flagg)/3):math.ceil(len(flagg)*2/3)]])) ^\
        int("000".join([str(ord(c) << 2) for c in flagg[math.ceil(len(flagg)*2/3):]]))

    p3 = p1 ^ int("000".join([str(ord(c)) for c in flagg[math.ceil(len(flagg)*2/3):]]))

    print(p1,p2,p3)
    jx = base64.b64encode("123456789".join([str(p1), str(p2), str(p3)]).encode("ascii"))
    with open("encoded.bin", "wb") as file:
        file.write(jx)

forward_engineering("Hey")
jx = open("encoded.bin", "rb").read()
jx_decoded = base64.b64decode(jx).decode().split("123456789")
p3 = jx_decoded[2]
p2 = jx_decoded[1]
p1 = jx_decoded[0]



print(p1,p2,p3)

# print(p3)