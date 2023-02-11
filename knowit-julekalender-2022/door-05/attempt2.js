// You can use this equation to prove if a deck og k size can be solved in n amount of out shuffles.
// Math equation: pow(2,n) = 1 (mod k-1)
// So with 52 cards: Math.pow(2,8)%51 = 1
// So based on this I could bruteforce from 2 cards and upwards until I found something that = 1 on 13 out shuffles
// Since Math.pow is slow we just precalculate Math.pow(2,13) to be 8192. Then we can modula that with the deck size.

for(let deckSize = 2; deckSize<=10000; deckSize+=2) {
    if (8192%(deckSize-1) == 1) {
        console.log(`Required deck size: ${deckSize}`);
        return
    }
}