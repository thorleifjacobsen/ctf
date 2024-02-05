# konvertere

For å konvertere mellom store tall og strenger anbefales det å bruke pycryptodome i Python. Denne kan installeres med pip install pycryptodome.

Vi bruker denne i f.eks. kryptooppgaver med RSA for å gå fra byte-strenger til tall for å gjøre RSA operasjoner, og tilbake. Dette er brukt i RSA oppgaven kontraktsignering.

Jeg har skjult et flagg som et tall:

```python
>>> from Crypto.Util.number import long_to_bytes, bytes_to_long   
>>> flag = bytes_to_long(b"helsectf{??? ... ???}")
>>> print(flag)
9999168102934914777774346849293018679871929920575661949
```

For å konvertere tilbake til bytes kan du bruke print(long_to_bytes(<tall>))

# Writeup

Ran python3 and pasted the two lines in to get the flag:

```python
>>> from Crypto.Util.number import long_to_bytes
>>> print(long_to_bytes(9999168102934914777774346849293018679871929920575661949))
b'helsectf{bytes_to_long}'
```

# Flag

```
helsectf{bytes_to_long}
```