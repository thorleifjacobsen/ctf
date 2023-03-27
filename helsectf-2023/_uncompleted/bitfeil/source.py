import random
import radio

flag = open("flag.txt","rb").read().strip()
hopp = 2**6 - 1

def p(a,b):
    return str("".join([a[i] for i in b]).count("1")%2)

def f(b):
    return p(b,[0,1,3]) + p(b,[0,2,3]) + b[0] + p(b,[1,2,3]) + b[1:]
  
def forbedre_bits(data):
    assert len(data)%2 == 0    
    bits = "".join([bin(tegn-hopp)[2:].rjust(6,"0") for tegn in data])    
    immune_bits = ""
    assert not "b" in bits
    for i in range(0, len(bits), 4):
        immune_bits += f(bits[i:i+4])
    assert len(immune_bits)%7 == 0
    return immune_bits

def print_bits(bits):
    bits = "".join([bits[i+2] + bits[i+4:i+7] for i in range(0, len(bits), 7)])
    melding = [int(bits[i:i+6],2)+hopp for i in range(0, len(bits), 6)]    
    return bytes(melding).decode()


bits = forbedre_bits(flag)
bits = list(map(int,bits))
bits = radio.overf0r_bits(bits,bitfeilrate=75) # simulerer en radio med høy en-bits feilrate (75%) for hvert 7ende bit.
print("bits=", bits)
print("melding=", print_bits(bits))