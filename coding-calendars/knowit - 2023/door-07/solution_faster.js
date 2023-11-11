let count = 0;
let sequence = "";

for (let i = 0; i < 100_000; i++) {

    const currentNumberString = i.toString();

    if (sequence.indexOf(currentNumberString) == -1 ) {
        count ++;
        sequence += currentNumberString;
    }
}
console.log(count);