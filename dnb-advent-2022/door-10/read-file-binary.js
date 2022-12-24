const fs = require('fs');

// let file = "wl-original.txt";
// let file = "mywishlist-original.txt"
let file = "mywishlist.txt"
fs.readFile(file, (err, data) => {
    if (err) throw err;
    let str = "[";
    for (let i = 0; i < data.length; i++) {
        str += "0x" + data[i].toString(16) + ", ";
    }
    console.log(str.substring(0,str.length-2) + "]")
});

