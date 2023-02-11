const fs = require('fs');

// Load dictionary and letter
let dict = {};
fs.readFileSync('dictionary.txt', 'utf8').split("\n").forEach(w => dict[w.split(",")[0]] = w.split(",")[1]);
let letter = fs.readFileSync('letter.txt', 'utf8');
let letterTranslated = "";

let position = 0;
let lastWasSuccess = false; 

let lastSuccessfullMatch = []
let bannedWords = {};

// Loop through until the position is at the last element.
while(position < letter.length) {
    
    // In last run there was no found words. So we cannot continue one this word
    // I'll pop out the last word and ban it from the position so it wont be tested again.
    if (!lastWasSuccess) {
        let lastWord = lastSuccessfullMatch.pop();
        // Revert position marker
        position = lastSuccessfullMatch.reduce((a,b) => a+b.length, 0);

        // Add this word to banned words on this position.
        if(bannedWords[position]) bannedWords[position].push(lastWord);
        // Initialize the positions's array if not existing.
        else bannedWords[position] = [lastWord] 
    }

    // New start, lets go!
    lastWasSuccess = false;
    position = lastSuccessfullMatch.reduce((a,b) => a+b.length, 0);

    for (let word in dict) { 

        let isBannedWord = typeof bannedWords[position] == "object" && bannedWords[position].includes(word);

        // If letter can be found on this position and it is not banned we're good to go!
        if (letter.slice(position).indexOf(word) == 0 && !isBannedWord) {
            lastSuccessfullMatch.push(word);
            lastWasSuccess = true;
            break;
        }
    }   
}

lastSuccessfullMatch.forEach(word => letterTranslated += `${dict[word]} `);
console.log(letterTranslated.trim().length);