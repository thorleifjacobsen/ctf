from string import ascii_uppercase
import random
import os

flag = os.environ.get("FLAG", "wack{demo_flag}")

with open("./plaintext.txt") as f:
    data = f.read().strip().upper()
    data = "".join(c for c in data if c in ascii_uppercase)
    print(data)


def encrypt(pt, key):
    number_key = [ascii_uppercase.index(k) for k in key] * (len(pt) // len(key) + 2)
    ct = ""
    for p, k in zip(pt, number_key):
        ct += ascii_uppercase[(ascii_uppercase.index(p) + k) % len(ascii_uppercase)]
    return ct

if __name__ == "__main__":
    text1 = "Welcome to vigenereathon"
    text2 = "Here you will have to solve 1000 instances of the viginere cipher, dcode.fr will not save you now"
    lpadding = (len(text2)-len(text1)) // 2
    rpadding = (len(text2)-len(text1)) // 2 + ((len(text2)-len(text1)) % 2)
    print( "+ " + "-"*len(text2) + " +")
    print( "| " + " " * lpadding + text1 + " " * rpadding + "|")
    print( "| " + text2 + " |")
    print( "+ " + "-"*len(text2) + " +")
    input("Are you ready?")

    for i in range(1000):
        textofset = random.randrange(0, len(data) - 1400)
        keylen = random.randrange(4, 8)
        key = "".join(random.choices(ascii_uppercase, k=keylen))
        pt = data[textofset: textofset + 1400]
        ct = encrypt(pt, key)
        print("Here is some ciphertext")
        print(ct)
        print("What is the coresponding plaintext")
        innput_pt = input("> ")
        if innput_pt != pt:
            print(f"That is not correct, the correct key was {key}")
            exit()
        print("That is correct")
    print("Very good here is a flag as a reward")
    print(flag)

