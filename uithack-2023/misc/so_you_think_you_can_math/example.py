from pwn import *

p = remote("motherload.td.org.uit.no", 8010)
p.recvuntil(b"Ready?")
p.sendline(b"Yup")
p.recvline()

while True:
    question = p.recvline().strip().decode()
    if not question:
        break

    print(question)

    try:
        question = question.split(": ")[-1]
        answer = str(int(eval(question))).encode()
        print(f"Answer is: {answer}")
        p.sendline(answer)
    except:
        break
