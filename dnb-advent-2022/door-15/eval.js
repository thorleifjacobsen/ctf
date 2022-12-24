const readline = require('readline');
const http = require('http');

const defaultOptions = {
    host: 'grinchcalculator.ambitiousbeach-e7bbe16d.norwayeast.azurecontainerapps.io',
    port: 80,
    headers: { 'Content-Type': 'application/json' }
}

const post = (path, payload) => new Promise((resolve, reject) => {
    const options = { ...defaultOptions, path, method: 'POST' };
    const req = http.request(options, res => {
        let buffer = "";
        res.on('data', chunk => buffer += chunk)
        res.on('end', () => resolve(buffer))
    });
    req.on('error', e => reject(e.message));
    req.write(JSON.stringify(payload));
    req.end();
});

var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let history = [];

rl.on('line', async (input) => {
    if(input == "fn") { rl.setPrompt("$ "); rl.prompt(true); return true; }
    if(input == "ev") { rl.setPrompt("> "); rl.prompt(true); return true; }

    if (rl.getPrompt() == "$ ") {
        history.push(input);
        input = `eval.constructor("return (() => {${input.replace(/(["'])/g, "\\$1")}})()")()`;
        let data = await post("/evaluate", { exp: input })
        console.log(data);
    } else {
        history.push(input);
        let data = await post("/evaluate", { exp: input })
        console.log(data);
    }
    rl.prompt(true);
});

rl.on('keypress', (str, key) => {
    if (key.name === 'up' && history.length > 0) {
        const previousCommand = history[history.length - 1];
        rl.setInput(previousCommand);
    } else if (key.name === 'down' && history.length > 0) {
        const nextCommand = history[history.length - 1];
        rl.setInput(nextCommand);
    }
});

console.log("Started eval script.");
console.log("Commands: fn, ev");
rl.prompt();
