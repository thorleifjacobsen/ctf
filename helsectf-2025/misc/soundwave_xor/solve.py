with open('intro.raw','rb') as f1, open('outro.raw','rb') as f2, open('xor.raw','wb') as out:
    while True:
        data1 = f1.read(1024)
        data2 = f2.read(1024)
        if not data1 or not data2:
            break
        out.write(bytes(a ^ b for a, b in zip(data1, data2)))
