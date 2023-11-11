# Historisk mail-bommert

Å nei! Historikkeralven klarte ved et uhell å åpne opp en ondsinnet .pdf-fil på e-mailen sin, og diktet han var i ferd med å levere til Julenissen har blitt kryptert.

Heldigvis har hackerene som sendte PDF-filen klart vært uvarsomme nok til å ikke slette [nøkkelfilen](./input.txt), så cyberalvene tror de har mulighet til å dekryptere [diktet](cypher.txt). De er litt usikkre på nøyaktig hvordan filen er kryptert, men det ser ut som om nøkkelfilen inneholder lister med tall som går fra 0-28 og er nøyaktig 29 elementer lang. Det kan også virke som om , og linjene er ivaretatt.

Cypheralvene antar at dersom man har nøkkelen

```
  a   b   c  d   e   f  g   h  i   j  k  l   m  n   o   p  q   r   s   t  u   v   w  x   y  z   æ   ø   å
[15, 23, 21, 5, 11, 26, 8, 20, 6, 28, 2, 7, 19, 3, 22, 14, 24, 1, 18, 13, 4, 12, 27, 0, 17, 9, 25, 16, 10]
```

Vil ordet "Jul" bli til "åeh". Og for å gå tilbake til ordet "Jul", må du finne hvilken bokstav som har i nøkkelen som inneholder cypher-bokstaven.

Visualisering av nøkkelkorrespondans:

```
  a   b   c  d   e   f  g   h  i   j  k  l   m  n   o   p  q   r   s   t  u   v   w  x   y  z   æ   ø   å
[ p,  x,  v, f,  l,  æ, i,  u, g,  å, c, h,  t, d,  w,  o,  y, b,  s,  n, e,  m,  ø, a,  r, j,  z,  q,  k]
```

# Solution

```javascript
// Load values from file:
const fs = require("fs");
let key = fs.readFileSync("input.txt", "utf-8");
let poem = fs.readFileSync("cypher.txt", "utf-8");

const alphabeth_ordered = "abcdefghijklmnopqrstuvwxyzæøå".split("");

// Read and parse data
key = key.split("\r\n").map(value => JSON.parse(value));
poem = poem.match(/(.*?\s+)/g).map((word, index) => {

    let alphabeth_crypted = key[index].map(value => alphabeth_ordered[value]);

    // Loop through every character to decrypt them:
    return word.split("").map(char => {
        const cryptedIndex = alphabeth_crypted.indexOf(char);
        return cryptedIndex > -1 ? alphabeth_ordered[cryptedIndex] : char
    }).join("");
})

console.log(poem.join(""));

// Answer:

console.log("Solution: "+poem.join("").split("\n").map(val => val.charAt(0)).join("").replace(" ", ""));
```

Returns:

```
julenissen gikk en tur i nordpolens vakre daler
der møtte han noen fine dyr, med veldig korte haler
han hoppet opp i gledens dans, og hilste blidt på dem
og flyvende, de kom dit hen, med gevir på hodets lem

slik var det nissen fant reinets dyr
og vant sin store glede
og livet har siden vært et eventyr
for nå flyr de julens store slede

om ikke annet skal bli sagt
har alle parter gleden hatt
for julenissen deler godt med mat
som gives bort til reinsdyrs fat

nå er vårt dikt ved veiens ende
men gled deg, for du er vår venn
julen kommer snart til å hende
og nissen giver gaver nok igjen

løsningen er første bokstav i hver linje satt sammen, uten mellomrom, inkludert denne

Solution: jdhosoofohfsnmjol
```

# Flag

```
jdhosoofohfsnmjol
```