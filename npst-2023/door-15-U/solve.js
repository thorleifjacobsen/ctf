const fs = require("fs");

const filePrefix = "./manual/manual.bak.";
const regex = new RegExp(`[{}#$\\[\\]§¤@]`);
// Regexp for a-z A-Z 0-9
const regex2 = new RegExp(`[a-zA-ZæøåÆØÅ]`);

let letter = 0;
let reconstructedLetters = {};

while (letter < 10) {

    for (let i = 0; i < 1000; i++) {
        // Pad number to 3 digits
        const file = filePrefix + i.toString().padStart(3, "0");

        const fileData = fs.readFileSync(file, "utf-8").split("");

        // Check if letter number has any of these characters: {}#$[]§¤@
        if (regex2.test(fileData[letter])) {
            reconstructedLetters[letter] = fileData[letter]

            console.log(reconstructedLetters);
        }
    }

    letter++;

}