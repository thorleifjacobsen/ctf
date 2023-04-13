import b64decode from base64

jx = open("flagg.bin", "rb").read()
jx_decoded = b64decode(jx).decode().split("123456789")
p1 = int(jx_decoded[0])
p2 = int(jx_decoded[1])
p3 = int(jx_decoded[2])

p3_solved = "".join([chr(int(c)) for c in str(p1 ^ p3).rsplit("000")])
x = int("000".join([str(ord(c) << 2) for c in p3_solved]))
p2_solved = "".join([chr(int(c)) for c in str(p2^x).rsplit("000")])
p1_solved = "".join([chr(int(c)) for c in str(p1 ^ (p3 ^ p1) ).rsplit("000")])

print(p1_solved + p2_solved + p3_solved)
