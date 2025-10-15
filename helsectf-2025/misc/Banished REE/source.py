banned = """\nUC5#$;sg^o.`xI\\\x0b3wLMEn_GuA6jJl/yW'kd>+@\x0ct|N VmBr0K-9bOHSYZP?8v*41qRzh&eXFT\r7\tDiQ=p2"""

def challenge():
    print("Python REE (read-eval-exec)")
    _in = bytes.fromhex(input(">> ")[0:4096].strip()).decode()
    if not _in.isascii(): return("nah, we only deal in asciis")
    if any([x in banned for x in _in]): return("cheater")
    return exec(eval(_in))

if __name__ == "__main__":
    try:
        print(challenge())
    except:
        print("error")
