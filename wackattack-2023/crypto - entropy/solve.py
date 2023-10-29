import random
import base64

# Base64 encoded ciphertext
var = "LphpCmqgeVl37rTsD0WTVSMjwrDp6pvbM44CoFD2yhClx0kAs0dInVdReA=="

# Decode the base64 encoded ciphertext
ciphertext = base64.b64decode(var)

# Recreate the key using the same seed
msg = "I made this encryption system just for you!"
r = random.Random()
r.seed(msg)
key = [f ^ r.randint(0, 255) for f in ciphertext]

# XOR the key with the ciphertext to recover the original message
original_message = bytes(c ^ k for c, k in zip(ciphertext, key)).decode()

print(original_message)
