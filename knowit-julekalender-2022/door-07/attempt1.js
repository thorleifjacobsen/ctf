const fs = require('fs');

// Load dictionary and letter
let code = [];
fs.readFileSync('encrypted.txt', 'utf8').split("\n").forEach(e => code.push(e.trim().split(" ")));
let width = code[0].length;
let height = code.length;


code.forEach(line => {
  let l = "";
  line.forEach(pixel => {
    let bin = parseInt(pixel).toString(2);
    let isEvil = (bin.match(/1/g) || []).length % 2 != 0
    // console.log(isEvil); 
    l += (isEvil ? "#" : " ");
    // console.log(parseInt(pixel).toString(2));
  })

  
  console.log(l);
  
});