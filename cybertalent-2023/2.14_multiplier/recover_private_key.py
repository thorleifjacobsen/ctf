
from Crypto.Util.number import bytes_to_long
from Crypto.Hash import SHA256
import ecdsa, libnum, sys

file1 = sys.argv[1] if len(sys.argv) > 1 else "missile.1.3.37.fw"
file2 = sys.argv[2] if len(sys.argv) > 2 else "test.txt_signed"


with open(file1, 'rb') as f:
    f1 = f.read()
    r1 = bytes_to_long(f1[-64:-32])
    s1 = bytes_to_long(f1[-32:])
    f1 = f1[:-64]
    f1_h = SHA256.new()
    f1_h.update(f1)
    h1 = int(f1_h.hexdigest(), base=16)

with open(file2, 'rb') as f:
    f2 = f.read()
    r2 = bytes_to_long(f2[-64:-32])
    s2 = bytes_to_long(f2[-32:])
    f2 = f2[:-64]
    f2_h = SHA256.new()
    f2_h.update(f2)
    h2 = int(f2_h.hexdigest(), base=16)

print(file1)
print(f"r: {r1}\ns: {s1}\nsha256: {h1}\n")
print(file2)
print(f"r: {r2}\ns: {s2}\nsha256: {h2}\n")

G = ecdsa.SECP256k1.generator
order = G.order()

valinv = libnum.invmod( r1*(s1-s2),order)
x1rec = (   (s2*h1-s1*h2) * (valinv)) % order
print (f"Private recovered:\n{x1rec}")
# valinv = libnum.invmod( (s1-s2),order)
# k1rec = (   (h1-h2) * valinv) % order
# print ("\nK recovered ",k1rec)