import os

def run_code(code):    
    print("------------\n", code.decode("ascii"), "\n------------\nresult:", sep="", end=" ")
    open("mycode.go","wb").write(code)
    os.system("go run mycode.go 2>/dev/null || echo 'there be errors'")    

code = open("sourcecode.go","rb").read()
print("Mitt Go program kompilerer fint, men viser ikke flagget? Jeg som trodde Go aldri kunne gjøre noe feil!?\n")
run_code(code)

offset = input("\noffset (decimal)?> ")
byte = input("byte (hex)?> ")
try:
    offset = int(offset)
    byte = bytes.fromhex(byte)

    code = list(code)
    code[offset] = int.from_bytes(byte, "big")        
    code = bytes(code)

    run_code(code)
except Exception as e:
    quit("error")