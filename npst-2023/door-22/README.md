# Gaveliste-endring

Hei Toffe,

JULESOC har fått en alarm fra informasjonssystemet tilknyttet NISSENS gavelager på VALøya i Tromsø. Alarmen handlet om en uautorisert modifikasjon i databasen som styrer inventaret til lageret, og JULESOC har sendt oss databasefilene slik de forekom på tidspunktet alarmen gikk.

Har du mulighet til å sjekke ut filene og finne ut hvilken rad som er blitt modifisert?

[📎 ALARM_JULESOC.zip](./ALARM_JULESOC.zip)

Returner UUID til den modifiserte raden, f.eks. PST{6eab374e-735f-416e-bcc6-81b4b8dfc7a9}

# Writeup

The zip file contains 3 files `inventory.db`, `inventory.db-shm` and `inventory.db-wal`. These points to sqlite3 so I start by invenstigating the `.db` file with that. Since they want us to figure ut which rows has been changed the `WAL` (Write-Ahead Logging mode) file will be of great help. As I understand this file contains changes not yet commited to the DB. So just see the difference in the DB after and before the WAL file by doing this:

```bash
unzip ALARM_JULESOC.zip
mv inventory.db-wal inventory.db-wal2
sqlite3 inventory.db .dump > dump1.txt
mv inventory.db-wal2 inventory.db-wal
sqlite3 inventory.db .dump > dump2.txt
diff dump1.txt dump2.txt
```

That returns

```bash
42072c42072
< INSERT INTO gifts VALUES('9da1b2a6-5a52-41ec-8bf0-32381e054db7','Nano Jade Mindflex',48564);
---
> INSERT INTO gifts VALUES('9da1b2a6-5a52-41ec-8bf0-32381e054db7','Nano Jade Mindflex',0);
```

So they changed the number of Mindflex from `48564` to `0`.

# Flag

```
PST{9da1b2a6-5a52-41ec-8bf0-32381e054db7}
```