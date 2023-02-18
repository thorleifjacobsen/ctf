# Code Page

I fired up my old machine, the whirling and clicking of the hard drive was comforting. I opened up the terminal and typed in the passcode: 2 1 0 2 7 and was greeted with the homescreen. There I found with a weird file, but im no Klingon. Can you help me translate it?

# Writeup

Needed a hint here and the hint mentions `EBCDIC`. This is `an eight-bit character encoding used mainly on IBM mainframe and IBM midrange computer operating systems`

So googling EBCDIC and Code Page 21027 a lot. I found [this archive link](https://web.archive.org/web/20190406193522/https://blogs.msdn.microsoft.com/shawnste/2005/09/12/code-page-21027-extendedext-alpha-lowercase/) which is an old MDN article titled `I'm not a Klingon`. So this matches the task description. 

So after a while I found [codepage npm](https://www.npmjs.com/package/codepage) which I installd with `npm install npm` then made a app.js and tried:

```js
const cptable = require('codepage');
process.stdout.write(cptable.utils.decode(21027, "UiTHack"))
```

Output

```
$ node app.js | xxd -p -c0
efbdadefbdb9efbdacefbda72fefbdb32c

$ xxd -p -c0 file1
efbdadefbdb9efbdacefbda72fefbdb32cefa396efa39723253fefbdbdefbdbec2acefbdb93ec2acefbdbeefbdbc2f3eefbdbd252fefbdbeefbdb93f3e27
```

This confirms we have the codepage, now I can possible use the Encode function?

```js
const cptable = require('codepage');
const fs = require('fs');

const fileContent = fs.readFileSync('./file1', 'utf8')
console.log(cptable.utils.encode(21027,fileContent).toString());
```

Bingo! :) 

```
UiTHack23{lost_in_translation}
```