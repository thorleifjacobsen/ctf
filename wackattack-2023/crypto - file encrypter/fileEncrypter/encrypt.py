from secrets import key

assert len(key) == 8
for i in key:
    assert i <= 255 and i >= 0

with open("Chip.png", "rb") as file:
    data = list(file.read())

out = []

for i, val in enumerate(data):
    out.append(val ^ key[i % len(key)])

with open("encrypted", "wb") as outfile:
    outfile.write(bytes(out))
