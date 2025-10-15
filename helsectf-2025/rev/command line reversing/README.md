# command line reversing

Radare2 (r2) er et rammeverk for REVerse engineering og analysere binaries:
- https://github.com/radareorg/radare2

For å komme igang kan det kanskje være kjekt med en jukselapp:
- https://github.com/radareorg/radare2/blob/master/doc/intro.md

Jeg hjelper deg litt på veien, prøv dette i r2 consolet:
```
aaa
afl
iS
f~flag
s sym.main
pdf
```

Koble til remote, og se om du kan reverse engineer deg frem til et flagg! Lykke til!

```
from pwn import *
io = remote("helsectf2025-42694257c6fdb3976dd6-command-line-reversing.chals.io", 443, ssl=True)
io.interactive()
```

# Writeup

<Enter writeup here>

# Flag

```
flag{goes_here}
```