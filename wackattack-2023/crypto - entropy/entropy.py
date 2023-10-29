import random
import base64

flag = ""
with open("flag.txt", "rb") as f:
    flag = f.read()

msg = "I made this encryption system just for you!"

r = random.Random()
r.seed(msg)

key = [f ^ r.randint(0, 255) for f in flag]

c = [m ^ k for m, k in zip(msg.encode(), key)]

print(base64.b64encode(bytes(c)).decode())

# Output:
# LphpCmqgeVl37rTsD0WTVSMjwrDp6pvbM44CoFD2yhClx0kAs0dInVdReA==


# Now we can use the same code to recover the flag

ciphertext = base64.b64decode("LphpCmqgeVl37rTsD0WTVSMjwrDp6pvbM44CoFD2yhClx0kAs0dInVdReA==")

i = 0
r.seed(msg)
for c in ciphertext:
    k = (c ^ msg.encode()[i]) ^ r.randint(0, 255)
    print(chr(k), end="")
    i += 1

