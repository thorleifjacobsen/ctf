# Codebreaker

After saving the crew you've been captured by the Xenithians, and your escape depends on predicting the next three numbers of their code which changes each attempt. Luckily, the Xenithians seem to have left out a crucial vulnerability when generating their code. Crack the code to be set free!

`nc uithack.td.org.uit.no 9001`

[⬇️ codebreaker.zip](./codebreaker.zip)

# Writeup

Quickly reading the code it seems that it want med to guess 3 numbers. It also seems like it's using the `rand` function to generate the numbers. It feeds [srand](https://cplusplus.com/reference/cstdlib/srand/) with the current time to get a random seed. It also leaks that seed to us. So we can just use the same seed to get the same numbers.

```python
from pwn import *
from ctypes import CDLL

context.log_level = 'warn'

p = remote("uithack.td.org.uit.no", 9001)

# Get the `time` which is used in the seed.
p.recvuntil(b"it shows: ")
time = int(p.recvline().decode().strip())

# Call the local libc version.
# I was not sure if i needed to extract this from the 
# docker image it is running on which we could. But 
# seems to run fine on the local libc version.
libc = CDLL("libc.so.6")
libc.srand(time)
libc.rand() # Get the first 4 numbers
libc.rand() # Get the first 4 numbers
libc.rand() # Get the first 4 numbers
libc.rand() # Get the first 4 numbers

p.recvuntil(b"Your guess: ")
# Now lets send the 3 next numbers it is asking for
p.sendline(str(libc.rand() % 34).encode())
p.sendline(str(libc.rand() % 34).encode())
p.sendline(str(libc.rand() % 34).encode())
p.recvuntil(b"UiTHack24{")
print("UiTHack24{" + p.recvuntil(b"}").decode().strip())
p.close()
```

Flag

```bash
$ python3 solve.py 
UiTHack24{X3n1th14n_3sc4p3}
```