const { spawn } = require('child_process');
const fs = require('fs');

const encrypt = async (text) => {
    return new Promise((resolve, reject) => {
        const child = spawn("./re-santa-3");
        child.stdout.on('data', (data) => { });
        child.on('close', (code) => {

            let file = "mywishlist.txt"
            fs.readFile(file, (err, data) => {
                if (err) throw err;
                let str = [];
                for (let i = 0; i < data.length; i++) { str.push(data[i]); }
                resolve(str);
            });
        });
        child.stdin.end(text + "\n");

    })
}

(async () => {
    let encryptedWishlist = [0x1f, 0x9e, 0xe2, 0xe2, 0x9e, 0xa3, 0xd8,
        0x9a, 0x48, 0xc4, 0xab, 0x2e, 0x3a, 0x24,
        0xee, 0x8f, 0x68, 0xa5, 0x9d, 0xad, 0x46,
        0x3a, 0x85, 0x5a, 0xf8, 0xd5, 0x4e, 0xb3]

    let knownString = "${"

    // Generate a list of all ascii characters
    let charset = '';
    for (var i = 0; i <= 127; i++) charset += String.fromCharCode(i);
    
    while (knownString.length < encryptedWishlist.length) {

        for (let i = 0; i < charset.length; i++) {
            let testString = (knownString + charset[i]).padEnd(encryptedWishlist.length, "-");
            let result = await encrypt(testString);

            // knownString.length is without the 0 so this will automatically
            // show the next now known letter to compare.
            if (result[knownString.length] == encryptedWishlist[knownString.length]) {
                knownString += charset[i];
                break;
            }
        }

        // Output progress!
        console.log(knownString);
    }
})()