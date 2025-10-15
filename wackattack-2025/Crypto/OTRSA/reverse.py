e = 65537
plaintext = []

with open("OTRSA/handout.txt") as f:
    for line in f:
        c, e_str, n = map(int, line.split())
        # Try all possible byte values (0–255)
        for m in range(256):
            if pow(m, e, n) == c:
                plaintext.append(m)
                break

print(bytes(plaintext))