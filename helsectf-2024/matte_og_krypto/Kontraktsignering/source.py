from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
from flag import flag

contract = b"Dette er en superviktig kontrakt for veeldig viktige ting med store ord og uforstaaelige kruseduller."

# Standard RSA nøkkelgenerering
p = getPrime(1024)
q = getPrime(1024)
N = p*q
e = 0x10001
d = inverse(e, (p-1)*(q-1))

# Standard RSA signering/verifikasjon: https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Signing_messages
def sign(m):    
    return pow(m, d, N)

def verify(m,s):
    s = bytes_to_long(s)
    m = bytes_to_long(m)
    return sign(m) == s

print("Signaturtjenesten 2OpphøydIe signerer alle dine meldinger, bortsett fra den superviktige kontrakten:\n")
print(contract.decode())
print(f"\nN={N}")
while True:
    try:
        command = input("> ")
        if command == "sign":
            m = bytes.fromhex(input("message="))        
            if m == contract:
                quit("haha, du tru kanskje at æ e så lettlurt?? ånei du, du får itj signert den meldinga der nei!")

            print("derre va itj kontrakten, så da ska du få en signatur:")
            print("sign=", long_to_bytes(sign(bytes_to_long(m))).hex())
        elif command == "verify":
            s = bytes.fromhex(input("signature="))
            if verify(contract,s): 
                print("ja, herre e riktig signatur ja, no va du flink!")
                print("flag=", flag)
                exit(0)
            print("haha, derre va feil ja! du må hjem å øv dæ!")
        else:
            print("du kan bare bruke 'sign' eller 'verify'")
    except Exception as e:
        quit("error")
