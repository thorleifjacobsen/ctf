# Challenge

So if you remember reading Santas blog, Santa has taken up coding!

His first attempts didn't go so well, but now he finally created his own funny compiler!

Have a go here:

http://santascodeconsole.norwayeast.azurecontainer.io:8192/

> **Hint:** I wonder what we are looking at here John...

# Writeup

Not sure the reference to John, but I see that sending an empty response gives `NaN` 

🏤🍎🏤

Seems like it replaces repeating number with the quantity and then the number. So e.g. `1111 = 41`. Another example: `112344411 = 21 12 13 34 21` (I've added spaces for readability).

Newlines seems to break it.

Adding any character then a number seems to work, e.g `x1` gives `1x11`

Overflowing the data results in 413: 

```javascript
PayloadTooLargeError: request entity too large
    at readStream (/app/node_modules/raw-body/index.js:156:17)
    at getRawBody (/app/node_modules/raw-body/index.js:109:12)
    at read (/app/node_modules/body-parser/lib/read.js:79:3)
    at jsonParser (/app/node_modules/body-parser/lib/types/json.js:135:5)
    at Layer.handle [as handle_request] (/app/node_modules/express/lib/router/layer.js:95:5)
    at trim_prefix (/app/node_modules/express/lib/router/index.js:328:13)
    at /app/node_modules/express/lib/router/index.js:286:9
    at Function.process_params (/app/node_modules/express/lib/router/index.js:346:12)
    at next (/app/node_modules/express/lib/router/index.js:280:10)
    at expressInit (/app/node_modules/express/lib/middleware/init.js:40:5)
```

Which helps telling me that this is all NodeJS based. I already thought so based on the `NaN` output earlier. After a bit of digging another wild coop appears and we're lead to `John Conway`. So looking at the conway sequence on dcode.fr it is exactly what we get here. But what now? 

My coop player here went so far to just continue the sequence. Data in -> data out. And keep it going until a flag appeared. I'm not sure how many times but the number ended up beeing huge.

```
💰🔒🍇💬🏤🍒💬🍇🔻🤪🍑🤑🏏🔻😈🍇🔻👾🍑🍓🚡🍇🔻😈🔻🤪🔻🍑🎢🤑🏏🙈🤑🤪🍑🤑🏏❕🔓
```

So running this through a reverse decoding function I made and I got the flag:

```javascript
// This map was stolen from the website
const map = { "1": "🎅", "2": "removed rest for readability" };
const flag = "<FLAG INSERTED HERE";
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
```

`${5@N7@5_C0DE_I5_B06U5_I_C_0xDEADC0DE!}`