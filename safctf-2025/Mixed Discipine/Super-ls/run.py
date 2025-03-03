from ctypes import CDLL
from base64 import b64encode
libc = CDLL("libc.so.6")

for _ in range(1337): y = str(libc.rand())
r = b64encode("".join([chr(int(y[i:i + 2])) for i in range(0, len(y), 2)]).encode()).decode().replace("=", "")
print(r)