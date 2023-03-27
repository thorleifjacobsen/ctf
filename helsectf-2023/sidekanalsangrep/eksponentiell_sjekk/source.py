import string
from flag import FLAG

alfabet = list((string.ascii_letters + string.digits + string.punctuation).encode())
assert all(ch in alfabet for ch in FLAG) == True
assert len(FLAG) > 50
assert len(FLAG) < 100

def hash(s):        
    return s + (s&128)**999999

def strcmp(s1,s2):
    if len(s1) != len(s2):        
        return False
    for i in range(len(s1)):
        if hash(s1[i]^s2[i]) != 0:
            return False
    return True

def Challenge():
    print(f"""I den andre oppgaven om sidekanalsangrep er selve sårbarheten mer kamuflert.

Det eneste du kan gjøre er å sjekke om du vet hele flagget, eller ikke.
    """)    
    while True:        
        flag = input(f"Hva er flagget? ")
        try:
            flag = bytes.fromhex(flag)
        except:
            print("Forventet input er hexadecimal, f.eks.: ffff")
            continue

        if strcmp(FLAG,flag) == True:
            print("Gratulerer, oppgaven er løst. Du vet allerede flagget! :)")
        else:
            print("Nei, det er ikke riktig flagg :(")
        print()

if __name__ == "__main__":
    c = Challenge()