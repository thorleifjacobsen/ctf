╞══════════════════════════════════════════════════════════════════════════════╡
│ program name > findflag.prg                                                  │ 
│ 000000 | 05.7c.40.93 | sxtw  x5, w0                                          │ Move stdout to x5
│ 000004 | 08.07.80.d2 | movz  x8, #0x38                                       │ | x8 Openat
│ 000008 | 60.0c.80.92 | movn  x0, #0x63                                       │ | param1: 99
│ 00000c | 01.00.00.90 | adrp  x1, #0                                          │ | param2: Memory lokasjo nfor "."
│ 000010 | 02.00.88.d2 | movz  x2, #0x4000                                     │ | param3: 0x4000
│ 000014 | 21.f0.03.91 | add   x1, x1, #0xfc                                   │ | (fix param2)
│ 000018 | 01.00.00.d4 | svc   #0                                              │ | - execute
│ 00001c | 40.04.f8.37 | tbnz  w0, #0x1f, #0xa4                                │ | somehow check return value, if it fails it jumps to a4
│ 000020 | ff.07.40.d1 | sub   sp, sp, #1, lsl #12                             │
│ 000024 | 0a.00.00.90 | adrp  x10, #0                                         │
│ 000028 | 07.7c.40.93 | sxtw  x7, w0                                          │
│ 00002c | eb.03.00.91 | mov   x11, sp                                         │
│ 000030 | 4a.e1.03.91 | add   x10, x10, #0xf8                                 │
│ 000034 | e0.03.07.aa | mov   x0, x7                                          │
│ 000038 | e1.03.0b.aa | mov   x1, x11                                         │
│ 00003c | a8.07.80.d2 | movz  x8, #0x3d                                       │
│ 000040 | 02.00.82.d2 | movz  x2, #0x1000                                     │
│ 000044 | 01.00.00.d4 | svc   #0                                              │
│ 000048 | 1f.00.00.71 | cmp   w0, #0                                          │
│ 00004c | 0d.02.00.54 | b.le  #0x8c                                           │
│ 000050 | 04.7c.40.93 | sxtw  x4, w0                                          │
│ 000054 | 06.00.80.d2 | movz  x6, #0                                          │
│ 000058 | 69.01.06.8b | add   x9, x11, x6                                     │
│ 00005c | 20.49.40.39 | ldrb  w0, [x9, #0x12]                                 │
│ 000060 | 1f.20.00.71 | cmp   w0, #8                                          │
│ 000064 | 01.04.00.54 | b.ne  #0xe4                                           │
│ 000068 | 21.4d.00.91 | add   x1, x9, #0x13                                   │
│ 00006c | 00.00.80.d2 | movz  x0, #0                                          │
│ 000070 | 42.69.60.38 | ldrb  w2, [x10, x0]                                   │
│ 000074 | c2.01.00.34 | cbz   w2, #0xac                                       │
│ 000078 | 23.68.60.38 | ldrb  w3, [x1, x0]                                    │
│ 00007c | 7f.00.02.6b | cmp   w3, w2                                          │
│ 000080 | 21.03.00.54 | b.ne  #0xe4                                           │
│ 000084 | 00.04.00.91 | add   x0, x0, #1                                      │
│ 000088 | fa.ff.ff.17 | b     #0x70                                           │
│ 00008c | 28.07.80.d2 | movz  x8, #0x39                                       │
│ 000090 | e0.03.07.aa | mov   x0, x7                                          │
│ 000094 | 01.00.00.d4 | svc   #0                                              │
│ 000098 | 00.00.80.52 | movz  w0, #0                                          │
│ 00009c | ff.07.40.91 | add   sp, sp, #1, lsl #12                             │
│ 0000a0 | c0.03.5f.d6 | ret                                                   │
│ 0000a4 | 00.00.80.12 | movn  w0, #0                                          │ - failed
│ 0000a8 | c0.03.5f.d6 | ret                                                   │
│ 0000ac | 08.07.80.d2 | movz  x8, #0x38                                       │
│ 0000b0 | 60.0c.80.92 | movn  x0, #0x63                                       │
│ 0000b4 | 02.00.80.d2 | movz  x2, #0                                          │
│ 0000b8 | 01.00.00.d4 | svc   #0                                              │
│ 0000bc | 1f.00.00.71 | cmp   w0, #0                                          │
│ 0000c0 | 01.7c.40.93 | sxtw  x1, w0                                          │
│ 0000c4 | ad.00.00.54 | b.le  #0xd8                                           │
│ 0000c8 | e8.08.80.d2 | movz  x8, #0x47                                       │
│ 0000cc | e0.03.05.aa | mov   x0, x5                                          │
│ 0000d0 | 03.02.a0.d2 | movz  x3, #0x10, lsl #16                              │
│ 0000d4 | 01.00.00.d4 | svc   #0                                              │
│ 0000d8 | 28.07.80.d2 | movz  x8, #0x39                                       │
│ 0000dc | e0.03.01.aa | mov   x0, x1                                          │
│ 0000e0 | 01.00.00.d4 | svc   #0                                              │
│ 0000e4 | 20.21.40.79 | ldrh  w0, [x9, #0x10]                                 │
│ 0000e8 | c6.00.00.8b | add   x6, x6, x0                                      │
│ 0000ec | 9f.00.06.eb | cmp   x4, x6                                          │
│ 0000f0 | 48.fb.ff.54 | b.hi  #0x58                                           │
│ 0000f4 | d0.ff.ff.17 | b     #0x34                                           │
│ 0000f8 | 46 4c 41 47 2e 00                               | FLAG..            │