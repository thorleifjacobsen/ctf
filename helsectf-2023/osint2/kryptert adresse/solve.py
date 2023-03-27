encryptedHex = "72f8a3a1bf16dd894894553a4adf624ed82408090c7908d920c3be82b856e7a60ca3426971897c62d8152304256913a576ce859b8120dcb824b2603b5f"

def encrypt(data, i):
    ct = bytearray(len(data))
    s = i
    for idx, byte in enumerate(data):
        s = (0x13 * s + 0x32) % 0xff
        ct[idx] = byte ^ s
    return ct

key = 26

# Find key
for i in range(0,0xff):
    if encrypt(b"helsectf", i).hex() in encryptedHex:
        print("Bingo", i)
        key = i
        break
print(f"Testing with key {key}")

# Brute the system    
confirmed = "helse"
for x in range(0, 30):
    for i in range(0,256): 
        letter = chr(i)
        attempt = f"{confirmed}{letter}".encode()
        hexValue = encrypt(attempt, key).hex()
        if hexValue in encryptedHex:
            confirmed += letter

print(confirmed)
