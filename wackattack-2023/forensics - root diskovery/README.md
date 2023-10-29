# Root Diskovery (easy)

Good job on uncovering the users secret. I think the server administrator has been up to something as well, but I can't find his password?

author: taschmex

(Flag format: wack{PASSWORD})

Download: http://ctf.wackattack.eu/static/diskovery.img.gz (Same as diskovering users)

# Writeup

Guessing they want me to find the root password. So a quick [google](https://erev0s.com/blog/cracking-etcshadow-john/) shows me how to do it.

As i've already mounted it I go into `/etc` and copy out the `shadow` and `passwd` files out. 

Unshadow the files according to the guide and end up with this root entry:

```
root:$y$j9T$CYRX2gVi0eP83WH7Ik0hS1$Fh6TdDMOY1BLNPuPot3iV1ssryYLC.KlkPCOPqxeARA:0:0:root:/root:/bin/bash
```

Using John to crack it I get a error: 

```bash
└─$ sudo john --wordlist=/usr/share/wordlists/seclists/Passwords/500-worst-passwords.txt unshadowed.txt
Using default input encoding: UTF-8
No password hashes loaded (see FAQ)
```

A quick [google](https://superuser.com/questions/1684358/john-the-ripper-on-kali-linux-it-outputs-no-password-hashes-loaded) shows me I need to specify a format and Now it seems to work:

```bash
└─$ sudo john --format=crypt unshadowed 
Using default input encoding: UTF-8
Loaded 1 password hash (crypt, generic crypt(3) [?/64])
Cost 1 (algorithm [1:descrypt 2:md5crypt 3:sunmd5 4:bcrypt 5:sha256crypt 6:sha512crypt]) is 0 for all loaded hashes
Cost 2 (algorithm specific iterations) is 1 for all loaded hashes
Will run 16 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 94 candidates buffered for the current salt, minimum 96 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
buster1          (root)     
1g 0:00:00:21 DONE 2/3 (2023-10-26 23:28) 0.04608g/s 506.0p/s 506.0c/s 506.0C/s tapanis..poohbear1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

# Flag

```
wack{buster1}
```