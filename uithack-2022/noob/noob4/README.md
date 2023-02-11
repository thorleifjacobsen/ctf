# Noob4

Title says it all. Help Eminem find mom's spaghetti!

The username for this , is noob4.
The server name is wwww.limewire.td.org.uit.no.
Password is noob3's flag

# Writeup

Dang, lots of files. I used find to run strings on all and grepped for UiTHack

```shell
noob4@limewire:~/flag$ find ./ -type f -exec strings "{}" \; | grep UiTHack
His palms are spaghetti, weak sweater, are heavy. There's vomit on his knees already, mom's sweaty flag. UiTHack23{m0m'55p46h3771}
```