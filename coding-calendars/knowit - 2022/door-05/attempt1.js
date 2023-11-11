// This was very slow. After 2500 it started to slow down really much
// Time to run until the answer was around 30 seconds on my computer.
// I knew it had to be a better way so I created another attempt (attempt2.js)
// That ran on 0.0051sec


// Define a riffleshuffle function
const outShuffle = (deck, startHalf = "bottom")  => {
    const top = deck.slice(0,deck.length/2);
    const bottom = deck.slice(deck.length/2);
    let shuffeledDeck = [];
    let half = startHalf;
    deck.forEach( _ => { // Quick way to create a loop matching deck size! :P
        if(half == "top") {
            shuffeledDeck.push(top.pop())
            half = "bottom";
        } else {
            shuffeledDeck.push(bottom.pop())
            half = "top";
        }
    });
    return shuffeledDeck.reverse();
}

let startDeckSize = 2;
let stopDeckSize = 10000;


for (let deckSize = startDeckSize; deckSize <= stopDeckSize; deckSize+=2) {

    // Build deck of deckSize cards
    let originalDeck = [];
    for(let i = 1; i<=deckSize; i++) { originalDeck.push(i); }

    let shuffeledDeck = originalDeck;
    for(let shuffleTimes = 1; shuffleTimes<=50; shuffleTimes++) {
        shuffeledDeck = outShuffle(shuffeledDeck);
        if(JSON.stringify(shuffeledDeck) == JSON.stringify(originalDeck)) { 
            if(shuffleTimes == 13) {
                console.log("MATCH"); 
            }
            console.log(`Deck of ${deckSize} back to original position after ${shuffleTimes} times`);
            break;
        }
    }
}