# View Access

Can you figure out how to get some access?

http://rsxc.no:9002

# Writeup

Getting a redirect to `index.php?a=viewAccess` where it says `There is no access for you`. Guessing we need to find the correct keywoard in the `a`. To find it there must be something. So I dirbusted the website only to find `/icons/small/`.

I then tried a whole lot of combinations of `xAccess`. 

```
rootAccess
giveAccess
fullAccess
adminAccess
writeAccess
superUserAccess
flagAccess
flag.txt
flag
```

I tried a whole lot of Path Traversal techniques. None of them work.

I then gave up, the variable can be `anything` without any hint. So I started  bruteforcing the website using gobuster I put `rockyou.txt` on `?a=FUZZ`. Then I put some more common words on `?a=FUZZAccess` and there I found the correct `grantAccess`

```console
toffe@kali:~$ gobuster fuzz -u http://rsxc.no:9002/index.php?a=FUZZAccess -w /usr/share/wordlists/dirb/common.txt -b 302,400 
===============================================================
Gobuster v3.3
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://rsxc.no:9002/index.php?a=FUZZAccess
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Excluded Status codes:   302,400
[+] User Agent:              gobuster/3.3
[+] Timeout:                 10s
===============================================================
2023/04/01 15:12:29 Starting gobuster in fuzzing mode
===============================================================
Found: [Status=200] [Length=1229] http://rsxc.no:9002/index.php?a=grantAccess

Found: [Status=200] [Length=1378] http://rsxc.no:9002/index.php?a=viewAccess

Progress: 4554 / 4615 (98.68%)
===============================================================
2023/04/01 15:12:53 Finished
==============================================================
```

If I only knew how close I was with `giveAccess`.. 

# Flag

```
RSXC{FUZZING_VERBS_FOR_SUCCESS}
```