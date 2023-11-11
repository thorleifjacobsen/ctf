// Load values from file:
const fs = require("fs");
let data = fs.readFileSync("random_text.bin", "utf-8");

data = data.split("\u0000").sort((a, b) => b.length - a.length);


let letter = 0;
for (let id in data) {
  const val = data[id];
  if (letter == 0 && val.charAt(0) == "E") { console.log(val.charAt(0), id); letter++; }
  else if (letter == 1 && val.charAt(0) == "G") { console.log(val.charAt(0), id); letter++; }
  else if (letter == 2 && val.charAt(0) == "G") { console.log(val.charAt(0), id); letter++; }
  else if (letter == 3 && val.charAt(0) == "{") { console.log(val.charAt(0), id); letter++; }
}
