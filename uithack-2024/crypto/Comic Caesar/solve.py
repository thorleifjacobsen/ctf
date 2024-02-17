def decrypt(text):
    flag_dec = ""
    for idx, char in enumerate(text):
        if char in alphabet:
            if idx % 2 == 0:
                flag_dec += alphabet[(alphabet.index(char)-3) % len(alphabet)]
            else:
                flag_dec += alphabet[(alphabet.index(char)+3) % len(alphabet)]
        else:
            flag_dec += char
    return flag_dec

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("flag.txt.enc", "r") as f:
    flag = f.read().strip()

dec_flag = decrypt(flag)
with open("flag.txt", "w") as f:
    f.write(dec_flag)