# feil_domene_1 (488)

Her er en webserver, men du må vite riktig domene for å få ut noe vettugt:

https://161.35.192.95/

# Writeup

Running `curl -v --insecure https://161.35.192.95/` shows that the certs are for `seretdomain-88a.helsectf.no`

```
* Server certificate:
*  subject: C=NO; ST=Some-State; O=Påskeharen; OU=Sikkerhetsavdelingen; CN=seretdomain-88a.helsectf.no
*  start date: Mar  9 20:04:01 2023 GMT
*  expire date: Mar  8 20:04:01 2024 GMT
*  issuer: C=NO; ST=Some-State; O=Påskeharen; OU=Sikkerhetsavdelingen; CN=seretdomain-88a.helsectf.no
*  SSL certificate verify result: self-signed certificate (18), continuing anyway.
```

Using curl's `--resolve` I can open the IP address as any domain I want so using that domain:

```bash
$ curl --insecure --resolve seretdomain-88a.helsectf.no:443:161.35.192.95 https://seretdomain-88a.helsectf.no
helsectf{paaskemorgenslukkersorgen}
```

Could also use `Host` header:

```
$ curl https://161.35.192.95/ --insecure -H 'Host: seretdomain-88a.helsectf.no'
helsectf{paaskemorgenslukkersorgen}
```


# Flag

```
helsectf{paaskemorgenslukkersorgen}
```