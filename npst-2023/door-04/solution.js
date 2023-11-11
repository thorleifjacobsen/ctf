// Load values from file:
const fs = require("fs");
let data = fs.readFileSync("pinneved.txt", "utf-8");

// Parse data:
const otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15].reverse();
const parts = data.match(RegExp(`.{1,${Math.ceil(data.length / otp.length)}}`, 'g')) || [];

// Reverse the `ascii` values of each character in each fragment:
let reversedFragments = parts.map(fragment => {
  return fragment.split('').map(c => String.fromCharCode(c.charCodeAt(0) - 2)).join('');
});

// Rebuild the fragments in the correct order:
const rebuildFragments = [];
for (let i = 0; i < otp.length; i++) {
    rebuildFragments[otp[i]] = reversedFragments[i];
}

// Print the result:
console.log(rebuildFragments.join(''));