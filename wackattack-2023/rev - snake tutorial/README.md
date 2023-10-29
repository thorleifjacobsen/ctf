# Snake Tutorial (easy)

If you don't already know parselmouth, you better learn it quick.

Author: krloer

📎 [snake_tutorial_handout.tar.gz](snake_tutorial_handout.tar.gz)

# Writeup

This is usually a hard task as it uses random numbers to encrypt the secret. But they also seed the random number generator with `1337` which will make it generate the same numbers.

So I just started reversing the snake_tutorial.py script and made it `undo_stuff`:

```python
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
```

This ended up printing the flag!

# Flag

```
wack{S5Ssss5SSsss5sSS5SSss55ssSSssSSSS55SSsssS55}
```