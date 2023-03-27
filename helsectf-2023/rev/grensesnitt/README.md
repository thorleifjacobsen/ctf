# grensesnitt (499)

Du kan koble til vårt grensesnitt for å kjøre kode.

Se intro/remote for introduksjon til oppkobling.

```python
from pwn import *
io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-grensesnitt.chals.io", 443, ssl=True)
io.interactive()
```

# Writeup

Tried that python script multiple times. Seems to not work on my computer? Only get this:

```
└─$ python remote.py 
[+] Opening connection to helsectf2023-6ac4e1c6d8855c1bd96a-grensesnitt.chals.io on port 443: Done
[*] Switching to interactive mode

kode> $ test

[*] Got EOF while reading in interactive
$ 
[*] Interrupted
[*] Closed connection to helsectf2023-6ac4e1c6d8855c1bd96a-grensesnitt.chals.io port 443
```

But tried snicat again and it seems to give me more:

```
$ ./sc helsectf2023-6ac4e1c6d8855c1bd96a-grensesnitt.chals.io
(connected to helsectf2023-6ac4e1c6d8855c1bd96a-grensesnitt.chals.io:443 and reading from stdin)
Vi har laget et grensesnitt for å printe data fra minne. Vårt minne er ikke så stort :(
Flagget ligger lagret i minne, og for å komme igang kan du printe Hello, world! 2 ganger med følende program:

    oioioioioioioioioioioioioiodddddddddddddoioioioioioioioioioioioioio

Gyldige instruksjoner er: i d o
kode> 
```

So we're supposed to do a memory leak, writing multiple `o` seems to only output multiple `H`, doing `oioo` seems to give `Hee`. And `oiodoio` gives `HeHe`. So I think I know what the instructions means:

```
i = increment posisiton
d = decrement position
o = output
```

So to output everything we just need to go backwards a lot.

```
ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddoioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioioio
```
resulted in 

```
z+J3*-;lU's{G,[helsectf{inc_dec_output!}
ja n
```

Curious me need to see what the memory contains, going a lot backwards and forwards this is the whole from the start. Start is at -55 and it has valid data until +113

```
helsectf{inc_dec_output!}
ja n@ er du p@ riktig vei!
Hello, world!
Du er p@ feil vei, pr0v den andre veien.
```

# Flag 

```
helsectf{inc_dec_output!}
```