import string,random
import enchant

letters = [i for i in "abcdefghijklmnopqrstuvwxyz"]
d = enchant.Dict("en_US")
cipher = "w😇a😲 😲😇a😲"

for x in letters:
    for y in letters:
        line = cipher.replace("😇", x).replace("😲", y)
        if d.check(line.split(" ")[0]): # Check first word
            if d.check(line.split(" ")[1]): # Check last word
                print(line) # Legal combo! Print!