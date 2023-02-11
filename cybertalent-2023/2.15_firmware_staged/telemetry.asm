│ 000000 | 04.7c.40.93 | sxtw  x4, w0                                          │ Mode 32bit data from w0 to 64bit register x4 (x4 is actually stdout)
│ 000004 | c8.18.80.d2 | movz  x8, #0xc6                                       │ | syscal no.198: socket https://man7.org/linux/man-pages/man2/socket.2.html
│ 000008 | 40.00.80.d2 | movz  x0, #0x2                                        │ | param1: AF_LOCAL
│ 00000c | 21.00.80.d2 | movz  x1, #0x1                                        │ | param2: SOCK_STREAM
│ 000010 | c2.00.80.d2 | movz  x2, #0x6                                        │ | param3: SOCK_NONBLOCK
│ 000014 | 01.00.00.d4 | svc   #0                                              │ | --- EXECUTE
│ 000018 | e0.04.f8.37 | tbnz  w0, #0x1f, #0xb4                                │ Check return value of the above syscall, if it is not zero jump to 0xb4 (exit)
│ 00001c | 03.7c.40.93 | sxtw  x3, w0                                          │ Move the file descriptor to x3 for storage.
│ 000020 | 68.19.80.d2 | movz  x8, #0xcb                                       │ | syscal no.203: connect https://man7.org/linux/man-pages/man2/connect.2.html
│ 000024 | e0.03.03.aa | mov   x0, x3                                          │ | param1: fd
│ 000028 | 01.00.00.90 | adrp  x1, #0                                          │ | param2: 0xc4 (02 00 04 01 7f 00 00 01 00 00 00 00 00 00 00 00)
│ 00002c | 02.02.80.d2 | movz  x2, #0x10                                       │ | param3: 0x10 (dec 16)
│ 000030 | 21.10.03.91 | add   x1, x1, #0xc4                                   │ | param2: modify
│ 000034 | 01.00.00.d4 | svc   #0                                              │ | --- EXECUTE
│ 000038 | 1f.04.00.31 | cmn   w0, #1                                          │ Compare result of connect with 1. 
│ 00003c | 60.03.00.54 | b.eq  #0xa8                                           │ Branch if equal to 0xa8 (close socket, then exit program)
│ 000040 | 01.00.00.90 | adrp  x1, #0                                          │ Set x1 to 0
│ 000044 | ff.03.04.d1 | sub   sp, sp, #0x100                                  │ Substract stack pointer with 256. 
│ 000048 | 08.08.80.d2 | movz  x8, #0x40                                       │ | syscall no.64 : write https://man7.org/linux/man-pages/man2/write.2.html
│ 00004c | e0.03.03.aa | mov   x0, x3                                          │ | param1: fd
│ 000050 | 21.f0.02.91 | add   x1, x1, #0xbc                                   │ | param2: 0xbc (75 65 6c 65 = tele)
│ 000054 | 82.00.80.d2 | movz  x2, #0x4                                        │ | param3: 4 bytes
│ 000058 | 01.00.00.d4 | svc   #0                                              │ | --- EXECUTE
│ 00005c | e5.03.00.91 | mov   x5, sp                                          │ Save stack pointer to x5
│ 000060 | e0.03.03.aa | mov   x0, x3                                          │ | param1: fd
│ 000064 | e1.03.05.aa | mov   x1, x5                                          │ | param2: x5 (stack pointer start)
│ 000068 | e8.07.80.d2 | movz  x8, #0x3f                                       │ | syscall no.63 : read https://man7.org/linux/man-pages/man2/read.2.html
│ 00006c | 02.20.80.d2 | movz  x2, #0x100                                      │ | param3: 256
│ 000070 | 01.00.00.d4 | svc   #0                                              │ | --- EXECUTE (This reads 256 bytes into stack)
│ 000074 | e2.03.00.aa | mov   x2, x0                                          │ Move result from x0 to x2 (result is number of bytes read)
│ 000078 | 1f.00.00.f1 | cmp   x0, #0                                          │ Compare x0 with 0 bytes of data
│ 00007c | ad.00.00.54 | b.le  #0x90                                           │ Branch if less or equal to 0, jump to: 0x90  (close socket, then exit program)
│ 000080 | e0.03.04.aa | mov   x0, x4                                          │ | param1: x4 (whatever that is?)
│ 000084 | 08.08.80.d2 | movz  x8, #0x40                                       │ | syscall no.64 : write https://man7.org/linux/man-pages/man2/write.2.html
│ 000088 | 01.00.00.d4 | svc   #0                                              │ | -- EXECUTE (param1 is still SP, param2  x2 is number of bytes read, so this prints out to screen)
│ 00008c | f5.ff.ff.17 | b     #0x60                                           │ Branch to 0x60, to re-read until we read 0 bytes.
│ 000090 | 28.07.80.d2 | movz  x8, #0x39                                       │ | syscall no.57 : close https://man7.org/linux/man-pages/man2/close.2.html
│ 000094 | e0.03.03.aa | mov   x0, x3                                          │ | param1: fd of socket (got from x3)
│ 000098 | 01.00.00.d4 | svc   #0                                              │ | --- EXECUTE
│ 00009c | 00.00.80.52 | movz  w0, #0                                          │ Set the lower 32 bites of x0 to 0's.
│ 0000a0 | ff.03.04.91 | add   sp, sp, #0x100                                  │ Add 256 to stack pointer.
│ 0000a4 | c0.03.5f.d6 | ret                                                   │ return
│ 0000a8 | 28.07.80.d2 | movz  x8, #0x39                                       │ | syscall no.57 : close https://man7.org/linux/man-pages/man2/close.2.html
│ 0000ac | e0.03.03.aa | mov   x0, x3                                          │ | param1: fd of socket (got from x3)
│ 0000b0 | 01.00.00.d4 | svc   #0                                              │ | --- EXECUTE
│ 0000b4 | 00.00.80.52 | movz  w0, #0                                          │ Set the lower 32 bites of x0 to 0's.
│ 0000b8 | c0.03.5f.d6 | ret                                                   │ return
│ 0000bc | 74 65 6c 65 00 00 00 00 02 00 04 01 7f 00 00 01 | tele............  │ .DATA
│ 0000cc | 00 00 00 00 00 00 00 00                         | ........          │ .DATA
