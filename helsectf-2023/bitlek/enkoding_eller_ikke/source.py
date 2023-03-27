flag = open("flag.txt","rb").read().strip()
def encrypt3(flag):
    ciphertext= 0 
    for i in range(0, len(flag)):
        ciphertext |= ((flag[i]&127)^128) << (7*i)

    return ciphertext

print(encrypt3(flag))