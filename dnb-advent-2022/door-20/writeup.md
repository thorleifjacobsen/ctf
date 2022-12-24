# Challenge

# Writeup

Quickly understood the point was to get many points. So in Chrome's inspector I opened the script.js and modified it to send "999999999999999999999" on both requests in every field. 

The first field is my score, second field is also the score basically. Third field is number of spawned astroids. So they must be all equal to get a price. Having all with 9's gives a perfect score. Not a single missed bullet.

The request now put a new cookie to my browser, a price! 

```json
{
  "set-cookie": [
    "prize=%2Fflag%3Fsig%3DhyC3XdiUJrv16HNN3CN5ZaKjDYJFba9kCeNJ7Ew%2FkrtRaObQAhbKIwhugX21Ky58mkJQylS%2Fb33rS6ptxqEnumHyHMobOHzeo8ZILC8lH9%2FyIlw2X2iioabO1iOjxOR4GVDFjQb0%2BWLvS8yyycPMmfuCDU3O70O85TvypHiolQLiqv8LbFcInQZOk0WloMnlsAidqNlvUBuOBWbdfABc4ZN3rvyd%2B6yHdiT5lY6oKMMQXDyxygA6hVMsiX5jyg7ubxuC%2BLkAtXRNei0lL9nDNffOnmgy1qDZWt2N0Jf9%2FYzjE5%2B4jWFEgzJr5GUsTyT6YDqVlF%2Bo8rPtIzA2tEPK2%2BfzP%2FH82GLrsAK7QlxMN2Ova3yexi%2BlXjr4sn1O5WYyVlsPOTvciDQxt7If2tDrMTmvXolx2tCFktycZPq%2FTuQfVC%2FAwwyPXLSJxnvlGJgEd35%2BBNo3DAAIsL5KZTiRbIRA07jL15kJPBGAgvKIB0gm7t9q%2FRjHhxqCASCX0yGW; Path=/"
  ]
}
```

The price consists of a new url. The whole thing is urlencoded so I decode it and paste it in.

"Nope..."

After a quick break I get a so called "Aha-Opplevelse".. There are characters in that flag after urldecoding which will be different received from the browser. I need to urlencode the sig value.

There! A big freaking string.. Looks like base64, decoding it gives a whole lot of `()[]=`. Oh, this is JSFuck all the way! 

Heads over to browser console. Pastes the code, error in code!

```javascript
VM445:3 Uncaught ReferenceError: Buffer is not defined
    at eval (eval at <anonymous> (flag:1:383), <anonymous>:3:12)
    at <anonymous>:1:596838
```

Clicks the VM445:3 link to get the source of the JSFuck code:

```javascript
(function anonymous(
) {
let data = Buffer.from('JHtXMFZfWTBVX0pVNTdfQlIwSzNfNzQzX1cwUjFEX1IzQzBSRCEhIX0=','base64');console.log(data.toString('ascii'));
})
```

Shows a base64 string, then I run that through a decoder:

```bash
JHtXMFZfWTBVX0pVNTdfQlIwSzNfNzQzX1cwUjFEX1IzQzBSRCEhIX0=

decodes to

${W0V_Y0U_JU57_BR0K3_743_W0R1D_R3C0RD!!!}
```