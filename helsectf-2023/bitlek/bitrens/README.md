# bitrens (493)

Det kan virke som meldingen min ble utsatt for litt støy da jeg overførte den. Ikke'no problem! Vi renser bittene slik at meldingen blir lesbar!

```python
melding = "c96ea0e3efedf0757469ee67aca0e269f4206ef56de2e57269ee672069f3a074e8e5a0e3ef6ef6656e74e96feea0f573e564a0746fa0e964656ef469e6f9a074e8e52062e9f4a070ef73697469efee73a0e96ea061a0e2696e61f279a0eef56d62e5722ea08a8a49eea0e3ef6df0f57469ee677468e5a06deff3f4a0f369e76e69e66963e1eef420e269f42028cdd342a9a0f2e5f072e57365ee74732074e865a0e86967e865f374ad6ff2e46572a070ece1e3e5a06fe6207468e520e2e9ee61f2f920e96ef4e567e572ae20d4e8e5204cd34220e9f3a0736fed657469ede573a072e566e5f2f265e4a074efa0e1f32074e8e5206ceff72d6f72e465f2a0e269f4a06f7220f2e967e874ad6d6ff3f420e2e9742ca0e4f5652074efa074e8e520e36fee7665eef4696f6e20e96ea0f06f736974696f6e616c206e6f746174696f6e206f662077726974696e67206c657373207369676e69666963616e7420646967697473206675727468657220746f207468652072696768742e20546865204d53422069732073696d696c61726c7920726566657272656420746f2061732074686520686967682d6f7264657220626974206f72206c6566742d6d6f7374206269742e200a0a536f757263653a2068747470733a2f2f656e2e77696b6970656469612e6f72672f77696b692f4269745f6e756d626572696e670a"
def bitrensing(s):
    return "".join(map(lambda ch: chr(ch&0x7f), bytes.fromhex(s)))
print(bitrensing(melding))
```

Kanskje noen burde undersøke denne støyen nærmere. Den virker ikke å være så tilfeldig som man skulle tro.

# Writeup

Analyzed the `bitrensing` function which seems to only get rid of any bit above the 7 bits needed for ascii. So guessing there are more than 8 bits then.

A quick script to get the 8th bit out.

```python
for b in bytes.fromhex(melding):
    print(b >> 7, end="")
```

resulted in:

```
10111110001011101001011001000110111110100010111010100110001011101100111010000110110101100010111001001110111101100100011011111010010011101010011011111010010000101100101010110010111110100010111011010110101011100100111001000110101011101101111001100110001011101100011010100110110011100011011010100110000101100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

Fully plausible that this means something. After manual analyzing I found out based on the string from the original message talking about MSB that this is 8 bits. So doing a rough automagic-"manual" method:

```
temp = flag = ""
for b in bytes.fromhex(melding):
    b = b >> 7
    temp += f"{b}"
    if len(temp) == 8:
        flag += chr(int(temp[::-1],2))
        temp = ""

print(flag[::-1])
```

# Flag

```
helsectf{ubrukt_MSB_er_bortkastet_bit}
```