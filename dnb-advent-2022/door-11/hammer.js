const axios = require('axios').default;
const url = 'http://djoilerlock.norwayeast.azurecontainer.io:2674/unlock';
let guess = { "keyCodes": ["a", "a", "a"] }

function generateCombinations(numLetters, str = '') {
    if (numLetters === 0) {
        return [str];
    }

    let combinations = [];
    for (let i = 'a'.charCodeAt(0); i <= 'z'.charCodeAt(0); i++) {
        combinations = combinations.concat(generateCombinations(numLetters - 1, str + String.fromCharCode(i)));
    }
    return combinations;
}

(async () => {
    for (let i = 1; i < 3; i++) {
        let combs = generateCombinations(i);

        for (comb of combs) {
            guess.keyCodes = [comb, comb, comb]
            /* These 3 next lines was added after i found the solution.. */ 
            /* it takes 10 seconds to get one true. */
            /* So annoying that I did not just finish this scrip! */
            data = await axios.post(url, guess);
            if (data.data.includes(true)) {
              console.log(`GOT TRUE: ${data.data} on ${guess.keyCodes}`) 
            }
            else { console.log(`No dice: ${guess.keyCodes}`); }
            /* End of modifications AFTER i found solution. I was SO CLOSE! */
        }
    }
})()