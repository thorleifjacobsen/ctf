# noob1

Our flag was stolen from our spaceship, and we need your 1337 hacker skills to get it back for us.

You can connect to the server with the following command: `nc uithack.td.org.uit.no 6000`

The username is `noob1`

The password is `noob1`

Read up on the `cat` command to get the flag

`nc uithack.td.org.uit.no 6000`

# Writeup

Quicky connected and got a `shell`. Could use basic linux commands and it shows `flag.txt` upon connection. So `cat flag.txt` shows the flag.

```bash
$ nc uithack.td.org.uit.no 6000
Username: noob1
Password: noob1
Logged in! Use 'exit' to logout
Here is your shell!

flag.txt
login
ynetd
cat flag.txt
UiTHack24{7h3_1337357_0f_3m_4ll}
```


