# 2.05_anvilnotes_source

Logget inn som brukeren "oper" siden han også har samme passord som admin, ser ut som denne brukern har backup av client og server på botnettet dems som notat. Inni dem lå flagget for denne 

```
Kategori: 2. Oppdrag
Oppgave:  2.05_anvilnotes_source
Svar:     959b0eef26acb7d007100026ac83ab60
Poeng:    10

Dette så interessant ut!
En samarbeidende tjeneste i Pseudova vurderer at dette meget sannsynlig er kildekoden for skadevaren benyttet i angrepene mot kraftverket deres.
```

Så for å dekode base64 strengen ser jeg det så ut som det ble noe binært. Dekodet det til en fil med `base64 -d client.txt > client` og kjørte "file" på den.

```
┌──(toffe㉿GamingPC)-[~/Projects/cybertalent/botnet]
└─$ file client 
client: gzip compressed data, from Unix, original size modulo 2^32 20480
```

Prøvde litt google og så at `.tgz` filending fungerte så `tar -zxvf client.tgz` og der har jeg kildekoden til clienten. Gjør det samme med server og sitter med all intel.