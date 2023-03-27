# sju_hopp_til_venstre (493)

Flagget er skjult med en enkel enkoding

[source.py](source.py) [output.txt](output.txt)

# Writeup

Trying to understand how this script works, it gets the ASCII value of each characters. It then OR's it with 127 which is the same as `1111111`.  It then shifts all bits 7*character position. So the first one is 7 bits to the left, second is bit 8 to 14 e.t.c. When done it has a long number.

To reverse this we need to get 7 bits at a time out of the cipher. So we start with the number and remove 7 bits at a time until we have removed all.

```python
ciphertext = 121618823462879646550735496413151112443159521807771000855798554217421990706110849430002588375600568500567865051416710544882967
while ciphertext > 0: 
    # Extract 7 bits
    character = ciphertext & 0b1111111
    print(chr(character), end = '')
    # Remove 7 right most bits
    ciphertext = ciphertext >> 7
```

# Flagg

```
helsectf{ascii_kan_enkodes_med_7bit_siden_MSB_alltid_er_0}
```