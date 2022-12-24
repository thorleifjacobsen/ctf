# Challenge

Can you decode this cipher text?

JHtMMEFmcGd4N0tAeDRQMGtAbHh9

> **Hint:** Basic romans...

# Writeup

I've used atleast 3 hours on this. I just went the wrong way on the second part of this task.

I saw the base64 and decoded it, simple I thought. That was all. I had the flag.

`${L0Afpgx7K@x4P0k@lx}`

But it did not accept it. Ok, so basic romans hints to caesars cipher. 

So lets rotate this, I add the special characters, a-z, numbers and everything. Nothing looks correct. Trying +- 100 rotations. Ok nothing, lets convert all to ascii then rotate then convert back? No nothing.

A few hours later I inserted it into [dCode.fr's Caesar Cipher](https://www.dcode.fr/caesar-cipher) and tweaked settings nad tried bruteforce aswell. Nothing made sense. 

Giving up a while, a collegue at work finds something with `rot2`. 

```${N2Chriz9MBz6R2mBnz}```

And I'm like, YEAH! Christmas.. Weird text but ok. But short lived. It was wrong!

Later that evening i tried again on dCode.fr and pasted `L0Afpgx7K@x4P0k@lx` and selected bruteforce. And, wait, "Chriz" is there on line 24.. It just rotated the alphabeth and it suddenly made sense.

```
${N0Chriz7M@z4R0m@nz}
```

No Christmas For Romans! Darn, the importance of taking a step back and revisiting old attempts..