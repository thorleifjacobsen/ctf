
ct = bytes.fromhex("f8f3c9ddefd1f5c8feeef1c7dec8f8edcbefc3ccfdc1f6fdf5d3f0f8f1c7cbcef5c1fafddcc5e3c1f6fdf5ccf4fffffdce81b0bfb5e5")

key = [0] * 6 
key[0] = ct[0] ^ ord("R")
key[1] = ct[1] ^ ord("S")
key[2] = ct[2] ^ ord("X")
key[3] = ct[3] ^ ord("C")
key[4] = ct[4] ^ ord("{")
key[5] = ct[53] ^ ord("}")

for idx, c in enumerate(ct):
  print(chr(c^key[idx % len(key)]), end="")