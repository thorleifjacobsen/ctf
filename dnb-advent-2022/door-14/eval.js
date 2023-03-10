const http = require('http');
let input = process.argv.slice(2).join(" ").trim();

const map = { "1": "ð", "2": "ð", "3": "ð", "4": "ð","5": "ð","6": "ð","7": "ð","8": "ð","9": "ðĨ­","0": "ð","a": "ð", "b": "ð", "c": "ð", "d": "ðĐ", "e": "ðŠ", "f": "ðŧ", "g": "ðž", "h": "ðŦ", "i": "ðŽ", "j": "ð­", "k": "ðŪ", "l": "ðŊ", "m": "ðī", "n": "ð·", "o": "ðļ", "p": "ðđ", "q": "ðš", "r": "ðŧ", "s": "ð―ïļ", "t": "ðū", "u": "ðŋ", "v": "ð", "w": "ð ", "x": "ðĒ", "y": "ðĨ", "z": "ðĻ", "A": "ð", "B": "ðū", "C": "ðĪŠ", "D": "ðĪ", "E": "ð", "F": "ð", "G": "ðïļ", "H": "ðïļ", "I": "ð", "J": "ðïļ", "K": "ðĄ", "L": "ðĒ", "M": "ðĢ", "N": "ðĪ", "O": "ðĨ", "P": "ðĶ", "Q": "ðĻ", "R": "ðĐ", "S": "ðŠ", "T": "ðģ","U": "ðĄ","V": "ð","W": "ð","X": "ðē","Y": "ð","Z": "ð","!": "â","\"": "âĪïļ","#": "ð","$": "ð°","%": "ðŊ","&": "ð","'": "ð","(": "ð",")": "ð","*": "âĻ","+": "â",",": "ðââïļ","-": "â",".": "ðââïļ","/": "ðĄïļ",":": "ðââïļ",";": "ðââïļ","<": "ð","=": "ð",">": "ð","?": "â","@": "ðŽ","[": "ð","\\": "âŽïļ","]": "ð","^": "ðš","_": "ðŧ","`": "âïļ","{": "ð","|": "ð","}": "ð","~": "ð" };
const flag = "ð°ðððŽðĪððŽððŧðĪŠððĪððŧðððŧðūðððĄððŧððŧðĪŠðŧððĒðĪðððĪðĪŠððĪðâð";
const decode = (data) => {
    let newString = "";
    Array.from(data).forEach((char) => {
        if(map.hasOwnProperty(char)) newString += map[char];
        else if(Object.values(map).includes(char)) {
            newString += Object.keys(map)[Object.values(map).indexOf(char)];
        }
        else newString += char;
    })
    return newString;
}

console.log(decode(flag));

const defaultOptions = {
    host: 'santascodeconsole.norwayeast.azurecontainer.io',
    port: 8192,    
    headers: { 'Content-Type': 'application/json' }
}

const post = (path, payload) => new Promise((resolve, reject) => {
    const options = { ...defaultOptions, path, method: 'POST' };
    const req = http.request(options, res => {
        let buffer = "";
        res.on('data', chunk => buffer += chunk)
        res.on('end', () => resolve(JSON.parse(buffer)))
    });
    req.on('error', e => reject(e.message));
    req.write(JSON.stringify(payload));
    req.end();
});

input = "31131122211311123113321112131221123113111231121113311211131221121321131211132221123113112211121312211231131122211211133112111311222112111312211312111322211213211321322123211211131211121332211231131122211311122122111312211213211312111322211231131122211311123113322112111331121113112221121113122113111231133221121113122113121113222123211211131211121332211213211321322113311213211322132112311321322112111312212321121113122122211211232221123113112221131112311332111213122112311311123112111331121113122112132113311213211321222122111312211312111322212321121113121112133221121321132132211331121321132213211231132132211211131221232112111312212221121123222112132113213221133112132123123112111311222112132113311213211231232112311311222112111312211311123113322112132113212231121113112221121321132122211322212221121123222112311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122211311123113322113223113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331221122311311222112111312211311123113322112132113213221133122211332111213112221133211322112211213322112111312211312111322212321121113121112131112132112311321322112111312212321121113122112131112131221121321132132211231131122211331121321232221121113122113121122132112311321322112111312211312111322211213111213122112132113121113222112132113213221133112132123222112311311222113111231132231121113112221121321133112132112211213322112111312211312111322212311222122132113213221123113112221133112132123222112111312211312111322212321121113121112133221121311121312211213211312111322211213211321322123211211131211121332211213211321322113311213212312311211131122211213211331121321122112133221123113112221131112311332111213122112311311123112111331121113122112132113121113222112311311222113111221221113122112132113121113222112132113213221133122211332111213322112132113213221132231131122211311123113322112111312211312111322212321121113122123211231131122113221123113221113122112132113213211121332212311322113212221";
(async () => {
    for (let i = 0; i<100; i++) {
        
        let data = { code: input };
        const token = await post("/eval", data);
        // console.log(`Sending: ${data.code}`);
        // console.log(`Result: ${token.result}`);
        // console.log(`Result Decoded: ${decode(token.result)}`);
        input = token.result;
        console.log(`Status: ${decode(input)} ${token.status}`);
        
    }
})()

