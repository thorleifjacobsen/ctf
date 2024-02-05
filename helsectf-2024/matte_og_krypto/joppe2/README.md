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

First when connecting you can select between 5 questions but no code as with joppa1. 

Answers to the riddles i found were: `tastatur`, `7`, `4`, `meg` and `navn` which gave the following secrets:
The real answer to number #1 was `'` (single quote) but they accepted `tastatur` as well. Read about it on the bottom.

```
Secret 1: (4745696227450807, 655305480794027129181307180701455045712682321660286466368078)
Secret 2: (2588682506107567, 655305480793967733879479427128553132958736140573542016023878)
Secret 3: (4035090358829972, 655305480794003703185282913192696782073761367365025193477153)
Secret 4: (4359708773407619, 655305480794013934214261797861718778141983069985929089695418)
Secret 5: (6634057562378419, 655305480794107806938926839990618969191800755240410150653418)
```

I feeded that into my [solve.py](solve.py) as with [joppe1](../joppe1/README.md). Now I got a even bigger number. 

```bash
$ python3 solve.py NOTERM
Secret 1: (4745696227450807, 655305480794027129181307180701455045712682321660286466368078)
Secret 2: (2588682506107567, 655305480793967733879479427128553132958736140573542016023878)
Secret 3: (4035090358829972, 655305480794003703185282913192696782073761367365025193477153)
Secret 4: (4359708773407619, 655305480794013934214261797861718778141983069985929089695418)
Secret 5: (6634057562378419, 655305480794107806938926839990618969191800755240410150653418)
Code: 655305480793942574876234195691695898011105414377060925858173
```

I was now a bit hung up on `modulo` part of the task. It seems to be a red herring? I tried with and without and gave me the same. I saw the 65 and thought it was an hex string but that did nothing. Then after a while I understood that it was a `int` so converting it to `hex` then `ascii` gave me the flag.

```python
>>> hex(655305480793942574876234195691695898011105414377060925858173)
'0x68656c73656374667b6d756c64766172705f65725f6272617d'
>>> bytes.fromhex(hex(655305480793942574876234195691695898011105414377060925858173)[2:])
b'helsectf{muldvarp_er_bra}'
```

# Flag

```
helsectf{muldvarp_er_bra}
```

# Undertanding the first riddle:

`Æ` is `"` (double quote)
and `[` is `=` (equal sign)
what is lowercase `æ`?

So basically it seems to reference what the letters are when using a norwegian keyboard on a english computer. 

The `æ` key is the `" '` key. Holding shift gives double quote. Without it gives single quote. 

So the answer is `'` (single quote). Not sure why keyboard (tastatur) worked though.