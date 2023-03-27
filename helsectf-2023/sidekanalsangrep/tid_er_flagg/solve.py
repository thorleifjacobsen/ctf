from pwn import *
import time

io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-tid_er_flagg.chals.io", 443, ssl=True)

for i in range(279, -1, -1): #280
    io.recvuntil(b"Hvilket bit skal vi aksessere? (bitindex er et tall mellom 0 .. 279) ")
    io.sendline(str(i).encode())
    io.recvuntil(b"vent litt, vi skal aksessere bitindex ")
    accessTimeStart = time.time()
    io.recvuntil(b"done")
    accessTime = time.time() - accessTimeStart
    print(1 if accessTime > 0.25 else 0, end="")