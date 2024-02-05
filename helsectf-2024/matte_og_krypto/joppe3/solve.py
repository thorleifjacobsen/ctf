from pwn import *
from numpy.polynomial.polynomial import Polynomial

# Disable logging
context.log_level = 'warn'

io = remote("helsectf2024-2da207d37b091b1b4dff-joppe3.chals.io", 443, ssl=True)

# Question 1
io.recvuntil(b":")
io.sendline(b"1")
io.recvuntil(b":")
io.sendline(b"barnebarn")
io.recvuntil(b": ")
secret1 = io.recvuntil(b"\r\n", drop = True).decode()
print(f"Secret 1: {secret1}")

# Question 2
io.recvuntil(b":")
io.sendline(b"2")
io.recvuntil(b":")
io.sendline(b"alle")
io.recvuntil(b": ")
secret2 = io.recvuntil(b"\r\n", drop = True).decode()
print(f"Secret 2: {secret2}")

# Question 3
io.recvuntil(b":")
io.sendline(b"3")
io.recvuntil(b":")
io.sendline(b"fyrstikken")
io.recvuntil(b": ")
secret3 = io.recvuntil(b"\r\n", drop = True).decode()
print(f"Secret 3: {secret3}")

# Question 4
io.recvuntil(b":")
io.sendline(b"4")
io.recvuntil(b":")
io.sendline(b"stearinlys")
io.recvuntil(b": ")
secret4 = io.recvuntil(b"\r\n", drop = True).decode()
print(f"Secret 4: {secret4}")

# Question 5
io.recvuntil(b":")
io.sendline(b"5")
io.recvuntil(b":")
io.sendline(b"hansker")
io.recvuntil(b": ")
secret5 = io.recvuntil(b"\r\n", drop = True).decode()
print(f"Secret 5: {secret5}")

# Parse secrets
secret1 = tuple(map(int, secret1.strip("()").split(",")))
secret2 = tuple(map(int, secret2.strip("()").split(",")))
secret3 = tuple(map(int, secret3.strip("()").split(",")))
secret4 = tuple(map(int, secret4.strip("()").split(",")))
secret5 = tuple(map(int, secret5.strip("()").split(",")))
secrets = [secret1, secret2, secret5]

# Solve the Shami's secret sharing thing:
from sympy import symbols, Eq, solve
a, b, c = symbols('a b c')

# Create equations based on the equation y = a + bx + cx^2
equations = [Eq(a + b*x + c*x**2, y) for x, y in secrets]

# Solve the equations
solved = solve(equations, (a, b, c))
a = solved[a]
b = solved[b]
c = solved[c]

solved = hex(int(a))[2:] # is decoded to: x=<somenumbers>
x = int(bytes.fromhex(solved).decode().split("=")[1]) # Extract x

print(f"a={a}")
print(f"b={b}")
print(f"c={c}")
print(f"x={x}")

y = symbols("y")
# Create equation to find Y based on the equation y = a + bx + cx^2
equations = [Eq(a + b*x + c*x**2, y)]
y = int(solve(equations,y)[y])
print(f"y={y}")
print("Flag:", bytes.fromhex(hex(y)[2:]).decode())
