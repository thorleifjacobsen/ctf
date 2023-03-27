# tid_er_flagg (498)

Dette er den første oppgaven i en serie med sidekanalsangrep.

Sidekanalsangrep er en type angrep som går ut på å innhente ekstra informasjon uten å få direkte svar, hacke eller knekke noe. Dette kan være alt fra å måle strømtrekk, synkronisering av ulike typer informasjon eller måle tid.

Ofte er årsaken en grov feil, forenkling eller optimalisering i implementasjonen av en algoritme, mens selve standarden, protokollen eller algoritmen er uten feil.

I denne oppgaven vil du greie å lekke bittene til flagget hvis du setter av litt tid til å løse den.

Se intro/remote for introduksjon til oppkobling.

from pwn import *
io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-tid_er_flagg.chals.io", 443, ssl=True)
io.interactive()

# Writeup

The start of the `source.py` sets some rules for the flag:

```
alfabet = list((string.ascii_letters + string.digits + string.punctuation).encode())
assert all(ch in alfabet for ch in FLAG) == True
assert len(FLAG) > 50
assert len(FLAG) < 100
```

So signs, digits, letters and between 50 to 100 characters.

I noticed when manually entering bits on the server some were a bit slower than other to respond. Seems like high bits are taking longer time than low bits to access? Around half a second.

```
./sc helsectf2023-6ac4e1c6d8855c1bd96a-tid_er_flagg.chals.io
```

Wrote this python script to manually go through from 279 to 0. 

```
from pwn import *
import time

io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-tid_er_flagg.chals.io", 443, ssl=True)

for i in range(279, -1, -1): #280
    io.recvuntil(b"Hvilket bit skal vi aksessere? (bitindex er et tall mellom 0 .. 279) ")
    io.sendline(str(i).encode())
    io.recvuntil(b"vent litt, vi skal aksessere bitindex ")
    accessTimeStart = time.time()
    io.recvuntil(b"done")
    accessTime = time.time() - accessTimeStart
    print(1 if accessTime > 0.25 else 0, end="")
```

After run I get:

```
0110100001100101011011000111001101100101011000110111010001100110011110110011011100110001011001000101111101101011001101000100111001011111001100010011001101101011010010110110010101011111001100010100111001100110001100000111001001001101001101000011010101101010001100000100111001111101
```

Which is the binary representation of the flag.

# Flag

```
helsectf{71d_k4N_13kKe_1Nf0rM45j0N}
```