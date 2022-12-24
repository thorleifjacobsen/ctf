# Challenge

Ok, so DJ Santa has gotten a guest artist to contribute to his yearly Christmas Rave Party. DJ Oiler has created this hot track for your enjoyment! But what can you do with this ting?

Well here is the track at least...

https://htbbinaries.z1.web.core.windows.net/dj-oilers-theme.mp3

Hint: `Sing it! Crypto stego constant pain!`

# Writeup

Downloaded the above MP3 and looked at spectrogram, but it seems far fetched as we just had this kind of task 3 days ago. Also this has no logic in it.

Sound of the file made no sense to me.

8 beats repeated 4 times, then a swap, and repeat 2 times.
So total of 3x 32 beats. 

Exiftool shows some interesting data:

```
Artist URL                      : aHR0cDovL2Rqb2lsZXJsb2NrLm5vcndheWVhc3QuYXp1cmVjb250YWluZXIuaW86MjY3NC8=
Popularimeter                   : Windows Media Player 9 Series Rating=255 Count=0
Band                            : DJ Oiler
Conductor                       : 3fe1406a8254afd471de2bdd53483501f947004cd3d174e6a607648638ae1a3e
Initial Key                     : C Major
```

```
Artist url is base64 of : http://djoilerlock.norwayeast.azurecontainer.io:2674/
Conductor is a sha256 of "interval" 
Initial Key: [C Major](https://en.wikipedia.org/wiki/C_major)
```

Seems like that website takes 3 keys, reading the script it will allow you to unlock one by one. So inputing the correct key and pressing it will go green. But the backend replies with false / true based on it it is correct key or not..

Thinking to make a quick bruteforce app, so I start a little, starting from a -> zzzzzzzz. Figures out this will take months with the 2 second delay and the key is prolly 32 characters or 8 minimum so I toss that thought away. Might also be 1337 speak. 

It seems like the 3 segments of the Mp3 file (32 * 3 beats) is a part of the 3 locks. So 32 beats for each lock we need to decode.

After multiple hours of attempting stuff I try decoding the first 8 beats as notes:

```
  E C F C G D D A
```

Nothing matched, tried it 4 times in a row, alone e.t.c. Nothing. Giving up on this idea a little while. Now looking for other steno challenges. Did not find any, something got me to see on Leonhard Euler. He had Consonances which sounds good together and Dissonances which sounds bad. Reference to "Constant" and "Pain"? 

https://www.youtube.com/watch?v=B6Dvfv_ASVg
https://www.uni-miskolc.hu/~matsefi/Octogon/volumes/volume1/article1_25.pdf

ChatGPT tries to help me and drowns me with musical theory and leonard eular math. Totient and god knows what. Nothing works.

Sing it can refer to "do ro mi..." thingy.. (Google calls it Numbered musical notation](https://en.wikipedia.org/wiki/Numbered_musical_notation)) So doing that on the ECFCGDDA I get the following:

```
Note:	C	D	E	F	G	A	B
Solfège:	do	re	mi	fa	so	la	ti
Notation:	1	2	3	4	5	6	7
```
becomes:
```
mi do fa do so re re la
3  1  4  1  5  2  2  6
```

Try to input that, 1 time, 4 times, in all fields. With spaces, no spaces, nothing. NOTHING!.

Learns about [intervals](https://www.omnicalculator.com/other/music-interval)

```
  E-C = Major third (semi: 4, tones: 2)
  C-F = Perfect fourth (semi: 5, tones: 2.5)
  F-C = Perfect fourth (semi: 5, tones: 2.5)
  C-G = Perfect fifth  (semi: 7, tones: 3.5)
  G-D = Perfect fifth  (semi: 7, tones: 3.5)
  D-D = Perfect octave (semi: 12, tones: 6)
  D-A = Perfect fifth  (semi: 7, tones: 3.5)

  (gap between last of the 8 and the first of the next 8)

  A-E = Perfect fourth  (semi: 5, tones: 2.5)
```

Adding this together makes

```
4+5+5+6+6+12+7+5+4+5+5+6+6+12+7+5+4+5+5+6+6+12+7+5+4+5+5+6+6+12+7 = 195
```

195 does not work. Removing all + not  working, only taking the first 8 no dice. Try tones instead of semi, nooope.. Twist, turn, play and have fun.

I've also nearly daily been down many rabbit holes, math formulas, scripts, xor, who knows what. 
# Breakthrough

I'm working in a software development company, and they are bright people. So I did a last attempt and told them about the task. One of the many geniuses only took a few minutes before he came to me. "Got it"..

He then calculated the interval from the Major C scale to each note. So the first one were "31415926" which is the first digits of PI. So he entered the word pi in and got a match!

To explain this, the scale goes from: C, D, E, F, G, A, and B. So counting the C we can start with E4 the first tone. That is C + D + E = 3 in interval. Next is C which is 1. Then we have F which is C+D+E+F = 4 tones interval.  So there we have 314 (start of Pi). With the higher D5 we have to roll around and we get 9. I am guessign the Major C means starting with C4. so from C4 to C5 there is 8 notes. Then to D there is 1 more so 9. But dont take my word for this.

So we suddenly understood the hint "constant" .. These are mathematic constants. So we googled and found a few and quickly tested one of them "e".. What, a green lock. Only one to go!

I started continuing on my bruteforce code, it sounded more realistic to make it now with so short words. How long can a consonant be? But my collegue did listen to the notes and a few minutes later he wrote "Tau" to me.. And yes, there it was.. 

If I just did what I wanted to do the very start, start a bruteforcing. How long time would that take before I got it.

I would start with A-Z anyway.. 

So I would send in "a,a,a" then "b,b,b". only 5 attempts I would get `true` on the middle one. So basically 10 seconds (2second request delay) would give me more information than the hint ever would. 

Just for fun, the math to how long it would take to get true on all with a single thread.


```
a-z = 26 * 2sec = 52 seconds = 1 minute
aa-zz = 650 * 2sec = 1300 = 22 minutes 
aaa-zzz = 17576 * 2sec = 35152 sec = 586 minutes = 9.7 hours
```

So if I just started that damn 🔨 script I started on I would have gotten the answer within under 9 hours as tau is the furthest down the 3 letter bruteforce but not at the bottom. I regret not trying..

The request returned true, true, true + one object:

```json
[
    true,
    true,
    true,
    {
        "type": "Buffer",
        "data": [ 36, 123, 55, 52, 64, 55, 95, 49, 53, ... ]
    }
]
```
Quicky copied the array in the nodejs. `Buffer.from(dataValue).toString()` gave me:

```
${74@7_15_5uM_K3wL_c0n57@n7_7un35!}
```
# To sum up

DJ Oiler - sound like Euler which in terms is the same as a mathematician with connection to music. Euler's number is "e" which is the second part of the piece.

Sing It! - No idea
Constant - All are constants in math
Pain - could be "pai", "pi" which is the first key?

## Not related, just sent a whole lot of data to reveal backend. NodeJS

```
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
    at serveStatic (/app/node_modules/serve-static/index.js:75:16)
```

# Here is the start of my hammer script

I've finished the script, so all but the text between the comments below were done on the 11th december. I just stopped because I thought it would not be that easy. "If it sounds too good to be true, it most likely is!" 

```javascript
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
```

# Example run:

```bash
$ node hammer.js 
No dice: a,a,a
No dice: b,b,b
No dice: c,c,c
No dice: d,d,d
GOT TRUE: false,true,false on e,e,e
No dice: f,f,f
No dice: g,g,g
No dice: h,h,h
No dice: i,i,i
No dice: j,j,j
No dice: k,k,k
```