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

console.log(highestRepeatedSequence);