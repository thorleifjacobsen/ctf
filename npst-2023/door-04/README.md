# Pinneved

Alvebetjentene på Jule NISSEN sitt verksted våknet i dag til et fryktelig syn; Julenissens slede er sprengt i fillebiter. Vi har satt folk på saken for å finne ut av hvem som er ansvarlig for ødeleggelsen, men det er kritisk at sleden blir reparert slik at vi får testet den før Jule NISSEN skal levere pakkene.

Alvebetjentene har samlet vrakrestene, samt verktøyet de mistenker at sabotørene har brukt.

Vi trenger at du rekonstruerer sleden så fort som mulig!

- Tastefinger

📎 [pinneved.py](./pinneved.py)<br />
📎 [pinneved.txt](./pinneved.txt)

# Writeup

Seems like a reversing the python script is the way to go. I start by looking at the `pinneved.py` file. The action starts here and need to be reversed here:

```python
bang = explode(slede, 24)
eksplosjon = [''.join([chr(ord(c) + 2) for c in fragment]) for fragment in bang]
pinneved = [str(eksplosjon[i]) for i in reversed(otp)]
```

Starting with the explode function. It seems to split the data into a number of parts, and then return the parts in a list.

```python
def explode(input, antall):
    størrelse = len(input) // antall
    fragmenter = []
    
    for i in range(0, len(input), størrelse):
        fragment = input[i:i+størrelse]
        fragmenter.append(fragment)
    
    return fragmenter
```

Then they scramble the data by changing the ascii value of each character by 2. This is done by looping through each character in each fragment and adding 2 to the ascii value.

```python
[''.join([chr(ord(c) + 2) for c in fragment]) for fragment in bang]
```

Then using the `otp` list they set the order of the fragments to the position given there. But reversed.

```python
otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15]
[str(eksplosjon[i]) for i in reversed(otp)]
```

I'll use javascript as this has indexes for arrays so I can easily reverse the order of the fragments.

```javascript
// Load values from file:
const fs = require("fs");
let data = fs.readFileSync("pinneved.txt", "utf-8");

// Parse data:
const otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15].reverse();
const parts = data.match(RegExp(`.{1,${Math.ceil(data.length / otp.length)}}`, 'g')) || [];

// Reverse the `ascii` values of each character in each fragment:
let reversedFragments = parts.map(fragment => {
  return fragment.split('').map(c => String.fromCharCode(c.charCodeAt(0) - 2)).join('');
});

// Rebuild the fragments in the correct order:
const rebuildFragments = [];
for (let i = 0; i < otp.length; i++) {
    rebuildFragments[otp[i]] = reversedFragments[i];
}

// Print the result:
console.log(rebuildFragments.join(''));
```

Running this gave me [slede.txt](./slede.txt) which contains the flag as ascii art:

# Flag

```
PST{ASCII_art_er_kult}
```