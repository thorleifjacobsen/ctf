/* Not very effective: Runtime 31 seconds */

const validatePalin = (str) => {  
    const len = str.length;  
    for (let i = 0; i < len / 2; i++) {  
        if (str[i] !== str[len - 1 - i]) {  
            return false; 
        }  
    }  
    return true;
}  
const isMultiPalin = (number) => {
    let match = 0;

    // Check radix 2->16
    for (let i = 2; i<=16; i++) {
        if(validatePalin(number.toString(i))) match++;
    }
    return match >= 3; // If palin on atleast 3 of the 15 bases.
}

let answer = 0;

for (let i = 0; i<=10000000; i++) {
    if(isMultiPalin(i)) { answer += i; }
}

console.log(answer);

