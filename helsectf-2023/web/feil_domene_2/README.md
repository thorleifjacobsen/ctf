# feil_domene_2 (500)

Let's Encrypt utstedte en gang i 2020 et sertifikat til et subdomene av helsectf.no. Det viser seg at denne serveren fortsatt svarer på dette domenet.

https://161.35.192.95/

# Writeup

Used (subdomainfinder)[https://www.nmmapper.com/sys/tools/subdomainfinder/] which found the domains:

```
xn--pskentter-52a7s.helsectf.no
påskenøtter.helsectf.no
```

Used curl's `--resolve` to open that site with the hostname above:

```bash
$ curl --resolve xn--pskentter-52a7s.helsectf.no:443:161.35.192.95 https://xn--pskentter-52a7s.helsectf.no --insecure
<p>helsectf{paaskeharen_slukker_ogsaa_sorgen}</p>
```

Could also use `Host` header:

```
$ curl https://161.35.192.95/ --insecure -H 'Host: xn--pskentter-52a7s.helsectf.no'
<p>helsectf{paaskeharen_slukker_ogsaa_sorgen}</p>
```
# Flag

```
helsectf{paaskeharen_slukker_ogsaa_sorgen}
```