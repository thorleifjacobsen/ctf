const knownNumbersOrPath = {
    "1": "int()**int()",
    "2": "int()**int()+int()**int()",
    "3": "1+1+1",
    "4": "2*2",
    "5": "4+1",
    "7": "4+3",
    "8": "2**3",
    "16": "2**2**2",
    "32": "16*2",
    "37": "32+3+2",
    "64": "4**3",
    "46": "32+8+4+2",
    "47": "32+8+4+2+1",
    "81": "3**4",
    "97": "32*3+1",
    "100": "int(repr(int()**int())+repr(int())+repr(int()))",
    "101": "100+1",
    "102": "100+2",
    "103": "100+3",
    "104": "32*3+8",
    "105": "32*3+8+1",
    "108": "32*3+8+4",
    "109": "32*3+8+4+1",
    "111": "int(repr(int()**int())+repr(int()**int())+repr(int()**int()))",
    "112": "111+1",
    "115": "111+3",
    "116": "111+5",
    "120": "111+8+1",
}

const generateCharacterFormula = (number, wrap) => {
    let formula = knownNumbersOrPath[number];
    if (!formula) { 
        // Find all numbers required to generate this number
        const numbers = [];
        let n = number;
        values = Object.keys(knownNumbersOrPath).map((x) => parseInt(x)).sort((a, b) => b - a);
        while (n > 0) { for (const value of values) { if (value <= n) { n -= value; numbers.push(value); break; } } }
        formula = numbers.join("+");
    }
    
    // If it has plusses it usually requires parenthesis
    // this could save a bit to be optimized but, ey it works.
    if (formula.includes("+")) {
        formula = `(${formula})`;
    }

    // If this formula has numbers we need to generate the formula for those numbers
    formula = formula.replace(/\d+/g, (match) => {
        return generateCharacterFormula(match);
    });

    return formula;
}

// If no arguments use default path
const path = process.argv[2] || "/lol/hemmeligmappe/flagg.txt";
let skipNext = false;
let string = path.split("");

// Generate formula for each character
string = string.map((x,idx) => {

    // If previous character was the same we skip.
    if(skipNext) { skipNext = false; return ""; }

    // If then ext character is the same we can save some bytes
    // by using the multiplication operator and multiply it by 2.
    if (string[idx+1] == x) {
        skipNext = true;
        return `(chr(${generateCharacterFormula(x.charCodeAt(0))})*(int()**int()+int()**int()))`;
    }

    // If not we just get the formula for it.
    return `chr(${generateCharacterFormula(x.charCodeAt(0))})`;
});

// Remove any skipped characters
string = string.filter((x) => x != "");

// Log length of all our known numbers to see where we can optimize
Object.keys(knownNumbersOrPath).map((x) => {
    // console.log(x, generateCharacterFormula(x).length); // Disabled on completed program
});

// Join all the characters together and log information
const fullString = `print(*open(${string.join("+")}))`;
console.log(`Total length of program: ${fullString.length}`);

// Run program and get result
const url = `https://helsectf2024-2da207d37b091b1b4dff-short-not-cipher.chals.io?program=${encodeURIComponent(fullString)}`;
fetch(url).then((x) => x.text()).then((x) => console.log(x));