from random import seed, randint

def undo_stuff(flag):
    seed(1337)
    s = flag.split(",")

    # Revert the random adding thingy, janky but works
    for i, c in enumerate(s):
        random = len(chr(randint(0x30,0x39)) * randint(0,5)) * -1
        if random < 0:
            s[i] = c[:random]

    # Revert the converting to hex thingy
    s1 = [hex(int(a))[2:] for a in s]

    # Revert the xor thingy
    s2 = []
    for i, c in enumerate(s1):
        s2.append(chr(int(c)^(i**2 & 20)))

    print("".join(s2))

if __name__ == "__main__":
    with open("output.txt", "r") as f:
        flag = f.readline() 
    undo_stuff(flag)
    