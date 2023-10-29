# File Encrypter (easy)

We have intercepted an encrypted picture of a malicious circuit board. The encryption is quite bad, so you do not have to be a wizard to solve it, but some known magic would not hurt.

Author: oksenmu

📎 [fileencrypter_handout.tar.gz](fileencrypter_handout.tar.gz)

# Writeup

Reading the code we see this is a basic XOR cipher. They use a 8 byte long key to XOR a PNG image. XOR is a reversible operation and two of the tree values used in XOR can be used to get the last. So we can XOR the encrypted image with the key to get the original image. Or we can XOR the encrypted image with the original image to get the key. But we dont have the original image?

So what can we use? We know the PNG header is 8 bytes long so we can XOR the encrypted image with the PNG header to get 8 bytes for the key.

```python
with open("fileEncrypter/encrypted", "rb") as infile:
    data = list(infile.read())

# PNG Header
key = [137, 80, 78, 71, 13, 10, 26, 10]

# Loop through the first 8 bytes from the data
for i in range(8):
    key[i] = data[i] ^ key[i]

print(key)
```

This returns:

```python
[51, 181, 76, 39, 187, 155, 36, 209]
```

We now have the key so we can easily decrypt the rest of the image:

```python
with open("fileEncrypter/encrypted", "rb") as infile:
    data = list(infile.read())

out = []
key = [51, 181, 76, 39, 187, 155, 36, 209]

for i, val in enumerate(data):
    out.append(val ^ key[i % len(key)])

with open("decrypted.png", "wb") as outfile:
    outfile.write(bytes(out))
    
```

And here it is:

![decrypted.png](decrypted.png)

# Flag

```
wack{x0r3d_7h3_m4g1c_8y735}
```