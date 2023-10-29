# We temporary set the PNG header as the key, we'll replace one by one.
key = [137, 80, 78, 71, 13, 10, 26, 10]
out = []

with open("fileEncrypter/encrypted", "rb") as infile:
    data = list(infile.read())

# Loop through the first known 8 bytes to get the key:
for i in range(8):
    key[i] = data[i] ^ key[i]

# Now lets use the key to decrypt the file:
for i, val in enumerate(data):
    out.append(val ^ key[i % len(key)])

# Save to file and profit!
with open("decrypted.png", "wb") as outfile:
    outfile.write(bytes(out))
