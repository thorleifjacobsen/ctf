const fs = require('fs');
const crypto = require('crypto');

// Generate combinations for each part of the pattern
const lettersCM = [...Array(11).keys()].map((i) => String.fromCharCode(i + 'c'.charCodeAt(0)));
const digits09 = [...Array(10).keys()].map(String);
const lettersFZ = [...Array(21).keys()].map((i) => String.fromCharCode(i + 'f'.charCodeAt(0)));
const numbers27 = ['2', '3', '4', '5', '6', '7'];
const numbers15 = ['1', '2', '3', '4', '5'];

// Helper function to calculate the cartesian product of multiple arrays
function cartesian(...arrays) {
  return arrays.reduce(
    (acc, curr) =>
      acc.flatMap((c) => curr.map((n) => [].concat(c, n))),
    [[]]
  );
}

// Generate all combinations based on the pattern
const allCombinations = cartesian(lettersCM, digits09, lettersFZ, lettersFZ, numbers27, numbers15);

// Adjust for zero-based indexing and get the 585937th key
const correctKeyIndex = 585937 - 1; // Adjust for zero-based indexing
const correctKeyCombination = allCombinations[correctKeyIndex];

// Convert the array to a string to represent the key
const correctKey = correctKeyCombination.join('');

// Format the flag
const flag = `UiTHack24{${correctKey}}`;

console.log(flag);