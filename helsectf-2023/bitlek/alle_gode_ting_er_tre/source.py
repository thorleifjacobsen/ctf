def to21bit(t):
    # 3byte blir gjort om til 21bit (fjerner MSB fra hver byte)    
    return ((t[0]&127)) << 14 | ((t[1]&127)) << 7 | ((t[2]&127))    

def from21bit(b):
    # ekspanderer 21bit tilbake til 3bytes (3x8bit) hvor MSB settes til 0 i hver byte
    return (((b>>14)&127)<<16) | (((b>>7)&127)<<8) | (b&127)

def scramble(data):
    # input bytes blir rotet sammen til et 21bits tall
    a = 0xcbf29ce484222325
    for byte in data:
        a = a ^ byte
        a = (a * 0x100000001b3) % 2**64        
    b = a&0x1fffff  
    c = (a>>21)&0x1fffff
    d = (a>>42)&0x1fffff
    return b^c^d # xor-folding for å få 21bits output

def encrypt4(flag):
    plaintexts = [flag[i:i+3] for i in range(0, len(flag), 3)]
    keys = [scramble(tre) for tre in plaintexts]
    keys = [keys[-1]] + keys[0:-1]
       
    ciphertext = 0
    for i,ct in enumerate([to21bit(pt)^key for pt,key in zip(plaintexts,keys)]):
        ciphertext |= (ct << (21*i))
    return ciphertext

flag = open("flag.txt","rb").read().strip()
assert len(flag)%3 == 0
ct = encrypt4(flag)
print("ct=", ct)
