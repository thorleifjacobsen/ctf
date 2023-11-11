"""TEMMELIG HEMMELIG"""
"""Sør-Polar Sikkerhetstjeneste"""
"""Høyeksplosivt script for tilintetgjørelse av Julenissens slede"""

otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15]

def explode(input, antall):
    størrelse = len(input) // antall
    fragmenter = []
    
    for i in range(0, len(input), størrelse):
        fragment = input[i:i+størrelse]
        fragmenter.append(fragment)
    
    return fragmenter

with open("slede.txt", "r") as file:
    slede = file.read()

bang = explode(slede, 24)
eksplosjon = [''.join([chr(ord(c) + 2) for c in fragment]) for fragment in bang]
pinneved = [str(eksplosjon[i]) for i in reversed(otp)]

print(pinneved[0])
with open("pinneved2.txt", "w") as file:
    file.write(''.join(pinneved))