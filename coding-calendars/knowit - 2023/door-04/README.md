# Jule-en, jule-to, jule-tre...ning?

For å førebu seg på høgtida har Julenissen lagt seg i hardtrening det siste året. Han har blant anna gjort mange situps, og har loggført kor mange repitisjonar han klarte for kvar treningsøkt i [denne fila](./reps.txt). Nokon økter er betre enn andre, men det som er viktig for Julenissen er å klare fleire enn forrige trening.

## Oppgåve

Kor mange repitisjonar gjer Julenissen totalt i den lengste rekka av treningar der han klarer fleire repitisjonar enn dagen før? Om det er meir enn ein sekvens som kan vere mogleg svar ser vi etter den med størst sum.

## Døme

For øktene 133, 266, 174, 295, 228, 257, 75, 41, 370, 125, 188, 284, 301, 219, 276, 134, 315, 190, 183, 381, 12, 351, 384, 151, 255, 231, 232, 205, 95, 0, 97 ser vi at den lengste rekka med stigane repitisjonar er 125, 188, 284, 301, som er totalt 898 repitisjonar.

# Solution

```javascript
// Load values from file:
const fs = require("fs");
let reps = fs.readFileSync("reps.txt", "utf-8");

// Parse data:
reps = reps.split(",") // Split data into days
           .map(value => parseInt(value.trim())); // Convert value to number

let highestRepeatedSequence = [0, 0];
let currentSequence = [];
for (let rep of reps) {

  const previous = currentSequence[currentSequence.length-1] || 0;

  // If the current rep is higher than the previous rep, add it to the sequence
  if (rep > previous) {
    currentSequence.push(rep);
  } 

  // The current rep was lower than the previous rep
  else {
    
    // Calculate the sum of the sequence
    let sum = currentSequence.reduce((a,b) => a+b, 0);

    if(currentSequence.length > 4) console.log(`Sequence: ${currentSequence.length} - ${currentSequence.join(",")} - ${sum}`);
    
    // Replace highestRepeatedSequence if the current sequence is longer or higher sum.
    if (currentSequence.length >= highestRepeatedSequence[0]) {
      if (sum > highestRepeatedSequence[1] || currentSequence.length > highestRepeatedSequence[0]) {
        highestRepeatedSequence = [currentSequence.length, sum];
      }
    }

    // Reset the sequence to start the current rep
    currentSequence = [rep];
  }
}

console.log(highestRepeatedSequence); // [ 6, 969 ]
```