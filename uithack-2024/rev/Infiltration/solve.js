// Define the character array from the Java code
const str = ['x', 'D', 'y', 'e', 'L', 'N', 'F', 31, 25, 'V', 'z', 'E', 30, '_', 30, 'r', 28, 24, 'r', '@', 'T', 'r', 'N', 'X', ']', 'r', 29, 'K', 'r', 'G', 25, '[', 25, 18, 'P'];

let output = '';
for (let i = 0; i < str.length; i++) {
  // If number, use directly, otherwise get the char code
  const charCode = typeof str[i] === 'number' ? str[i] : str[i].charCodeAt(0);
  // XOR with the char code of '-', and convert back to a character
  output += String.fromCharCode(charCode ^ '-'.charCodeAt(0));
}
console.log(output);