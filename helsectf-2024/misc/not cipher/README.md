# not cipher

Utvikler Carl I. Pher trenger av og til å kjøre python-programmer på webserveren sin. Derfor har han laget en veldig enkel webtjeneste for å sende inn python-programmer og returnere output:

Eksempelkjøring av program: curl 'http://server/?program=print(repr(repr))'

For å hindre misbruk er kun 13 forskjellige tegn tillatt i python-programmet: not+cipher(*)

Dessverre viser det seg at dette ikke er godt nok. Hent ut flagget i /lol/hemmeligmappe/flagg.txt

https://helsectf2024-2da207d37b091b1b4dff-not-cipher.chals.io

# Writeup

I started by figuring out what builtins i could use with this snippet from last helsectf:

```python
def valid(s):
    for ch in s:
        if ch not in 'not+cipher(*)': return False
    return True

for b in dir(__builtins__):
    if valid(b): print(b)
```

gave me this list

```
chr,int,iter,oct,open,print,repr
```

So it seems like I need to make numbers to use chr and ord. I got + and * to make numbers and then I can use chr and ord to make strings. I can then use open to open files and print to print them.

I made a script based on the availability of the "ord" function. By using `ord(repr(int()))` I had 48. Dividing 48 on 48 gives 1. then But after I made the script to generate this for me I noticed that `ord` or `/` was not in the package. Luckily the script was made in such way that it could easily be modified to use any other method if I find one.

I tried tried a whole lot to generate a number but for some reason I could not get anything but `0`. Then suddenly I tried the `**` with `int()**int()` and there I got 1! After a bit of googling it shows that `**` is power.  that is the same as power. So `0^0` is `1`. [Read explanation here](https://betterexplained.com/articles/understanding-exponents-why-does-00-1/)

So with that in mind I modified my [solve.js](solve.js) script to use `int()**int()` instead of `ord(repr(int()))` and it failed. Complaining that I had `0x20` in there. After a sleep I figured out what that was. Using `+` it converts to spaces once the server receives it. I need to `URLEncode` the string to put it in the url. 

Slapped that on and now I could run this:

```bash
$ curl "$(node solve.js)"
helsectf{lange_programmer_lever_lengst}
```

# Flag

```
helsectf{lange_programmer_lever_lengst}
```