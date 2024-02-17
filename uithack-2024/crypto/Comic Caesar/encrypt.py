def encrypt(text):
    flag_enc = ""
    for idx, char in enumerate(text):
        if char in alphabet:
            if idx % 2 == 0:
                flag_enc += alphabet[(alphabet.index(char)+3) % len(alphabet)]
            else:
                flag_enc += alphabet[(alphabet.index(char)-3) % len(alphabet)]
        else:
            flag_enc += char
    return flag_enc

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("flag.txt", "r") as f:
    flag = f.read().strip()

enc_flag = encrypt(flag)
with open("flag.txt.enc", "w") as f:
    f.write(enc_flag)