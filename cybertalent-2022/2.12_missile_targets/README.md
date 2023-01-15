# 2.12_missile_targets

Inn på aurum siden dette er 2.11 så regner jeg med vi går videre derfra. Ser ut som `.bash_history` ikke ble clearet.

```
ls -lah
which signer
signer --help
echo "Testing testing" > test.txt && signer --file-name test.txt --key-file privkey.pem --rng-source urandom
rm test.txt
konekt
signer --file-name missile.1.3.37.fw --key-file privkey.pem --rng-source urandom
mv missile.1.3.37.fw_signed missile.1.3.37.fw
konekt
rm privkey.pem missile.1.3.37.fw
```

`signer` er en binary som vi sikkert skal dekompilere og `konekt` virker til å være kontrollsystemet til missilene. Her kan jeg laste ned firmwaren som det ser ut som de har modifisert. Browser missiler og finner flagg for 2.12

```
Kategori: 2. Oppdrag
Oppgave:  2.12_missile_targets
Svar:     bc23d07612ac5bb9aa1b0a4e612ff275
Poeng:    3

Bra jobba! Dette må være kontrollsystemet til missilene. Målparametrene er allerde lagt inn og sikter på mange vestlige byer!
Dette er viktig informasjon som vi har levert videre til våre oppdragsgivere. Analytikerene våre har plottet målene for deg, sjekk oppdragsmappen.
Som du forstår er det ekstremt viktig å forhindre dette!

Ny fil: /home/login/2_oppdrag/worst_case_scenario.jpg
```