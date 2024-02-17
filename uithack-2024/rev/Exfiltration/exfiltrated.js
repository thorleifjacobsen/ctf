const enc_flag = "3c3d1c29020859064f115e4242471011434147686e046a3e0f316b585d540b3133585a09124153544e7d";
const _0x6ee0 = "never gonna give you up";
const _0x10fafd = "never gonna let you down";

function _beard(_0xed, _0xca, _0xbea_) {
    return (_0xed["ch" + _0x6ee0[10] + "rC" + _0x10fafd[21] + _0x10fafd[20] + "eAt"](_0xbea_) ^ _0xed["ch" + _0x6ee0[10] + "rC" + _0x10fafd[21] + _0x10fafd[20] + "eAt"](_0xbea_+1 % _0xca)).toString(0x10).padStart(0b10, "0");
};

const _0x1695 = (_0xde) => {
    let _0x10bc = ['What\x20is\x20the\x20flag?\x20', '1448386GEOWEF', '1783000ecBLBo', 'Correct!', 'o', '25cMJKVA', '1112876yryjDY', '14NiBVWH', 'question', 'length', 'charCodeAt', '801VWpneM', 'log', '105140VZfvyP', 'readline', '2463672KMPYgA', '2498096OxrSLX', 'stdout', '4472832SmweuI', 'console', 'Wrong!'];
    return _0x10bc[_0xde];
};

const forEach = _0xab904564 => {
    let _0xa = "";
    for (let _0xbecfade = 0x0; _0xbecfade < _0xab904564[_0x1695(0x9)]; _0xbecfade++) {
        _0xa += _beard(_0xab904564, _0xab904564[_0x1695(0x9)], _0xbecfade);
    }
    return _0xa;
};

const _aldk = (_0x12e, _0x12f) => {
    const _0x1697 = () => {
        return console[_0x10fafd[12] + _0x1695(0x04) + _0x6ee0[0b00110]];
    };
    return _0x1697;
};

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('What is the password? ', (_ab1d2f3) => {
    const _a0be = _aldk(0x68, 0x1)();
    forEach(_ab1d2f3) === enc_flag ? _a0be(_0x1695(3)) : bl_3(_0x1695(20)), rl["close"]();
});
