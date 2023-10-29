from random import seed, randint

def do_stuff(flag):
    seed(1337)
    s = []
    for i, c in enumerate(flag):
        s.append(str(ord(c)^(i**2 & 20)))

    s1 = [str(int(a,16)) for a in s]

    for i in range(len(s1)):
        s1[i] = s1[i] + chr(randint(0x30,0x39)) * randint(0,5)

    res = ",".join(s1)

    return res

if __name__ == "__main__":
    with open("flag.txt", "r") as f:
        flag = f.readline() 
    out = do_stuff(flag)
    with open("output.txt", "w") as f:
        flag = f.write(out) 
    