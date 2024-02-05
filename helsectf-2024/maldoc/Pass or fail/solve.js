const fs = require('fs');
let data = fs.readFileSync('pass_or_fail.bat', 'utf8');
const knownVariables = {
    'public': "C:\\Users\\Public",
}

// Helper function to identify and find variables.
const parseBatchVariables = (data) => {
    let resultText = '';

    for (let i = 0; i < data.length; i++) {
        if (data[i] == '%') {
            let nextIndex = data.indexOf('%', i+1);
            if (nextIndex == -1) return data;

            let extracteData = data.substring(i+1, nextIndex);
            if (extracteData.includes(':~')) {
                const [variable, substring] = extracteData.split(':~');
                const [start, end] = substring.split(',').map((x) => parseInt(x));
                const res = knownVariables[variable] ? knownVariables[variable].substr(start, end) : match;
                resultText += res;
                i = nextIndex;
                continue;
            }


            if (knownVariables[extracteData]) {
                resultText += knownVariables[extracteData];
                i = nextIndex;
                continue;
            }
        }

        resultText += data[i];
    }
    
    return resultText;
}

const lines = data.split('\n').map((line, idx) => {
    if (idx == 0) { console.log(line); }
    line = parseBatchVariables(line, idx == 0);

    if (line.includes('set "')) {
        const [variable, value] = line.substring(line.indexOf('set "')+5, line.lastIndexOf('"')).split(/=(.*)/s);
        knownVariables[variable] = parseBatchVariables(value);
    }

    return line
});


fs.writeFileSync('pass_or_fail_2.bat', lines.join('\n'));