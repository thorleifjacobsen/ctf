flag="gemredsf|k3oFe`r1E2n`e02j_qqoh`MNdR8d_j^Fpqts`n`80~"

for i in range(len(flag)):
    letter=ord(flag[i])
    letterTransformed = letter - (i + (((i ^ i >> 0x1f) * 0x55555556 >> 0x20) ^ (i >> 0x1f)) * -3 + -1)

    print(chr(letterTransformed), end="")