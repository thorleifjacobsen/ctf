import cv2
import os
from pyzbar.pyzbar import decode

os.chdir("./smarte_kontrakter")
backwards = "git checkout HEAD~ >/dev/null 2>&1"
start = "git checkout main >/dev/null 2>&1"

res=os.system(start) # Goto start

while (res == 0):

    try:
        img = cv2.imread('qrcode.png')
        decoded = decode(img)
        print(decoded[0].data.decode())
    except: 
        pass
    res=os.system(backwards) # Go backwards in git history

os.system(start)