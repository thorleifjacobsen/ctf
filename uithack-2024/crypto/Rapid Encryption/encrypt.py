from Crypto.Util.number import bytes_to_long, getPrime

with open("flag.txt", "rb") as f:
    flag = f.read().strip()

e = 3
p = getPrime(512)
q = getPrime(512)
n = p * q
m = bytes_to_long(flag)

ct = pow(m, e, n)
print(f"{ct=}")
print(f"{n=}")
print(f"{e=}")