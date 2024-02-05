# Larsw sekvens

Vi har fanget opp en spesiell sekvens `AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAA` med en liste av korte tegn:

```
AjAA
AiAA
kAAl
AAnA
AiAA
hAAi
AnAA
iAAj
pAAq
QAAR
AAlA
AYAA
LAAM
AgAA
AgAA
AAiA
AiAA
WAAX
mAAn
nAAo
jAAk
AZAA
AlAA
LAAM
AqAA
```

Kameraten til Lars sier at han kan ha brukt dette til å kryptere flagget. Lars har muligens en overdreven interesse i sekvenser laget av Nicolaas Govert.

# Writeup

The text sends some signal that this is a sequence method by Nicolaas Govert. He have a sequance named [de Bruijn](https://en.wikipedia.org/wiki/De_Bruijn_sequence). The sequence given to us seems to contain A-Z and a-z followed by `AA`. 

I made a script [solve.js](./solve.js) which uses the sequence and the list to find the flag. 

```javascript 
const seq = "AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAA"
const list = ["AjAA", "AiAA", "kAAl", "AAnA", "AiAA", "hAAi", "AnAA", "iAAj", "pAAq", "QAAR", "AAlA", "AYAA", "LAAM", "AgAA", "AgAA", "AAiA", "AiAA", "WAAX", "mAAn", "nAAo", "jAAk", "AZAA", "AlAA", "LAAM", "AqAA"]

list.map((x) => {
    process.stdout.write(String.fromCharCode(seq.indexOf(x)));
})

process.stdout.write("\n")
```

# Flag

```
helsectf{0mG!__deBruiJn!}
```
