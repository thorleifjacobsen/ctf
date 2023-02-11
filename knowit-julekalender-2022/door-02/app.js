const fs = require('fs');

let presents = fs.readFileSync('gaver.txt', 'utf8').split("\n");
let previousPresents = [];
let lines = presents.length; // One line per present is a given

presents.forEach(present => {

    previousPresents.push(present);
    let linesForThisDay = previousPresents.length - 2 // We remove 2 this will put up to 3 packages on 1 line.

    // If linesForThisDay is less than 0 then we have not overflown the 3 packages for speedsinging. So we must add 1 line for those.
    lines += linesForThisDay > 0 ? linesForThisDay : 1; // always add 1 line, but if there is less than 3 no need.
    
    // If it contained alv, remove it.
    if(present.indexOf("alv") > -1) {
        previousPresents.pop();
    }
});

console.log(lines);