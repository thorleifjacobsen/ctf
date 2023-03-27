# remote (477)

I løpet av CTFen er det flere oppgaver som er hostet på en remote server og det krever at du kobler til en "rå" TCP port som går over SSL.

For å koble til hosted challenges har CTFd har dokumentasjon på dette: https://docs.ctfd.io/tutorials/challenges/connecting-to-challenges

Du kan velge å bruke snicat: https://github.com/CTFd/snicat for CLI eller tunnelering/proxy:

`sc helsectf2023-6ac4e1c6d8855c1bd96a-remote.chals.io`

Hvis du skal programmere en løsning er python og pwntools et godt valg. Først må du installere pwntools med f.eks. "pip install pwntools" så kan du kjøre følgende python script:

```python
from pwn import *
io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-remote.chals.io", 443, ssl=True)  
print(io.recvline().decode())  
```

# Writeup

Downloaded snicat as described and ran the sc command described which gave the flag.

```
$ ./sc helsectf2023-6ac4e1c6d8855c1bd96a-remote.chals.io  
(connected to helsectf2023-6ac4e1c6d8855c1bd96a-remote.chals.io:443 and reading from stdin)
Her har du et flagg: helsectf{remote_flag_killer} 
```

# Flag

```
helsectf{remote_flag_killer} 
```