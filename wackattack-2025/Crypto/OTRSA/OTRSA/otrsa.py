from Crypto.Util.number import getPrime

e = 65537

def encrypt(pt, n):
    return pow(pt, e, n)

if __name__ == "__main__":


    with open("flag.txt", "rb") as f:
        flag = f.read()

    for f in flag:
        p = getPrime(1024)
        q = getPrime(1024)
        n = p*q
        ct = encrypt(f, n)
        print(ct, e, n)


