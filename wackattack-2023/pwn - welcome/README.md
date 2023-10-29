# Welcome (beginner)

Welcome! Enjoy pwning!

Author: krloer

nc 20.100.141.224 1033

# Writeup

Quickly netcat to the server and we see the following:

```
Welcome to pwn!!!!
What would you like to say? (no more than 28 characters please)
```

Must be a overflow thing. pasting a lot of characters and press enter and I get:

```
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
Oh you are a ctf admin? Here you go:
wack{h4v3_fun_4nd_br34k_stuff}
```

To explain how this work look at the source code for the welcome binary running:

```
setbuf(stdout, NULL);
char buf[28];
int admin = 0;
```

It creates a buffer of 28 characters in memory. And in memory right after that buffer they have a admin variable. As they are using `gets(buf);` it does not limit how much you can write to memory. So if you write more than 28 characters you will start overwriting the admin variable. So if you write 28 and a 1 the admin variable will be set to 1 and you will get the flag.

# Flag

```
wack{h4v3_fun_4nd_br34k_stuff}
```