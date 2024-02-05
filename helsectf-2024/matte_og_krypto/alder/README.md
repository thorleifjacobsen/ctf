# alder

Kari og Ola er to gamle vampyrer.

I dag er Kari 3133713 år eldre enn Ola. Om 5 år vil Kari være 4 ganger eldre enn Ola. Hvor gammel er Kari og Ola i dag?

Flaggformat: `helsectf{<alder kari>_<alder ola>}`

Som eksempel, hvis Kari er 1 år og Ola er 3 år så ville svaret vært helsectf{1_3}. Merk at dette bare var et eksempel for å vise deg hvordan du leverer når du har riktig svar.

# Writeup

Here I just had to go slow and end up with the numbers. I started by writing down the equations.

```
# Kari is 3133713 years older than Ola
Kari = Ola + 3133713

# In 5 years kari is 4 times older than Ola.
(Kari + 5) = 4 * (Ola + 5)

# Solve Ola:
(Ola + 3133713 + 5) = 4 * (Ola + 5)
Ola + 3133718 = 4 * Ola + 20
3133718 = 3 * Ola + 20
3133698 = 3 * Ola

Ola = 3133698 / 3
Ola = 1044566

Kari = Ola + 3133713
Kari = 1044566 + 3133713
Kari = 4178279
```

Then I had the flag.

# Flag

```
helsectf{4178279_1044566}
```