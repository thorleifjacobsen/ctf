from pwn import *
io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-remote.chals.io", 443, ssl=True)  
print(io.recvline().decode())    

