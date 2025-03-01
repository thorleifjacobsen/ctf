# noob2

The flag has been stolen once more. They learned from the mistake and they have now taken measures to hide it.
You can connect to their server with the following command `ssh noob2@uithack-2.td.org.uit.no -p 6001`
The password is the flag from the previous noob challenge.
Read up on the "ls" command if you are not familiar with it.
Use command `exit` to disconnect from the server when you are done.


# Writeup

```bash
noob2@bd2656671b47:~$ ls -lah
total 24K
drwxr-xr-x 1 root root 4.0K Feb 23 17:08 .
drwxr-xr-x 1 root root 4.0K Feb 23 17:07 ..
drwxr-xr-x 1 root root 4.0K Feb 23 17:08 .secret
noob2@bd2656671b47:~$ cat .secret/flag.txt 
UiTHack25{Hidd3n_but_c4n_b3_Cena}
```

# Flag

```
UiTHack25{Hidd3n_but_c4n_b3_Cena}
```