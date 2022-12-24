# Challenge

See if you can figure out to get Santa's present early...

http://santaspresents.norwayeast.azurecontainer.io:4200/

> **Hint:** Well passwords are obsolete right?

# Writeup

I first check the source. Simply enough there is a comment in there

`<!--- 92706446560948009279782559541942421090352568584109452582172344770401293930185 -->`

I guess this is something I should understand? Well entering that wont work, but it takes me to a URL I can easily script towards:

`http://santaspresents.redactedurl.io:4200/password?password=92706446560948009279782559541942421090352568584109452582172344770401293930185`

So looking at the category this door has it is marked as "Crypto", so I guess I need to decode that string of numbers.

But how? you might ask.. Well I ask that too.. Lets see:

* Is odd number so not a 2 pair thing
* No visible pattern
* Cant be T9 typing with the 1's in there.
* Length is 77, which is divisible on: 7, 11 
* Bits/bytes 

```
7 digits
9270644
6560948
0092797
8255954
1942421
0903525
6858410
9452582
1723447
7040129
3930185

11 digits
92706446560
94800927978
25595419424
21090352568
58410945258
21723447704
01293930185
```

This makes no sense, my friend took it in a hex converted and told me that was exactly 64 letters. So we starte playing with that as a potensial solution.

```CCF5FD41EC247019BE2A322FDE33EB923A7CD3405D119A92A4BAAC7815218EC9```

I tried to do many things with this, pasted it into the cipher identifier https://www.dcode.fr/cipher-identifier

It shows that it could be a ascii shift identifier og sha256 and many more. I saw this and recognized it, if I just lowercase it it looks exactly like sha256. I opened it in CrackStation and pasted it in. Pressed I'm not a robot and hoped for gold. But, nothing! I was so tired and had to start all over again. This was 20:40.

I then started to ask if someone wanted to coop on this. Got a match and we started, I was told to look at the tool page, which I dont understand the only thing they point to is CrackStation and I've already done it.

I tried again as I'm desperate, this time it worked! I got the password IAmInvincible! Why??? Oh, I know why.. My other tab shows that I pasted the decimal number and not the hex! I litteraly cursed at my screen as the time is now 21:40. An hour after. Why did I not double check the paste?

Oh well, atleast I'm at the second stage. Now we had a lot of plans here. 

- CRC32 bruteforce. Checksum for flag.txt is 0xfe4b1a98, we know 3 of the characters ${}. So 15 left to go. Generate all possible 15 character possibilities with ${} around and crc32 them. Well, this might take ages? But it would match the hint "Well passwords are obsolete right?"
- Bruteforce, this can take ages.. 
- Dictionary attack (Rockyou?)
- pkcrack

I tried rockyou, I tried bruteforcing password 30-40 minutes. I tried bruteforcing the crc32, it took ages. 

But we always thought. There must be an easier solution? The hint is that passwords are obsolete, right? So we should not need passwords? Well, after a few moments someone got it, and it was a dictionary attack. So I had to try myself, I went for the big boss. CryptoStation.txt at 15 GB.

Bingo! ChristmasEve was here. 

I question a few things here. The hint, I think it misleading as I understood it. Someone understood it right away ofcourse. But my understanding was that you might not need it. But I now understand it was ment to tell you that the passwords are leaked. Using tools page was underestimated. I'll go there for every door in the future.