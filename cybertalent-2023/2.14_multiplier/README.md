
# 2.14_multiplier

Denne slet jeg med, jeg tok 2.13 og fra der klarte jeg å få 2.15. Ifølge 2.15 hinter den om at vi må løse signatursjekken. Så `signer` virket som å være en logisk 2.16.

I 2.13 hinter den om: `Herlig! Vi har nå lov til å kjøre programmer. Kan du bruke dette til noe?` så dette får meg til å tenke at 2.14 krever at vi kjører assembly på samme måte som 2.15. Med det brukes utallige timer på å generere forskjellige assemblykoder.

I `fracture` ser vi at vi er chrootet så prøver å komme unnav dette:

```cpp
iVar1 = chdir("/domain/interface");
if ((((iVar1 == 0) && (iVar1 = chroot("/domain/interface"), iVar1 == 0)) &&
    (iVar1 = setregid(0xfffe,0xfffe), iVar1 == 0)) &&
    (iVar1 = setreuid(0xfffe,0xfffe), iVar1 == 0)) {
  _session = session_create("operator",0,iVar3);
  daemon(0,0);
  panic_handler_set(panic_handler_regdump);
  ui_menu(&mainmenu);
  session_printf(&DAT_001036e7);
  session_close();
}
```

Prøvde følgende ting basert på alt jeg fant på internett når jeg søkte:

1. Jailbreak, prøve å komme ut av chrooten
2. Path traversal. Fant flagget "findflag" leter etter: `FLAG.30b1e2298b0e4e6b192de61142476f9e` (Hashen er md5 av "unguessable")
3. RCE 
4. Stack dump
5. Privesc

Ender opp med å klare å bygge opp følgende struktur på mappen vi er chrootet i. 

```
.
├── programs
│   ├── findflag.prg
│   ├── telemetry.prg
│   └── uid.prg
├── firmware
│   ├── missile.1.3.37.fw
│   └── server-software.tar.xz
└── FLAG.30b1e2298b0e4e6b192de61142476f9e
```

Dette var tydligvis, HELT feil. Fikk et hint om at det handlet om `signer` i 2.14. Ble litt irritert at hintene motarbeider seg sånn. Men med nytt mot åpner jeg signer og får full panikk. Koden er jo et ræl. Å dekompilere dette til noe som har mening vil jo ta evig lang tid.

Sitter flere dager her også og kikker, og velger faktisk å spørre om et hint til. Og får følgende hint fra Vealending:

```
du kan jo bare teste om krypteringen til signer funker da
har du sett på hvordan signaturen er implementert mtp. ECDSA?
er bare å lese seg opp på hvordan signering med ECDSA fungerer, og vanlige svakheter
```

Må inrømme at jeg ikke klarte å se i signer hvordan signeringen fungerte. Var ganske låst på at det var inni signer en plass jeg skulle se. Googlet så `ECDS Vulnerabilities` og fant [denne](https://halborn.com/how-hackers-can-exploit-weak-ecdsa-signatures/) artikkelen. 

> If two signatures have the same value for R, then the private key can be calculated using the equation:

Er det tilfeldig at det lå en signert test.txt fil? Og missilen er signert?

Sammarbeidet mned Decoy som så fant [denne](https://billatnapier.medium.com/ecdsa-weakness-where-nonces-are-reused-2be63856a01a). Basert på dette prøvde vi rett og slett bare å se om dette fungerte.

Etter litt hadde jeg [recover_private_key.py](recover_private_key.py). Den tar inn to filer og finner nøkkelen. Og dette ga jo etter litt prøving og feiling resultater.

```
Private recovered:
114798114433974422739242357806023105894899569106244681546807278823326360043821
```

Og dette var flagget

```
Kategori: 2. Oppdrag
Oppgave:  2.14_multiplier
Svar:     114798114433974422739242357806023105894899569106244681546807278823326360043821
Poeng:    5

Dette ser ut til å være privatnøkkelen som de bruker i ECDSA-signeringen sin. Som det kjente ordtaket går -- "Never roll your own crypto". La oss håpe denne nøkkelen kan brukes til noe nyttig :)
```

Nå vet vi at 2.16 handler om å modifisere missile firmware filene og laste opp. Bare å finne utav hvordan! 