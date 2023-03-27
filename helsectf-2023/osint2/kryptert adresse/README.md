# kryptert adresse (500)

pAAskeharen er fremdeles redd for at noen kan finne adressen til eggleveransen. Han har derfor bedt om ekstern bistand, fra selveste Krypto Kyllingen.

Krypto Kyllingen har analysert adressen og funnet ut at den både er lineær og kongruent! Dermed får han lagret den trygt i en smartkontrakt slik at ingen uvedkommende kan lese den, håper han..

[Encryptor.sol](Encryptor.sol)

# Writeup

I started the same way as the original to run the `Encryptor.sol` script. Using that I got an hex value which pososible is the encrypted address. From that I got something that possbile is the decrypted data. 

```
0x72f8a3a1bf16dd894894553a4adf624ed82408090c7908d920c3be82b856e7a60ca3426971897c62d8152304256913a576ce859b8120dcb824b2603b5f
```

I see that I need the hidden `s0` value which `Encyptor.sol` has hidden. I have no idea on what to do so try a bit different things. ChatGPT, Google. Then I find out that bruteforce might be the simple method.

```python
def encrypt(data, key):
    ct = bytearray(len(data))
    s = key
    for idx, byte in enumerate(data.encode()):
        s = (0x13 * s + 0x32) % 0xff
        ct[idx] = byte ^ s
    return ct.hex()

for i in range(0,0xff):
    if encrypt("helsectf", i) in "72f8a3a1bf16dd894894553a4adf624ed82408090c7908d920c3be82b856e7a60ca3426971897c62d8152304256913a576ce859b8120dcb824b2603b5f":
        print("Bingo", i)
```

This script is the same encrypt encrypt function so I'm basically encrypting the bytext helsectf and comparing them with the hext string I have. Looping form 0 until 255 as the key. The problem here is that the key could be in multiple of thousands, billions e.t.c. But as everything is a byte hex in the script I run this and cross my fingers.

```
$ python solve.py
Bingo 26
```

Eehem, well that was easy? With my new knowledge I can create a decrypt function as I now have the key! All hail the key holder! :) I try a bit to find out how to reverse, but I end up creating a bruteforce script kinda by accident. But somehow It gave me a flag. 

[solve.py](solve.py)

# Flag

```
helsectf{ikK3_oFt3_AdResS3r_eR_kRyp7eRT_MEd_LCG!}
```