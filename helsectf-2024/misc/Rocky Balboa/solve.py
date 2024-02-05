import bcrypt

the_hash = "$2b$14$WpeU3BB4A1FpeOoTRa100O3/a5RSzhnvFJyxOEZ3v2z4It/gM71Eu"


with open("rockyou_space.txt", encoding='utf-8', errors='replace') as f:
    wordlist = f.read().splitlines()

for pwd in wordlist:
    pwd = pwd.strip()
    if pwd.count(" ") < 4:
        continue

    print(f"Testing PW: {pwd}")

    if bcrypt.checkpw(pwd.encode('utf-8'), the_hash.encode('utf-8')):
        print(f"Bingo: {pwd}")
        break
else:
    print("# Fail")
