# r2jail

Kan vi stole på en sandbox?

Koble til remote, og se om du får ut `/flag.txt`

PS: Det ligger ikke noe flagg i binarien.

```
from pwn import *
io = remote("helsectf2025-42694257c6fdb3976dd6-r2jail.chals.io", 443, ssl=True)
io.interactive()
```

# Writeup

Find references to flag.txt
```c
[0x00001080]> / flag.txt
Searching 8 bytes in [0x402e-0x4070]
hits: 0
Searching 8 bytes in [0x3db0-0x402e]
hits: 1
Searching 8 bytes in [0x2000-0x210c]
hits: 0
Searching 8 bytes in [0x1000-0x1211]
hits: 0
Searching 8 bytes in [0x0-0x718]
hits: 0
Searching 8 bytes in [0x4070-0x40d8]
hits: 0
0x00004025 hit5_0 .ab the flag at /flag.txt.
```

Foun `/flag.txt` from 0x4024 -> 9 bytes.
```c
[0x00001080]> px 9 @ 0x4024
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x00004024  2f66 6c61 672e 7478 74                   /flag.txt
```

Using AFL to list functions

```c
[0x00001080]> afl
0x00001080    1 38           entry0
0x00001060    1 10           sym.imp.puts
0x00001070    1 10           sym.imp.setvbuf
0x00001160    5 137  -> 60   entry.init0
0x00001120    5 57   -> 54   entry.fini0
0x00001050    1 10           fcn.00001050
0x000010b0    4 41   -> 34   fcn.000010b0
```

Used `pdf` to disassemble `fcn.000010b0` and found the flag.

```c
[0x00001080]> pdf @ fcn.000010b0
            ; CALL XREF from entry0 @ 0x10b0



# Flag

```

```