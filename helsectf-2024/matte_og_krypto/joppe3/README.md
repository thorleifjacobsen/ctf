# joppe2

Redd Joppe, død eller levende!

Joppe er igjen låst inn av Adis venner.

Denne gangen er koden delt slik at du trenger 3 av bitene fra gjengen på 5 for å finne koden til safen der Joppe ligger. Koden inneholder også flagget.

Det er ganske store tall, presisjonen må opp og Adi kan ha glemt å bruke modulo her.

```python
from pwn import *
io = remote("helsectf2024-2da207d37b091b1b4dff-joppe2.chals.io", 443, ssl=True)
io.interactive()
```

# Writeup

I was stuck a while here, because I used the same script as on `joppe2` after I received all the secrets. But this gave me a [fraction](https://simple.wikipedia.org/wiki/Fraction_(mathematics)) back instead of a number which I was expecting.

```bash
$ python3 solve.py 
Secret 1: (2344332245, 65530548079400370318528292311996782073761367365025193477153)
Secret 2: (13429121073, 362422730191176971056722614457277134831341186224587467857920)
Secret 3: (3429121073, 95529569869860840087763619573109073266430740016361100443349)
Secret 4: (23429121073, 611905828855656382575774271667026570700762200408325616089780)
Secret 5: (267429121073, 1304263530048391400503348909036069075396369750743127072608747)
Code: 4887497043165153012042073196309043026084396090283918801549023/2004109180225602264000000000
```

And using 3 other secrets instead of 123 i used 543 then I got a different fraction. 

I tried to manually calculate the fraction in python cli or a calculator but it seems to big to make anything realistic. After a while I got a tip to wrap it in `int` which gave me a number.

From there I did the same as with `joppe2` and used secret 2,3,4 and got:

```bash
$ python3 solve.py 
Secret 1: (2344332245, 65530548079400370318528292311996782073761367365025193477153)
Secret n...
Code: x=323454343233
```

I have the X! Now what? I had X and that would solve it. But how? I tried to solve `Y` with the known `ABC` but that gave me two letters but rest was not possible to solve.

```
b'he\x7f\xb7f\x98=&\x000\x00\xe7\x81\xd2\x1e\xe5\xea\xc27\x04\xb7\xda\x9f'
```

I tried all methods I could think of.. I had x.. Then I asked a collegue and he said that his `x` ended with 4.. I changed my `x` to end with 4 and got a part of the flag:

```
b'helsectf{Jimmy_Ekelund\x16'
```

After a while we found out that he used secret 1,2 and 5 and when I used that my script printed a perfect flag. So after annoying myself on this I figured out what the problem was. The reason it returns a fraction is because the number is not a whole number. It needs to be rounded. And depending on which 3 secrets while rounding with `int` i get the X where value ends with 3, 4 or 5. 

This is probably where the modulo comes in. But I did not quite figure out where to use it or how. So I'm ready to read writeups for that :) 

# Flag

```
helsectf{Jimmy_Ekelund}
```


