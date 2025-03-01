# noob4

Shit! The constant back and forth with the flag has corrupted it. I'm trying to read it, but it just doesn't work!
You can connect to the server with the following command `ssh noob4@uithack-2.td.org.uit.no -p 6003`
The password is the flag from the previous noob challenge.
Use command `exit` to disconnect from the server when you are done.


# Writeup

```bash
noob4@508ba65e23b6:~$ ls -lah
total 28K
-rw-r--r-- 1 root root   18 Feb 23 17:08  -flag.txt
-rw-r--r-- 1 root root   26 Feb 23 17:08 '-flag.txt '
drwxr-xr-x 1 root root 4.0K Feb 23 17:08  .
drwxr-xr-x 1 root root 4.0K Feb 23 17:07  ..
-rw-r--r-- 1 root root   12 Feb 23 17:08  flag.txt
noob4@508ba65e23b6:~$ cat "../noob4/-flag.txt "
UiTHack25{D45h1ng_5ki11s}
```

# Flag

```
UiTHack25{D45h1ng_5ki11s}
```