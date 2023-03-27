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

# This is the CT we're given
ct = 91288880675628035011093545005790682206962326526026631772248877471574034941238763064368507363758616986

# Skip the first we do not know what this key is.
# As the key is based on the last 3 bytes of the flag which we do not have yet.
ct >>= 21

# We know the key for the next 3 bytes are `hel` as the flag starts with that.
keyPlaintext = b"hel"

# We build our flag starting with the 3 known one.
flag = keyPlaintext.decode()

while ct > 0:

    # Extract 21 bits 
    tre = ct & 0b111111111111111111111 # 21 bits
    # Remove the 21 bits we extracted from the CT
    ct >>= 21

    # So we use scrambled keyPlaintext XOR'ed with the 21 bits we extracted to get the value
    key = tre^scramble(keyPlaintext)

    # I split the 12 bits into 3 bytes and convert them to ascii
    keyPlaintext = chr(key >> 14 & 127) + chr(key >> 7 & 127) + chr(key & 127)
    
    # Add those to the flag
    flag += keyP

    # I convert the 3 characters to bytes just to make our life simpler. 
    keyPlaintext = keyPlaintext.encode()

    # Then we can restart the loop

# Lastly print the whole flag
print(flag)