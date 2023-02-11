# Wizardry

Gryffindor has gotten their flag stolen by another house. Rumour has it that it is hidden behind this spell.
Break the spell to get the flag!

Connect to the server with netcat

$ nc motherload.td.org.uit.no 8005

# Writeup

Given the source code for the software runnning which shows it will print the flag when receiving `sigsegv` which is segfault. So our mission is to segfault this software. Guessing overflow of characters as it is set to max 100 on read. So i just type a lot of crap:

```
└─$ nc motherload.td.org.uit.no 8005
Cast a spell:
>> asdasdj,askjdajskd jkasjkldaslkjdjalksdljkasjlkdasjlkdjklasljkdaslkjdlkjaslkjdalskjdjlkasljkdalskj dljkaslkj djklas jdlkasjlk
asdasdj,askjdajskd jkasjkldaslkjdjalksdljkasjlkdasjlkdjklasljkdaslkjdlkjaslkjdalskjdjlkasljkdalskj UiTHack23{W1ng4rd1um_l3vi0s4aa4}
```

Luck I guess.. Flag is there