
# denne dumper 0xFFF bytes av stack til console
sxtw x4, w0
mov x0, x4
mov x1, sp
mov x2, 0xFFF
mov x8, #0x40
svc #0
mov w0, #0
ret

HEX: 047c4093e00304aae1030091e2ff81d2080880d2010000d400008052c0035fd6

# Psudo code av telemetry.prg

c = open(AF_LOCAL, SOCK_STREAM, SOCK_NONBLOCK)
connect(c, "127.0.0.1:1025")
write(c, "tele")
while(data = read(fd, 256)) {
    write(stdout, data)
}
close(c)
return 0

