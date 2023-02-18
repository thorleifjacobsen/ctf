# Kasparovs nightmare

Kasparov is sick and tired of overused cryptographic techniques and has decided to invent his own technique using a simple chess puzzle. A chess board is a 8x8 square represented by letters going from left to right and numbers up and down. Force the checkmate as white.

Run python3 chess.py to start the challenge!

Example: Moving any piece from d2 to d4
From: 2d
To: 4d

# Writeup

I dont like chess so I started bruting.. 

```python
base_moves = ""
encrypted_flag = b'm\ng+T\x07^W\x00\x18@\x10Z\x06_\x00Z\x17[:]\x15j\x13A\x04F\rH'.decode()

for i in range(1,9):
    for x in range(ord("a"), ord("h")):
        flagg = [chr((ord(a) ^ ord(b))) for a, b in zip(encrypted_flag, base_moves + f"{i}{chr(x)}")]
        flagg = "".join(flagg)

        print(f"{i}{chr(x)} = {flagg}")
```

This loops all squares and adds to the algorithm. I knew `UiTHack23{` so I just took the matching things until I came as far as this:

```
Set base_moves to = "8c3c5d5e"

....
3c = UiTHack23{
....
```

So `8c3c5d5e3c` is the start. But I need more and now I'm just guessing. Thinking to make something that prints every possible thing, but that would .. big a lot :) So then I think maybe it is a regular setup? So I google `chess solver` and find [Chess Next Move](http://www.chessnextmove.com/). Moved the pieces as the board in python and  boom there I go. All the moves matches with what the code needs.

```python
moves = "8c3c" + "5d5e" + "3c3d" + "5e4f"  + "3d3e" + "4f5g" + "3e5e" + "5g6h" + "5e5h"
encrypted_flag = b'm\ng+T\x07^W\x00\x18@\x10Z\x06_\x00Z\x17[:]\x15j\x13A\x04F\rH'.decode()
print("".join([chr((ord(a) ^ ord(b))) for a, b in zip(encrypted_flag, moves)]))
```

```bash
UiTHack23{stockfish_is_trash}
```

