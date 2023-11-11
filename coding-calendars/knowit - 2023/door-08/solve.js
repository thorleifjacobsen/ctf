// Load values from file:
const fs = require("fs");
let key = fs.readFileSync("input.txt", "utf-8");
let poem = fs.readFileSync("cypher.txt", "utf-8");

const alphabeth_ordered = "abcdefghijklmnopqrstuvwxyzæøå".split("");

// Read and parse data
key = key.split("\r\n").map(value => JSON.parse(value));
poem = poem.match(/(.*?\s+)/g).map((word, index) => {

    let alphabeth_crypted = key[index].map(value => alphabeth_ordered[value]);

    // Loop through every character to decrypt them:
    return word.split("").map(char => {
        const cryptedIndex = alphabeth_crypted.indexOf(char);
        return cryptedIndex > -1 ? alphabeth_ordered[cryptedIndex] : char
    }).join("");
})

console.log(poem.join(""));

// Answer:

console.log("Solution: "+poem.join("").split("\n").map(val => val.charAt(0)).join("").replace(" ", ""));
