const max = 100_000;
const sequence = [];

for (let i = 0; i < max; i++) {

    const currentNumberString = i.toString();
    const sequenceString = sequence.join("");

    if (!sequenceString.includes(currentNumberString)) {
        sequence.push(i);
    }
}

console.log(sequence.length);