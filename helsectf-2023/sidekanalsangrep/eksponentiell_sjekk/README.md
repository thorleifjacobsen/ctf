# eksponentiell_sjekk (500)
I den andre oppgaven om sidekanalsangrep er selve sårbarheten mer kamuflert.

Det eneste du kan gjøre er å sjekke om du vet hele flagget, eller ikke. Se ellers intro/remote for introduksjon til oppkobling.

from pwn import *
io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-eksponentiell_sjekk.chals.io", 443, ssl=True)
io.interactive()

[souce.py](source.py)

# Writeup

Seeing as this is a side channel attack we can do some side channel analysis. The app seems to do a pretty heavy hashing if we meet the length requirement. 


```python
def strcmp(s1,s2):
    if len(s1) != len(s2):        
        return False
    for i in range(len(s1)):
        if hash(s1[i]^s2[i]) != 0:
            return False
    return True
```

Using this we should see a bit of time increase if we bypass the first check. Creating a simple script to do this just sending 2 FF's at a time. We know it is between 51 and 99 characters long so we dont have to check em all. The reason I send FF is that this is 255 and the highest number we can send to it which also uses more time. Easier to spot. 

Out comes [solve.py](solve.py)

```python
from pwn import *
import time
io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-eksponentiell_sjekk.chals.io", 443, ssl=True)

print(io.recvuntil(b"flagget?").decode())

for i in range(51, 100):
    start = time.time()*1000
    io.sendline(b"FF"*i)

    io.recvuntil(b"flagget?")
    end = round(time.time()*1000 - start)
    print(f"Testing length {i} - Time used: {end}ms")
```

This resulted in this output:

```
Testing length 51 - Time used: 96ms
Testing length 52 - Time used: 157ms
Testing length 53 - Time used: 96ms
Testing length NN - Time used: ~95ms
```

So most running only the if check takes around 96ms, but at 52 characters it takes around 60 ms more. This means we're in the hash function with 255 number. If we try a lower number e.g. 0 we would not be able to identify when we enter it.

So to leak data now we just need to send 52 bytes of 255 and alter the first byte until we see a spike in time use. So pretend that everything is padded up to 52 bytes of 256. If I put an "A" as the first character it would fail much faster thn 255. So around 100ms time before it returns wrong flag. But once I hit the correct one it will progress to the second byte which still is 256 and takes a whole lot longer time. So when we loop through the allowed characters once it hits `h` (start of flag) it will hash that value (104) which goes pretty fast. But then it will try to hash the second character which is 255 and takes longer time. This way we can identify that we managed to progress by 1 character and we know it.

So I build a script using that loops through 52 characters and does this simple time check and selects the character with the highest time. I've seen that there are some false positives so I added a double check if I got some high values. That was almost perfect and [this script](solve.py) gave me this:

```
helsectf{f@il_Fas7_a|g0ritmeR_k4N_L3Kke_1NfOrM45j0nR
```

I call that close enough, that is 52 letters so I know the last should be `}`. The reason it is hard to find out the last is that we do not run the hashing function on a next character so nearly any I try on the last character place will be around 100ms.

# Flag

```
helsectf{f@il_Fas7_a|g0ritmeR_k4N_L3Kke_1NfOrM45j0n}
```