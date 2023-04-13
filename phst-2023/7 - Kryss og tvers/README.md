# Kryss og tvers

Disse filene dukket opp i en sak, og de ser noe mystiske ut. Jeg tror vi ser på dette helt feil vei, du må nok ta en titt her!

[📎 encoder.py](encoder.py)

Det er best at du ikke sitter på gjerdet, og ser på saken for oss. Hvis du finner innholdet i [📎 flagg.bin](flagg.bin), så kommer det nok til å gå på skinner!

# Writeup

Started by slowly reversing the encoder.py file, ended up with a small script [solve.py](./solve.py)

```python
import b64decode from base64

jx = open("flagg.bin", "rb").read()
jx_decoded = b64decode(jx).decode().split("123456789")
p1 = int(jx_decoded[0])
p2 = int(jx_decoded[1])
p3 = int(jx_decoded[2])

p3_solved = "".join([chr(int(c)) for c in str(p1 ^ p3).rsplit("000")])
x = int("000".join([str(ord(c) << 2) for c in p3_solved]))
p2_solved = "".join([chr(int(c)) for c in str(p2^x).rsplit("000")])
p1_solved = "".join([chr(int(c)) for c in str(p1 ^ (p3 ^ p1) ).rsplit("000")])

print(p1_solved + p2_solved + p3_solved)
```

This outputted:

```
ZigZag PR_cr__ew}S{alFnee_nfnltntitTie_eii_s
```

The description talks about sitting on a fence, and here we see zigzag. Googling `zigzag cipher` gave me a clue that there is something called `rail fence (zigzag) cipher`. So three things hints towards that in the description. Oh well, opening it there gives me nearly nothing. So I open cyberchef, find the zigzag and gets [this](https://gchq.github.io/CyberChef/#recipe=Rail_Fence_Cipher_Decode(3,0)&input=UFJfY3JfX2V3fVN7YWxGbmVlX25mbmx0bnRpdFRpZV9laWlfcw) result. We got the flag.

# Flag

```
PST{Rail_Fence_er_en_fin_liten_twist}
```