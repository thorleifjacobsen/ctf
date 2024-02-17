# noob2

Our flag was stolen once again. This time we think they have `hidden` it. Can you get it back for us?

You can connect to the server with the following command: nc uithack.td.org.uit.no 6001

The username is `noob2`

The password is the flag you found in `noob1`

Read up on the `ls` command to get the flag

`nc uithack.td.org.uit.no 6001`

# Writeup

Same as with noob1, connected and used `ls -lah` to see a `.secret` folder. Using `ls -lah .secret` shows the content and we can `cat .secret/*.txt` to print all text files in there.

```bash
$ nc uithack.td.org.uit.no 6001
Username: noob2
Password: UiTHack24{7h3_1337357_0f_3m_4ll}
Logged in! Use 'exit' to logout
Here is your shell!

login
ynetd
ls -lah
total 64K
drwxr-xr-x 1 root root 4.0K Feb 15 10:07 .
drwxr-xr-x 1 root root 4.0K Feb 15 10:07 ..
-rwxr-xr-x 1 root root  220 Jan  6  2022 .bash_logout
-rwxr-xr-x 1 root root 3.7K Jan  6  2022 .bashrc
-rwxr-xr-x 1 root root  807 Jan  6  2022 .profile
drwxr-xr-x 1 root root 4.0K Feb 15 10:07 .secret
-rwxr-xr-x 1 root root  17K Feb 15 09:44 login
-rwxr-xr-x 1 root root  19K Feb 15 09:44 ynetd
ls -lah .secret 
total 12K
drwxr-xr-x 1 root root 4.0K Feb 15 10:07 .
drwxr-xr-x 1 root root 4.0K Feb 15 10:07 ..
-rwxr-xr-x 1 root root   53 Feb 15 09:44 flag.txt
cat .secret/*.txt
UiTHack24{7h3r3_1s_n0_h1ding_fr0m_7h3_1337_0f_3m_4ll}
```