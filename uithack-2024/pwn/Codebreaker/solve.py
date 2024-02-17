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