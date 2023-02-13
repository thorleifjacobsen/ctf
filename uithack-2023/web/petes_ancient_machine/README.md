# Pete's Ancient machine

Pete has an ancient machine stored in his parents basement which both his parents have neglected over time. The password is known and is a 5 digit code (2, 4, 6, 8, 10). Pete, however, is having trouble getting on > to the machine and has found that the password resets after a short time. Find a way to enter the 5 digit > code as fast as possible.

The flag will be the same format as this one: UiTHack23{this_could_be_a_key}.

Make GET request

motherload.td.org.uit.no:8012

# Writeup

I made a script to send the curl requests like this first:

```bash
curl motherload.td.org.uit.no:8012/?digit=2
curl motherload.td.org.uit.no:8012/?digit=4
curl motherload.td.org.uit.no:8012/?digit=6
curl motherload.td.org.uit.no:8012/?digit=8
curl motherload.td.org.uit.no:8012/?digit=10
```

Somehow 2-3 attempts nothing. So I thought I might wait for a correct response so I made a python script which did that.

```python
import requests

url = "http://motherload.td.org.uit.no:8012"

response = requests.get(f"{url}?digit=2")
while "STARTING, HURRY!" not in response.text:
    response = requests.get(url)

for digit in [4, 6, 8, 10]:
    res = requests.get(f"{url}?digit={digit}")
    print(f"Response for digit {digit}: {response.text.strip()}")
```

This only gave me: 

```bash
Response for digit 4: STARTING, HURRY!
Response for digit 6: STARTING, HURRY!
Response for digit 8: STARTING, HURRY!
Response for digit 10: STARTING, HURRY!
```

A few days later I was "complaining" about me sucking and I pasted this code to the discord. And there I see why it always says `STARTING, HURRY!`. I did not use the correct variable for the print statement. I used `response` but I should have used `res`. So the new (script.py)[script.py] works perfect. The first idea also worked just had to try a bit more. But my script.py is more fun.


```bash
└─$ time python3 script.py
Response for digit 4: HURRY
Response for digit 6: HURRY
Response for digit 8: HURRY
Response for digit 10: {
  "key": "UiTHack23{that-was-really-fast-god-damn}"
}

real    0.57s
user    0.13s
sys     0.04s
cpu     30%
```