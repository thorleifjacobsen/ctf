from pwn import *

# Disable logging
context.log_level = 'warn'

io = remote("helsectf2024-2da207d37b091b1b4dff-joppe1.chals.io", 443, ssl=True)

# Question 1
io.recvuntil(b":")
io.sendline(b"1")
io.recvuntil(b":")
io.sendline(b"ingenting")
io.recvuntil(b": ")
secret1 = io.recvuntil(b"\r\n", drop = True).decode()
print(f"Secret 1: {secret1}")

# Question 2
io.recvuntil(b":")
io.sendline(b"2")
io.recvuntil(b":")
io.sendline(b"gikk")
io.recvuntil(b": ")
secret2 = io.recvuntil(b"\r\n", drop = True).decode()
print(f"Secret 2: {secret2}")

# Question 3
io.recvuntil(b":")
io.recvuntil(b":")
io.sendline(b"3")
io.recvuntil(b":")
io.sendline("Håndkle".encode('utf-8'))
io.recvuntil(b": ")
secret3 = io.recvuntil(b"\r\n", drop = True).decode()
print(f"Secret 3: {secret3}")

# Parse secrets
secret1 = tuple(map(int, secret1.strip("()").split(",")))
secret2 = tuple(map(int, secret2.strip("()").split(",")))
secret3 = tuple(map(int, secret3.strip("()").split(",")))
secrets = [secret1, secret2, secret3]

# Solve the Shami's secret sharing thing:
from sympy import symbols, Eq, solve
a, b, c = symbols('a b c')

# Create equations based on the equation y = a + bx + cx^2
equations = [Eq(a + b*x + c*x**2, y) for x, y in secrets]

# Solve the equations
secret = solve(equations, (a, b, c))[a]

print(f"Code: {secret}")

# Test code
io.recvuntil(b":")
io.recvuntil(b":")
io.sendline(b"4")
io.recvuntil(b": ")
io.sendline(str(secret).encode())
print(f"Flag: {io.recvuntil(b'}').decode()}")
io.close()
