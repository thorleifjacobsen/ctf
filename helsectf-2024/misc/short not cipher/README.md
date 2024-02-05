# short not cipher

Denne oppgaven er helt lik not cipher, bare at programmet du sender inn må være kortere enn 5000 tegn.

# Writeup

I already had the [solve.js](../not%20cipher/solve.js) from the previous so I created a new one here to modify so I could shorten it. I think the last one had 14k characters. So this is 2/3 reduction.

I started by using the power method. That could generate higher numbers faster than just multiplying a whole lot. Then after modififying the script and then fine-tuning a bit we added:

* Repeating characters uses multiplication method to repeat the character
* Only adding pharanthesis on formulas with +

While this got it down to around 6500 it still was not good enough. Then I remembered `repr` which takes any object and stringifies it. Using this I could go from `233` characters to create the number 100 down to `49`. `repr(int()) == '0'` and `repr(int())*int() == '1'`. So I could use this to create 111 and 100 easily.

```python
>>> int(repr(int()**int())+repr(int())+repr(int()))
100
```

Adding this shortened a lot of the numbers. See table below:

| Number | Characters before | Characters after |
|:------:|:-----------------:|:----------------:|
| 32     | 131               | 113              |
| 37     | 214               | 184              |
| 46     | 315               | 269              |
| 47     | 330               | 282              |
| 64     | 117               | 97               |
| 81     | 117               | 97               |
| 97     | 197               | 169              |
| 100    | 233               | 49               |
| 101    | 250               | 64               |

And this was the bingo moment. I had `4095` characters on my new [solve.js](solve.js).  So I shipped it and got the flag!

# Flag

```
helsectf{h4rd3r_b3tt3r_f4s73r_sh0rt3r}
```
