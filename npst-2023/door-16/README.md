# Invasjon

Gjennom temmelig hemmelige innhentingsmetoder har vi fått tak i det vedlagte dokumentet som avslører den egentlige hensikten bak løsepengeangrepet: Sydpolare aktører planlegger å invadere Nordpolen for å stoppe julen én gang for alle!

I dokumentet nevnes det at aktørene har plantet deep-cover agenter i blant oss, og at de har hemmelige koder for å etablere kontakt med disse. Analyser materialet og se om du klarer å avsløre de hemmelige kodene slik at vi kan få disse agentene på kroken!

I mellomtiden iverksetter vi umiddelbare mottiltak for å stanse invasjonen.

- Tastefinger

[📎aksjon_2023.zip](./aksjon_2023.zip)

# Writeup

Unzip shows that there is a .git folder aswell:

```bash
unzip aksjon_2023.zip 
Archive:  aksjon_2023.zip
   creating: aksjon_2023/
   creating: aksjon_2023/.git/
   <many git files>
  inflating: aksjon_2023/plan.md    
```

`plan.md` shows nothing but there are more branches available with:

```bash
└─$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/Rettelser
  remotes/origin/Risikoanalyse
  remotes/origin/Tidsplan
  remotes/origin/fase2
  remotes/origin/ikke-merge-før-julaften
  remotes/origin/master
  remotes/origin/teknisk
  remotes/origin/teknisk-fase-1
```

Checking out the `not to be merged before christmas eve` there is a new file `feltagenter_kontaktmanual.md` which has the placeholder codes for the agents.

```
# Eksfil av feltagenter

Våre deep-cover feltagenter har blitt instruert i å respondere på følgende koder.

Bruk disse for å initiere kontakt ved eksfil etter vellykket operasjon, eller ved ekstraordinært behov ellers.

## Koder

- Agent "Julie Bånd": KODE_PLACEHOLDER_1
- Agent "Solid Sankt": KODE_PLACEHOLDER_2
- Agent "Jollyson Bål": KODE_PLACEHOLDER_3
```

Now I just need to figure out when they are added. `git log --all -- feltagenter_kontaktmanual.md` shows that this is the only place it exists. `git grep "ode" $(git rev-list --all)` shows only this file with the word `Kode`. So no commits. Then I try to merge it and the placeholder code is replaces with something new. It has been self destructed. Maybe because it is not christmas? 

How can this happen when this is not in the code? Well, pre-merge commit hooks. So in the file `.git/hooks/pre-merge-commit` I found this:

```bash
#!/usr/bin/env bash

FIL="feltagenter_kontaktmanual.md"

if test -e "$FIL"; then
    sed -i "s/$(echo S09ERV9QTEFDRUhPTERFUl8x | base64 -d)/$(echo VW5uc2t5bGQsIHZldCBkdSB2ZWllbiB0aWwgYmlibGlvdGVrZXQ/IDxSRVNQT05TPi4gU2EgamVnIGJpYmxpb3Rla2V0PyBKZWcgbWVudGUgZmlza2Vmb3JoYW5kbGVyZW4sIGthbiBkdSB2YWdnZSBib3J0IG1lZCBtZWc/ | base64 -d)/" "$FIL"
    sed -i "s/$(echo S09ERV9QTEFDRUhPTERFUl8y | base64 -d)/$(echo SWtrZSBnb2QganVsLg== | base64 -d)/" "$FIL"
    sed -i "s/$(echo S09ERV9QTEFDRUhPTERFUl8z | base64 -d)/$(echo S1JJUE9Te0ZsYWdnIGkgYWxsZSBrcmlrZXIgb2cga3Jva2VyfQ== | base64 -d)/" "$FIL"
    echo "S29kZXIgaGFyIGJsaXR0IHNrcmV2ZXQK" | base64 -d

    if [ -z "$DISABLE_SELF_DESTRUCT" ]; then
        sed -i "s/\(: \)[^\n]*/\1$(echo PEtPREVOIEhBUiBTRUxWREVTVFJVRVJUPg== | base64 -d)/" "$FIL"
        echo "S29kZXIgaGFyIHNlbHZkZXN0cnVlcnQK" | base64 -d
    fi
fi
```

Manually running the echo's I found the last had the flag

```bash
$ echo S1JJUE9Te0ZsYWdnIGkgYWxsZSBrcmlrZXIgb2cga3Jva2VyfQ== | base64 -d
KRIPOS{Flagg i alle kriker og kroker}             
```

