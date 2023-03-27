
import time
def hash(s):        
    return s + (s&128)**999999

start = time.time() * 1000
hash(0x00)
end = time.time() * 1000 - start

print(end)