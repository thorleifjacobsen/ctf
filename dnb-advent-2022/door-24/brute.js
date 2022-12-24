

const axios = require('axios').default;
const url = 'http://elliotspasswordfinder.norwayeast.azurecontainer.io/api/parts/';
let guess = { id: 10, word: "test" }

let found = []; // Ignore those found, add to list

let combs = "crypto stego constant pain breakpoint dancing meltdown overflow my bufer pop my stack hardware problem oct31 catch my exception hackers assemble drcircuit and the stack tracers ctf".split(" ");

(async () => {
    for (comb of combs) {
        console.log(`Testing: ${comb}`)
        let promises = [];
        for (let i = 1; i <= 10; i++) {
            if (found.includes(i)) { continue; }
            guess.id = i;
            guess.word = comb;
            
            let newUrl = url + i;

            promises.push(axios.post(newUrl, guess)
                .then(data => {
                    if (data.data.operation != "failed") console.log(`${i} - ${guess.word} = ${data.data.operation}`);
                }));

        }
        await Promise.all(promises);
    }
})();