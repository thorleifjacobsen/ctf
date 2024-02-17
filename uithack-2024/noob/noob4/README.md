# noob4

Our trip through space and time seems to have messed with the future, and now we cannot access our flag!

You can connect to the server with the following command: `nc uithack.td.org.uit.no 6003`

The username is `noob4`

The password is the flag from `noob3`

`nc uithack.td.org.uit.no 6003`

# Writeup

The problem here is that there is a dash in front, so using `cat -flag.txt` seems to add the paramteres `-flag.txt` to the command. The workaround according to google was to use `cat -- -flag.txt`. This gave me the output from the first file. Then I tried `*.txt` but that did not work either. After a while I found that I could get the `inode` number for it and use find for that number to execute cat on it.

```bash
ls -i
3025685 -flag.txt
3025686 -flag.txt 
3025690 login
3025691 ynetd
find . -inum 3025686 -exec cat {} \;
UiTHack24{d4sh_31337}
```

The description was updated later on to tell us there was a space in the name. That explains it, the fix would have been:

```bash
cat -- *flag*
```
