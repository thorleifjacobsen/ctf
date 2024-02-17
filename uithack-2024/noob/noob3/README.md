# noob3

Oh no! Someone deleted `flag.txt` from our system, and our spaceship is broken, so we are not able to go back in `history` to retrieve it.

You can connect to the server with the following command: `nc uithack.td.org.uit.no 6002`

The username is `noob3`

The password is the flag from `noob2`

Read up on how Linux stores the bash history to get the flag.

`nc uithack.td.org.uit.no 6002`

# Writeup

In this one they hint towards the history, so I just cat `.bash_history` to find the flag.

```bash
$ nc uithack.td.org.uit.no 6002
Username: noob3
Password: UiTHack24{7h3r3_1s_n0_h1ding_fr0m_7h3_1337_0f_3m_4ll}
Logged in! Use 'exit' to logout
Here is your shell!

login
ynetd
cat .bash_history
cd ..
cd ..
ls
clear
id
uname -a
clear
cd ~/
ls -al
echo "UiTHack24{1337_t1m3_tr4v3ll3r}" > flag.txt
cat flag.txt
exit
clear
ls
cd 
rm flag.txt
rm bash_history
ls
```