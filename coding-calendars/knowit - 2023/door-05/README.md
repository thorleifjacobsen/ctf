# Summe-dele-primtall

Hvis man tar tallet 18 og deler det opp i sifferene det består av, så får man 1 og 8. Hvis man plusser sammen disse sifferene får man tallet 9. Hvis man deretter tar tallet 18 og deler på 9 så får man heltallet 2, som er et primtall. Vi definerer derfor 18 som et summe-dele-primtall tall.

## Eksempel på summe-dele-primtall
Hvis vi tar tallet 9015, så er summen av sifferene lik 15. Hvis vi nå tar 9015 og deler på 15, så får vi heltallet 601. 601 er et primtall, og dermed er 9015 et summe-dele-primtall.

## Oppgave
Nissen har glemt koden til en av leketøyfabrikkene sine. Men frykt ikke! Han husker nemlig at koden er det samme som hvor mange summe-dele-primtall det eksisterer mellom 1 og 100 000 000. Kan du finne koden?

# Solution

[JavaScript](./solution.js) Made by me

[Go](./solution.rs) Made with ChatGPT by providing the Javascript solution

[Rust](./solution.go) Made with ChatGPT by providing the Javascript solution

```javascript
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

console.log(sumDividePrimes); // 642344
```