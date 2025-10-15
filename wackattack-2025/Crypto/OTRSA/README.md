# OTRSA

I heard that encrypting every letter with a brand-new key provides perfect secrecy.
I used this idea to improve public-key cryptography.

[⬇️ OTRSA.tar.gz](./OTRSA.tar.gz)

# Writeup

```python
from Crypto.Util.number import getPrime

# Static exponent
e = 65537

# Crypting plaintextbyte ^ exponent ^ the generated modulus
def encrypt(pt, n):
    return pow(pt, e, n)

if __name__ == "__main__":

    # Gets flag
    with open("flag.txt", "rb") as f:
        flag = f.read()

    for f in flag:
        # Gets two random prime numbers to generate the modulus (n) for each byte.
        p = getPrime(1024)
        q = getPrime(1024)
        n = p*q
        ct = encrypt(f, n)
        # Prints CipherText Exponent and Modulus (B).
        print(ct, e, n)
```

We get all three numbers and the power of two of the numbers always become the third number. So basically we can brute the ciphertext, its one byte so 255 possible methods for each line in handout.txt.

What we do is that we use the modulus for each byte, the exponent and then try to cipher it and see if we get the same. If we do we end up with the plaintext flag.


```python
e = 65537
plaintext = []

with open("handout.txt") as f:
    for line in f:
        c, e_str, n = map(int, line.split())
        # Try all possible byte values (0–255)
        for m in range(256):
            if pow(m, e, n) == c:
                plaintext.append(m)
                break

print(bytes(plaintext))
```

# Flag

```
wack{1_f0r607_4b0U7_bRu73f0rc3}
```