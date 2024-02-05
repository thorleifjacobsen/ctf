# joppe1

Redd Joppe, død eller levende!

Ola har en lei tendens til å miste muldvarpen sin, Joppe. Denne gangen er den blitt kidnappet av Adi Shamir og hans venner. Adi har låst den inn i safen med en kode som ingen helt vet.

De tre vennene har delt koden mellom seg på en slik måte at du trenger to av bitene for å kunne rekonstruere koden til safen.

De går med på å gi deg sin bit hvis du kan løse deres gåte.

Bruk endepunktet under for å prøve deg på gåtene.

Om du bruker du Adis metode eller ikke så finner du koden på null.

```python
from pwn import *
io = remote("helsectf2024-2da207d37b091b1b4dff-joppe1.chals.io", 443, ssl=True)
io.interactive()
``` 

# Writeup

First when connecting you can select between 3 questions or entering a code. The questions are in norwegian and are simple riddles. If you dont know them google would.

Answers to the riddles are: `ingenting`, `gikk` and `håndkle`. (Nothing, walked, towel) which gave the following secrets:

```
Secret 1: (-500, 1229)
Secret 2: (500, 2229)
Secret 3: (1000, 2729)
```

I then found out about [Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing) and doing some math would end up with a secret number. 

Not quite understanding the math I took to google found [this blog post](https://blog.boot.dev/cryptography/shamirs-secret-sharing/) which explained a bit more. (I've changed some variables to match the code). I used ChatGPT for some help on how to build the equation. It learned me to use `sumpy` which worked wonders.

I made a [solve.py](solve.py) which fetches all of them and then calculates the secret number. 

```bash
$ python3 solve.py NOTERM
Secret 1: (-500, 1229)
Secret 2: (500, 2229)
Secret 3: (1000, 2729)
Code: 1729
Flag: helsectf{ved_x_null_er_alt_gull}
```

# Flag

```
helsectf{ved_x_null_er_alt_gull}
```