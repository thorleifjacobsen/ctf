from pwn import *

while True:
    r = process(['./dice_handout/dice_game'])
    r = remote("ctf.wackattack.eu", 5011)

    r.recvuntil(b"0)?")
    r.sendline(b"1")
    

    while True:
        line = r.recvline()
        if b"Won: " in line:
            print(line)
            r.close()
            exit()
            break
        elif b"(y/n)" in line:
            r.sendline(b"y")
        elif b"You rolled" in line:
            line = line.decode()
            line = line.split(" ")
            print(f"Roll: {line[2]}")
        elif b"Thank you for playing" in line:
            r.close()
            break