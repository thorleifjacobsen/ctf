let flag = Buffer.from("JHtMMEFmcGd4N0tAeDRQMGtAbHh9", 'base64').toString('ascii');
const alpha = 'abcdefghijklmnopqrstuvwxyz';

const rot = (message, num) => {
    return message.replace(/[a-z]/gi, letter => { 
        //console.log(letter, alpha.indexOf(letter))
        let sl = letter.toLowerCase();
        let idx = (alpha.indexOf(sl) + num) % alpha.length;

        if(alpha.indexOf(letter.toLowerCase()) > -1) {
            if(letter.toLowerCase() !== letter) { return alpha[idx].toUpperCase() }
            return alpha[idx]
        }
        else return letter;
        
    });
}

console.log(`Flag is: ${flag}`);

for (let i = 0; i<25;i++) {
    let flagRot = rot(flag, i);
    console.log(`Rotated ${i} = ${flagRot}`);
}

//Rotated 2 = ${N0Chriz7M@z4R0m@nz}