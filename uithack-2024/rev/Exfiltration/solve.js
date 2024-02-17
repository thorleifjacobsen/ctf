const _0x6ee0 = "never gonna give you up";
const _0x10fafd = "never gonna let you down";



function _beard(_0xed, _0xca, _0xbea_) {
    return (_0xed["ch" + _0x6ee0[10] + "rC" + _0x10fafd[21] + _0x10fafd[20] + "eAt"](_0xbea_) ^ _0xed["ch" + _0x6ee0[10] + "rC" + _0x10fafd[21] + _0x10fafd[20] + "eAt"](_0xbea_ + 1 % _0xca)).toString(0x10).padStart(0b10, "0");
};

const _0x1695 = (_0xde) => {
    let _0x10bc = ['What\x20is\x20the\x20flag?\x20', '1448386GEOWEF', '1783000ecBLBo', 'Correct!', 'o', '25cMJKVA', '1112876yryjDY', '14NiBVWH', 'question', 'length', 'charCodeAt', '801VWpneM', 'log', '105140VZfvyP', 'readline', '2463672KMPYgA', '2498096OxrSLX', 'stdout', '4472832SmweuI', 'console', 'Wrong!'];
    return _0x10bc[_0xde];
};

const forEach = password => {
    let retString = "";
    for (let i = 0x0; i < password[_0x1695(0x9)]; i++) {
        retString += _beard(password, password[_0x1695(0x9)], i);
    }
    return retString;
};

const _aldk = (_0x12e, _0x12f) => {
    const _0x1697 = () => {
        return console[_0x10fafd[12] + _0x1695(0x04) + _0x6ee0[0b00110]];
    };
    return _0x1697;
};



let flag = "UiT";
let characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!#$%&'()*+,-./:;<=>?@[]^`{|}~";
const enc_flag = "3c3d1c29020859064f115e4242471011434147686e046a3e0f316b585d540b3133585a09124153544e7d";
let foundEnd = false;
while (!foundEnd) {
    for (let x = 0; x < characters.length; x++) {
        for (let y = 0; y < characters.length; y++) {
            let testFlag = forEach(flag + characters[x] + characters[y]);
            // console.log(`Testing: ${flag + characters[x] + characters[y]} => ${testFlag}`);
            testFlag = testFlag.substring(0, testFlag.length - 2);
            if (enc_flag.startsWith(testFlag)) {
                // Match letter   
                flag += characters[x];
                console.log(`Flag: ${flag}`);
                
                if (flag.length == enc_flag.length/2-1) {
                    console.log(`Flag: ${flag}}`);
                    foundEnd = true;
                }
                break;
            }
        }
    }
}