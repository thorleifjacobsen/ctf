
#einoprst"/()

#for test in open("./rosetorn"): print(test)


#print(it in open("./rosetorn"))


#curl "https://helsectf2023-6ac4e1c6d8855c1bd96a-tornerose.chals.io/?program=print(open(\"/rosetorn\"))"

# int
# str
# print
# open
# set


def valid(s):
    for ch in s:
        if ch not in 'einoprst"/()': return False
    return True

for b in dir(__builtins__):
    if valid(b): print(b)


print(repr(open("./rosetorn")))
