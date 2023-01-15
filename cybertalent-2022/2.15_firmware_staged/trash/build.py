
# importing the requests library
import requests
import sys

filename = sys.argv[1]

with open(filename) as f:
    asm = f.read()

r = requests.post('https://armconverter.com/api/convert', json={
  "asm": asm,
  "offset": "",
  "arch": "arm64"
})

data = r.json()['hex']['arm64'][1].lower().replace("\n", "")
valid = r.json()['hex']['arm64'][0]

print(f"{data}")


# Build payload
#0xBC == 188
#0xCC = 204
# ip  = "020004017f0000010000000000000000" # AF_INET, port 1025, 127.0.0.1
# payload  = "flsh".encode().hex()
# payload += p16(1).hex() # Sub
# payload += p16(1).hex() # Missile

# with open("missile.1.3.37.fw", 'rb') as f:
#     hex_data = f.read().hex()

# payload += hex_data


