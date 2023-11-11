from Cryptodome.Cipher import AES
from base64 import b64decode
import json

key = ""

hex_str1 = "980daad49738f76b80c8fafb0673ff1b"
hex_str2 = "a3c5a5a81ebc62c6144a9dc1ae5cce11"
hex_str3 = "fc78e6fee2138b798e1e51ed15e0a109"

# Convert hexadecimal strings to bytes
bytes1 = bytes.fromhex(hex_str1)
bytes2 = bytes.fromhex(hex_str2)
bytes3 = bytes.fromhex(hex_str3)

# Perform byte-wise addition
result = bytes(x ^ y ^ z for x, y, z in zip(bytes1, bytes2, bytes3))

# Convert the resulting bytes back to a hexadecimal string
result_hex = result.hex()
key = result_hex
print(result_hex)
# Print key length
print("Key length: " + str(len(key)))

with open("melding.enc", "rb") as f:
    data = json.loads(f.read())
    nonce = b64decode(data["nonce"])
    ciphertext = b64decode(data["ciphertext"])
    tag = b64decode(data["tag"])
    cipher = AES.new(key, AES.MODE_GCM, nonce = nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    print("Dekryptert melding: " + plaintext.decode('utf-8'))
