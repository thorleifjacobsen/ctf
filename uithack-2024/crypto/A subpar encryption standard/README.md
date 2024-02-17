# A subpar encryption standard

While looking around in the remains of an enemy spaceship you find some code. In their hurry they must have forgotten that there were more steps to do.

[⬇️ flag.txt.enc](./flag.txt.enc)
[⬇️ encrypt.py](./encrypt.py)

# Writeup

Saw that when I wrote "UiTHack" in the script I got the same output as the 7 first of the encrypted file. Then I tried some random letters `T` and `i` and saw that they resolved to the same. This way I could just brute it by testing every single character and see if it matched the byte, if it did print it and go to next. 

```python
# Brute the flag
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!#$%&'()*+,-./:;<=>?@[]^`{|}~"
flag_enc = "fc f9 20 52 ef fb 7f 23 18 21 aa b6 92 4d 3c ef 8f 92 4d 40 cf 40 f9 2 9f 43 ef 4d 50 ff".split(" ")
s_box = construct_s_box()

while len(flag_enc) > 0:
	for i in range(len(characters)):
		char = characters[i]
		char_enc = hex(s_box[ord(char) // 16][ord(char) % 16])[2:]

		if char_enc == flag_enc[0]:
			print(char, end="")
			flag_enc.pop(0)
			break
```

```
└─$ python3 decrypt.py 
UiTHack24{bytemaster_rijndael}
```