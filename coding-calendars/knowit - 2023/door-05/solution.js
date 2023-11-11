// Check if number is prime
const isPrime = num => {
    for(let i = 2, s = Math.sqrt(num); i <= s; i++) {
        if(num % i === 0) return false;
    }
    return num >= 2;
}

// Criterias: sum of digits, divided by sum, is whole number, is prime
const isSumDividePrime = num => {
    const sum = num.toString().split("").map(Number).reduce((a, b) => a + b, 0);
    const dividedBySum = num / sum;
    return Number.isInteger(dividedBySum) && isPrime(dividedBySum);
}

let sumDividePrimes = 0;

for (let i = 1; i <= 100000000; i++) {
    if (isSumDividePrime(i)) {
        sumDividePrimes ++;
    }
}

console.log(sumDividePrimes);