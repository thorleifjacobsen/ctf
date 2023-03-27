# git huskelapp (493)

pAAskeharen har vært litt uheldig etter at han hadde vært på teater. Han har overskrevet qrkoden som inneholdt noe viktig han måtte huske på!

# Writeup

Saw quickly the other repo from pAAskeharen which was named (smarte_kontrakter)[https://github.com/pAAskeharen/smarte_kontrakter]. Here was a QR code named `Huskelapp:` and around 200 commits. So randomly opening a commit shows the QR code changes. So I had to do this manually or just make a program. Using `pyzbar` it went really fast.

My script had to start from the last commit and go backwards so I ended up with (solve.py)[solve.py].

```python
import cv2
import os
from pyzbar.pyzbar import decode

os.chdir("./smarte_kontrakter")
backwards = "git checkout HEAD~ >/dev/null 2>&1"
start = "git checkout main >/dev/null 2>&1"

res=os.system(start) # Goto start

while (res == 0):

    img = cv2.imread('qrcode.png')
    decoded = decode(img)
    print(decoded[0].data.decode())

    res=os.system(backwards) # Go backwards in git history
```

Then we quickly found one of the commits with the following data:

```
Jeg har lekt med blokkjeder.
For å lære har jeg kun holdt meg til et ETH testnett.
Haaper jeg ikke har gjort noen feil!

etherum:0xb53449a6cd4D55bD09fD3f4509307139c354cc18
```

Guessing I need to remember this for a later task.

# Flag

```
helsectf{g1t_bEhOlD3r_h1sTor1KkeN!}
```