import struct  
FLAG = "helsectf".encode()
melding = ""
for f in FLAG:
    print(f)
    melding += struct.pack('<I', 0x1F900 + f + 77).decode("utf-32le")
print(melding)

# Reverse

melding = "🦵🦲🦹🧀🦲🦰🧁🦳🧈🦲🦺🥽🦷🥾🧀🦬🦯🦀🦴🧆🦛🦻🦲🦿🦬🦮🦮🦬🦯🦙🦶🦬🦼🦝🦽🦯🦿🦢🦸🧁🦬🦠🥽🦺🦬🦐🦡🦓🦬🦼🦽🦝🦴🦮🧃🦀🥮🧊".encode("utf-32le")
FLAG = ""
for i in range(0, len(melding), 4):
    chunk = melding[i:i+4]
    code_point = struct.unpack("<I", chunk)[0]
    original_code_point = code_point - 0x1F900 - 77
    FLAG += chr(original_code_point)
    
print(FLAG)


# FLAG = ""
# bytes_str = melding.encode("utf-32le")
# for i in range(0, len(bytes_str), 4):
#     chunk = bytes_str[i:i+4]
#     code_point = struct.unpack("<I", chunk)[0]
#     original_code_point = code_point - 0x1F900 - 77
#     FLAG += chr(original_code_point)
# print(FLAG)