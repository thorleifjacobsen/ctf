const fs = require('fs');

const cipher = fs.readFileSync("chiffertekst.txt", "utf-8").split("");
const cleartext = fs.readFileSync("klartekst.txt", "utf-8").split("");

function generateVigenereTable(alphabet) {
    let table = [];
    for (let i = 0; i < alphabet.length; i++) {
        let row = [];
        for (let j = 0; j < alphabet.length; j++) {
            row.push(alphabet[(j + i) % alphabet.length]);
        }
        table.push(row);
    }
    return table;
}

function findRepeatingKey(str) {
    // Regex to find repeating patterns
    const regex = /(.+?)\1+/;
    const match = str.match(regex);

    if (match && match.length > 1) {
        // The first captured group is the key
        return match[1];
    } else {
        return null; // or some default value if no repeating pattern is found
    }
}

function rotateKey(word) {
    word = word.split('');
    let firstLetter = word.shift();
    word.push(firstLetter);
    return word.join('');
}


let al1 = "qwertyuiopå"
let al2 = "asdfghjkløæ"
let al3 = "zxcvbnm"

let possibleKeys1 = "";
let possibleKeys2 = "";
let possibleKeys3 = "";

// Find key, we know the letter and cipher for a big chunk of the text
for (let i = 0; i < cleartext.length; i++) {
    const letter = cleartext[i];
    const cipherLetter = cipher[i];

    // Get table for this letter
    let table = undefined
    if (al1.includes(letter)) { table = generateVigenereTable(al1); }
    if (al2.includes(letter)) { table = generateVigenereTable(al2); }
    if (al3.includes(letter)) { table = generateVigenereTable(al3); }
    if (!table) { continue; }

    // Find out which row the letter is in
    let firstRow = table[0];
    let index = firstRow.indexOf(letter);
    
    // Find out which row the cipherletter is in the same index
    let cipherRow = table.find(row => row[index] == cipherLetter);

    // Add the key to the possible keys
    if (al1.includes(letter)) { possibleKeys1 += cipherRow[0]; }
    if (al2.includes(letter)) { possibleKeys2 += cipherRow[0]; }
    if (al3.includes(letter)) { possibleKeys3 += cipherRow[0]; }
}   


const key = []
key[1] = findRepeatingKey(possibleKeys1);
key[2] = findRepeatingKey(possibleKeys2);
key[3] = findRepeatingKey(possibleKeys3);

let decoded = "";

// Now lets decode it:
for (let i = 0; i < cipher.length; i++) {
    const cipheredLetter = cipher[i];


    // Get table and key for this letter
    let table = undefined
    let keyIndex = 0;
    if (al1.includes(cipheredLetter)) { table = generateVigenereTable(al1); keyIndex = 1; }
    if (al2.includes(cipheredLetter)) { table = generateVigenereTable(al2); keyIndex = 2; }
    if (al3.includes(cipheredLetter)) { table = generateVigenereTable(al3); keyIndex = 3; }
    if (!table) { decoded += cipheredLetter; continue }


    // Find out which row the cipherletter is in the same index
    let firstRow = table[0];
    // get first letter in key
    const keyLetter = key[keyIndex][0];
    // rotate key
    key[keyIndex] = rotateKey(key[keyIndex]);
    // find index of key letter in row
    const rowIndex = firstRow.indexOf(keyLetter);

    let cipherRow = table.find(row => {
        if (row[rowIndex] == cipheredLetter) {
            return true;
        }
        return false
    });

    decoded += cipherRow ? cipherRow[0] : cipheredLetter;
}

console.log(decoded);