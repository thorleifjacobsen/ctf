# reisetid

skolematte
Kari og Ola bor 150km fra hverandre og skal møtes for å ta en kaffe. Kari kjører kl 1200, og ville brukt 3 timer om hun måtte kjøre hele lengden på 150km. Ola kjører kl 1300, og ville brukt 5 timer om han måtte kjøre hele lengden på 150km.

Hva er klokka når de møtes, og hvor langt i meter har Kari kjørt?

Flaggformat: `helsectf{<tid 4tall>_<lengde i meter>}`

Som eksempel, hvis de møtes kl 1201 og Kari har kjørt 11km så vil svaret være "1201_11000". Merk at dette bare var et eksempel for å vise deg hvordan du leverer når du har riktig svar.

# Writeup

Kari is driving in 50km/t (150km/3h)
Ola is driving in 30km/t (150km/5h)

Kari has 1 hour headstart and is at 50km when Ola starts. Leaving 100km of road between them when Ola starts.

The last 100km they are driving a speed of total 80km/t. 
They meet after 100km/80km/t = 1.25 hours * 60 minutes = 75 minutes after Ola starts driving.

So meeting time is: 13:00 + 75 minutes = 1415

Kari is driving 50km/t * 1.25 hours = 62.5km of the last 100km.
Kari has driven a total of 50km + 62.5km = 112.5km.

# Flag

```
helsectf{1415_112500}
```