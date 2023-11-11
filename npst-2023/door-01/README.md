# 01 - Julekalender

Her får du den første oppgaven!

Under etterforskningen av hendelsen på jule-verkstedet har vi oppdaget noe rart. Et av meldingssystemene som sender varslinger til beredskapsvaktene for verkstedet har sendt en SMS til et ukjent nummer. Meldingen er dessverre helt uleselig for oss, så vi trenger dine mobildetektiv-egenskaper. Når du finner ut av det, send meg svar på formatet PST{ditt svar her}.

```
7-4 9-3 7-4 8-1 3-2 6-1 0-1
4-3 6-2 3-3 4-3 7-4 3-2 7-3
8-1 0-1 4-1 7-3 8-2 6-2 5-2
3-2 7-3 0-1 4-3 6-2 2-3 6-3
6-1 4-3 6-2 4-1
```

- Tastefinger

# Writeup

I quickly think of the old Nokia Phones and looking at the [image](./image.png) of one shows me the letters. So 7 pressed 4 times would be a `s`. I continue 3 letters and see `sys`. Then since I'm lazy I made this script to do this for me:

```python
#!/usr/bin/env python3

# This represent the numbers (index) and letters (values) of the keypad.
keypadLetters = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def getLetter(number, times):
    return keypadLetters[number][times-1]

# Load input and split by space
input="7-4 9-3 7-4 8-1 3-2 6-1 0-1 4-3 6-2 3-3 4-3 7-4 3-2 7-3 8-1 0-1 4-1 7-3 8-2 6-2 5-2 3-2 7-3 0-1 4-3 6-2 2-3 6-3 6-1 4-3 6-2 4-1".split(" ")

# Loop through the input
for i in input:
    # Split by -
    number, times = i.split("-")
    # Print the letter
    print(getLetter(int(number), int(times)), end="")
```

This returns something that makes .. half-sense? 

```
system infisert grunker incoming
```

Tried this as a flag and it worked!

# Flag

```
PST{system infisert grunker incoming}
```