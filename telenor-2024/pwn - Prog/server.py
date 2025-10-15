#!/usr/bin/env python
from calendar import c
import random

from six.moves import input


def server():
    print("Hello stranger!")
    secret = random.randint(1, 1000)
    while True:
        try:
            guess = input("What's the random number?")
            if int(guess) == secret:
                f = open("./flag.txt", "r")
                print("You got it!\n" + f.read() + "\n")
                exit()
            else:
                print("No.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    server()
