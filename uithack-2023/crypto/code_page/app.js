const cptable = require('codepage');
const fs = require('fs');

// process.stdout.write(cptable.utils.decode(21027, "UiTHack"))

const fileContent = fs.readFileSync('./file1', 'utf8')
console.log(cptable.utils.encode(21027,fileContent).toString());
