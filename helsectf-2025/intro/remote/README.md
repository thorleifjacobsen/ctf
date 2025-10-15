# remote

I løpet av CTFen er det flere oppgaver som er hostet på en remote server og det krever at du kobler til en "rå" TCP port som går over SSL.

For å koble til hosted challenges har CTFd har dokumentasjon på dette: https://docs.ctfd.io/tutorials/challenges/connecting-to-challenges

Du kan velge å bruke snicat: https://github.com/CTFd/snicat for CLI eller tunnelering/proxy:
```
sc helsectf2025-42694257c6fdb3976dd6-remote.chals.io
```

Om du er 1337-uber-hacker og har hørt om Nix så kan du fyre det direkte, uten å installere noe;
```
nix-shell -p "snicat" --command "sc helsectf2025-42694257c6fdb3976dd6-remote.chals.io"
```

Hvis du skal programmere en løsning er python og pwntools et godt valg. Først må du installere pwntools med f.eks. `pip install pwntools`. I senere tid med python kan det hende du ikke får lov til å installere pip pakker globalt, google it!

Du kan teste pwntools og hente et flag ved å kjøre dette i REPL;

[🔗 https://helsectf2025-42694257c6fdb3976dd6-remote.chals.io/](https://helsectf2025-42694257c6fdb3976dd6-remote.chals.io/)

# Writeup

<Enter writeup here>

# Flag

```
flag{goes_here}
```