banned = """oZOx.':Ri*U9N\nAT3HjI0z>Bn4F`5;L}SkldPG$KYw?maE{7g+Mrv2s\\b_u&tVC-e=D\x0b@J^Q|h 1W\r#8p6!\x0cq][X\t/y"""

def challenge():
    print("Python REE (read-eval-exec)")
    _in = bytes.fromhex(input(">> ")[0:1024].strip()).decode()
    if not _in.isascii(): return("nah, we only deal in asciis")
    if any([x in banned for x in _in]): return("cheater")
    return exec(eval(_in))

if __name__ == "__main__":
    try:
        print(challenge())
    except:
        print("error")
