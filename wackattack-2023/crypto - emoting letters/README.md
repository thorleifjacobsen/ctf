# Emoting Letters (easy)

People say that cryptographers are emotionless psychopaths, to disprove it I made this emoting cipher, can you solve it?

Author: oksenmu

📎 [emoteingLetters_handout.tar.gz](emoteingLetters_handout.tar.gz)

# Writeup

Finding a encrypted message which looks like a flag format. 

```
😄😧😑😗{😄😇😧😲_😲😇😧😲_😑😦😋😇😯😅_😄😧😝_😲😇😧😲_😝😦😂😋😓😯}
```

Quickly looking at the code I see no way of reversing it at first glance. So I started manually deciphering by replacing known characters. We know the flag starts with `wack` so all those emojies can be replaced.

```
wack{w😇a😲_😲😇a😲_c😦😋😇😯😅_wa😝_😲😇a😲_😝😦😂😋😓😯}
```

For me it seems logical to put in a `H` and `T` on the first word, but that seems to break everything for me. 

```
wack{what_that_c😦😋h😯😅_wa😝_that_😝😦😂😋😓😯}
```

We cannot have `what that` in a english sentence? I made a script to find all possible combination of words from the dictionary:

```python
import string,random
import enchant

letters = [i for i in "abcdefghijklmnopqrstuvwxyz"]
d = enchant.Dict("en_US")
cipher = "w😇a😲 😲😇a😲"

for x in letters:
    for y in letters:
        line = cipher.replace("😇", x).replace("😲", y)
        if d.check(line.split(" ")[0]): # Check first word
            if d.check(line.split(" ")[1]): # Check last word
                print(line) # Legal combo! Print!
```

```bash
└─$ python3 solve.py
wear rear
what that
```

Well, neither of those seems logical to be put after eachother. What am I missing! `what that` makes absolutely no sense for me. 

Struggeling and putting this behind me suddenly a coworker makes it. he tells me that I'm on the correct path and when I complain about `what that` cannot be start of the sentence he sends me:

    what, that could be a question?

Annoyed that the , was not in the flag and at my overthinking brain. I now understand it and starts the manual deciphering by replacing emojies as I go with what seems logical. 

```
😄😧😑😗{😄😇😧😲_😲😇😧😲_😑😦😋😇😯😅_😄😧😝_😲😇😧😲_😝😦😂😋😓😯}
w😧😑😗{w😇😧😲_😲😇😧😲_😑😦😋😇😯😅_w😧😝_😲😇😧😲_😝😦😂😋😓😯}
wa😑😗{w😇a😲_😲😇a😲_😑😦😋😇😯😅_wa😝_😲😇a😲_😝😦😂😋😓😯}
wac😗{w😇a😲_😲😇a😲_c😦😋😇😯😅_wa😝_😲😇a😲_😝😦😂😋😓😯}
wack{w😇a😲_😲😇a😲_c😦😋😇😯😅_wa😝_😲😇a😲_😝😦😂😋😓😯}
wack{w😇a😲_😲😇a😲_c😦😋😇😯😅_was_😲😇a😲_s😦😂😋😓😯}
wack{wha😲_😲ha😲_c😦😋h😯😅_was_😲ha😲_s😦😂😋😓😯}
wack{what_that_c😦😋h😯😅_was_that_s😦😂😋😓😯}
wack{what_that_ci😋h😯😅_was_that_si😂😋😓😯}
wack{what_that_ciph😯😅_was_that_si😂p😓😯}
wack{what_that_ciphe😅_was_that_si😂p😓e}
wack{what_that_cipher_was_that_si😂p😓e}
wack{what_that_cipher_was_that_simp😓e}
wack{what_that_cipher_was_that_simple}
```

# Flag

```
wack{what_that_cipher_was_that_simple}
```
