# Ollivanders

Before you go to Hogwarts you need to buy yourself a proper wand.
Visit Mr. Ollivander's shop to see if he has something interesting to sell you!

Connect to Ollivanders with netcat

$ nc motherload.td.org.uit.no 8008

# Writeup

Looking at the source I see buying, flag or wands. We start with 20 galleons annd need 50 to buy the flag. When buying wand it uses this formula

```
galleons - 7 * amount
```

So if i buy -5 my amount of galleonns will be 55 and that seems right:

```
You have 55g
```

So buying the flag is easy now:

```
What item would you like to buy?
1. Holly wand      7g
2. Flag            50g
>> 2

You have purchased the flag!
UiTHack23{Why_w0uld_y0u_buy_4_n3gat1ve_am0un7?}
```