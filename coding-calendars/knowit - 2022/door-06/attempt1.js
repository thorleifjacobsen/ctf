const fs = require('fs');

// Load dictionary and letter
let meanActions = {}; // {}
fs.readFileSync('slemmehandlinger.txt', 'utf8').split("\n").forEach(w => meanActions[w.split(":")[0]] = w.split(":")[1]);
let votes = fs.readFileSync('stemmer.txt', 'utf8').split("\n");

let tally = {};

votes.forEach(vote => {
    let voted = vote.split(":")[1];
    let actions = vote.split(":")[0].split(",");

    if (typeof tally[voted] == "undefined") tally[voted] = 0;

    let tallyWeight = actions.reduce((lowest,act) => meanActions[act] < lowest ? meanActions[act] : lowest, 1);
    tally[voted] += parseFloat(tallyWeight);
})

for (candidat in tally) {
    tally[candidat] = Math.round(tally[candidat]); 
}

// Sort biggest to lowest 
const sort = Object.entries(tally).sort((a, b) => b[1] - a[1]);

// Calculate the answer.
console.log(sort[0][1]-sort[1][1]);