from pwn import *
from Crypto.Util.number import bytes_to_long, inverse

context.log_level = "warn"

# The original contract
contract = b"Dette er en superviktig kontrakt for veeldig viktige ting med store ord og uforstaaelige kruseduller."
contract_long = bytes_to_long(contract)

# RSA Parameters
e = 0x10001
N = "Will be received upon connection"
r = 10 # Just a random value

# Connection:
io = remote("helsectf2024-2da207d37b091b1b4dff-kontraktsignering.chals.io", 443, ssl=True)
io.recvuntil(b"N=")
N = int(io.recvuntil(b"\n", drop = True).decode())
io.recvuntil(b">")
io.sendline(b"sign")
io.recvuntil(b"message=")
# Blind the message so the server cannot see what it contains
m_blind = (contract_long * pow(r, e)) % N
io.sendline(hex(m_blind)[2:].encode())
io.recvuntil(b"sign= ")
# Receive the signed blind message
s_blind = int(io.recvuntil(b"\n", drop = True).decode(), 16)
# Unblind the signed message
s = (s_blind * inverse(r, N)) % N
# Now s is the signed contract which we can verify
s_hex = hex(s)[2:]
io.sendline(b"verify")
io.recvuntil(b"signature=")
io.sendline(s_hex.encode())
print(io.recvall(timeout = 2).decode())
io.close()
