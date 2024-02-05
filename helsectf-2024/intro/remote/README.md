# remote

I løpet av CTFen er det flere oppgaver som er hostet på en remote server og det krever at du kobler til en "rå" TCP port som går over SSL.

For å koble til hosted challenges har CTFd har dokumentasjon på dette: https://docs.ctfd.io/tutorials/challenges/connecting-to-challenges

Du kan velge å bruke snicat: https://github.com/CTFd/snicat for CLI eller tunnelering/proxy:

```
sc helsectf2024-2da207d37b091b1b4dff-remote.chals.io
```

Hvis du skal programmere en løsning er python og pwntools et godt valg. Først må du installere pwntools med f.eks. "pip install pwntools" så kan du kjøre følgende python script:

```python
from pwn import *
io = remote("helsectf2024-2da207d37b091b1b4dff-remote.chals.io", 443, ssl=True)
io.interactive()
```

eller, browse til `https://helsectf2024-2da207d37b091b1b4dff-remote.chals.io/`

# Writeup

I used the browse method and got the flag.

# Flag

```
helsectf{remote_flag_er_best,_ingen_protest!} 
```
