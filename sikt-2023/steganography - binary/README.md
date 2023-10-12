# binary (🪙 738)

I got this picture from my friend. I don't know how to decrypt it. Can you help me?

📎 [binary.png](binary.png)

# Writeup

Reading this I see a digital signal, I try to decode it basically with 0 and 1's and get this the numbers below. Decoding it seems like base64 and decoding that seems like some asii characters resembling l33t. But I am missing the last part.

```
010110100110101001000101001100001011010011101110011110100111101 = ZjE0´îz= = f14
```

As I see on the base64 it is invalid data on the end there. I've missed a 0 or 1.. To make it simpler I open it up in [Photopea](https://www.photopea.com/). So I opened it in Photpea made it smaller and sectioned it up it what I roughly saw as 1 byte for each (8 bits). 

![binary_simpler.png](binary_simpler.png)

Then I got this:

```
01011010 01101010 01000101 00110000 01011010 01110111 00111101 00111101 = ZjE0Zw== = f14g
```

So finally I got something useful. But it did not have the right flag format. So after a whole lot of hours I finally asked a friend.. He told me to wrap it manually.. So I did and got the flag. 

# Flag

```
siktCTF{f14g}
```