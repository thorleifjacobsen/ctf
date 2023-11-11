// Load values from file:
const fs = require("fs");
let rows = fs.readFileSync("rekke.txt", "utf-8");

rows = JSON.parse(rows.replaceAll("(", "[").replaceAll(")", "]"))

// rows = [[1, 2], [4, 3], [2, 3], [5, 8], [7,6], [5,4], [6,8]]

rows.sort 
console.log(rows)

let sortedRow = []

for (let elf of rows) {

  let indexOfLeft = sortedRow.findIndex(element => element.includes(elf[0]))
  let indexOfRight = sortedRow.findIndex(element => element.includes(elf[1]))

  if (indexOfLeft + indexOfLeft == -2) { sortedRow.push(elf); }
  else if (indexOfLeft > indexOfRight) {
    sortedRow.splice(indexOfLeft, 0, elf)
  }
  else {
    sortedRow.splice(indexOfRight, 0, elf)

  }
  console.log(indexOfLeft, indexOfRight)

  
  // console.log(rows.indexOf(elf));
}

console.log(sortedRow);

console.log(sortedRow[Math.floor(sortedRow.length / 2)]);