# Ikkesett-sekvensen

Vi definerer en tallrekke der forekomster i tallrekken er stigende positive heltall som tidligere ikke er observert i den konkatenerte representasjonen av rekken.

## Forklaring:

Rekken starter som forventet: `0,1,2,3,4,5,6,7,8,9,10,11,13` men merk at `12` ikke er i rekken, siden vi allerede har `1,2` i rekken.

## Oppgave:

Hvor mange elementer mindre enn 100 000 er det i rekken?

# Solution

```javascript
const max = 100_000;
const sequence = [];

for (let i = 0; i < max; i++) {

    const currentNumberString = i.toString();
    const sequenceString = sequence.join("");

    if (!sequenceString.includes(currentNumberString)) {
        sequence.push(i);
    }
}

console.log(sequence.length);
```

## Runtime:

```shell
$ time node solution.js
23111

real    0m49,124s
user    0m44,480s
sys     0m7,900s
```

## Made a faster one

[solution_faster.js](solution_faster.js)

```shell
$ time node solution_faster.js 
23111

real    0m2,572s
user    0m2,552s
sys     0m0,025s
```