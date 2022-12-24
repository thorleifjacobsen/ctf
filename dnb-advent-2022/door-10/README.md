# Challenge

So I managed to get a hold of my sister's wishlist! But it seems to be encrypted by something. Maybe she used the wishlist tool from Santa's github page? I compiled it for you here...

https://htbbinaries.z1.web.core.windows.net/re-santa-3

oh yeah, the wishlist...

https://htbbinaries.z1.web.core.windows.net/mywishlist.txt

> **Hint:** So this should be easier than driving a radio controlled car right?

# Writeup

Started with a simple strings on the binary, it dumped the following of interest.

```
ItsBeg1n1ngT0L00kL1keChr1stmas
L3tItSn0w!
Jing3B3lls#!
RudolphTheRaind33r_!
S3cret12=
Q2FuVGhlR3JpbmNoSGFjaz8=
NoNoMrGrinch!
```

Opened Ghidra to look at the binary and found quickly it was some sort of encryption script just as the task told us. 

I started a many hour long progress of decompiling the source to create tthe encryption script. But after 3-4 hours I was tired and went to bed. As usuall, with new eyes comes new ways.

I made a quick nodejs script `read-file-binary.js` to get the binary value of the encrypted wishlist:

```bash
Encryption of: Secret Flag
1f 9e e2 e2 9e a3 d8 9a 48 c4 ab 2e 3a 24 ee 8f 68 a5 9d ad 46 3a 85 5a f8 d5 4e b3
```

I quickly encrypted a test text "test" and got these values:

```bash
Encryption of: test
4f 80 c6 a7
```

I thought maybe I could encrypt `${test}` to see the values, surely I got `1f 9e c1 b6 d8 e3 92`. It seems to me that the first two are `${` but the others are changed. Do they change depending on the length as I can see in the binary that this is a factor. So if I do `${28charaters}` then add enough characters to match the original file?

```bash
Encryption of: ${abcdefghijklmnoprstuvwxyz} 
1f 9e d4 b1 c8 f3 8a cd 1a 9b 9d 75 64 17 c0 d1 6a a5 9d ee 5f 26 c6 1e e4 96 1c b3
```

Seems like we got `}` as `b3`. Now can I just bruteforce this. Lets decode more, we got a-z. But is a the same everywhere?
 
```bash
Encryption of: ${aaaaaaaaaaaaaaaaaaaaaaaa} 
1f 9e f4 91 e8 d3 aa ed 3a bb bd 55 44 37 e0 f1 4a 85 bd ce 7f 6 e6 3e c4 b6 3c b3
```

No, this means positions matters.. Can I just do this for every letter to find the character matching that posistion? Lets write a bruteforce script. And here we go:

```bash
┌──(toffe㉿kali)-[~/Projects/dnb-julekalender-2022/door-10]
└─$ node bruteforce.js 
${W
${W1
${W15
${W154
${W1547
${W15471
${W154715
${W1547157
${W1547157_
${W1547157_1
${W1547157_15
${W1547157_15_
${W1547157_15_C
${W1547157_15_C0
${W1547157_15_C0m
${W1547157_15_C0mp
${W1547157_15_C0mpr
${W1547157_15_C0mpr0
${W1547157_15_C0mpr0m
${W1547157_15_C0mpr0mi
${W1547157_15_C0mpr0mi5
${W1547157_15_C0mpr0mi53
${W1547157_15_C0mpr0mi53d
${W1547157_15_C0mpr0mi53d:
${W1547157_15_C0mpr0mi53d:(
${W1547157_15_C0mpr0mi53d:(}
```

Bingo!! This was easier than doing the damn decompiling and rewriting the function.