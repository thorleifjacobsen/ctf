from pwn import *

context.log_level = 'error'
p = remote('185.125.168.82', 2337)
p.recvuntil(b'?')

for i in range(1,1000):
    p.sendline(str(i).encode())
    ans = p.recvline().decode()
    if 'No.' not in ans:
        print(i, ans)
        p.interactive()
        break
    