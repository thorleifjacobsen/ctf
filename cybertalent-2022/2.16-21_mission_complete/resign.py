from pwn import *
import ecdsa
import random
import libnum
import hashlib
import sys

privatekey = 114798114433974422739242357806023105894899569106244681546807278823326360043821

file = sys.argv[1] if len(sys.argv) > 1 else False

# Check whether a path pointing to a file
if os.path.isfile(file) == False:
    exit(f"File {file} does not exist")

with open(file, 'rb') as f:
    fileData = f.read()
    print(len(fileData))

    fileData = fileData.hex()
    signData = fileData[-128:]

if signData.startswith('260d633fe091a7ef'):
    print("This is signed, removing signature from upload")
    fileData = fileData[:-128]

fileData = bytes.fromhex(fileData)

h = int(sha256sumhex(fileData), base=16)

G = ecdsa.SECP256k1.generator
order = G.order()
Public_key = ecdsa.ecdsa.Public_key(G, G * privatekey)
x1 = ecdsa.ecdsa.Private_key(Public_key, privatekey)
k = random.randrange(1, 2**127)
sign = x1.sign(h, k)


newSign = sign.r.to_bytes(32, "big") + sign.s.to_bytes(32, "big")

fileData += newSign


print("Old sign: ",signData)
newSign = fileData.hex()[-128:]
print("New sign: ",newSign)
print(len(fileData))
with open(f"{file}_signed", 'wb') as f:
    f.write(fileData)
