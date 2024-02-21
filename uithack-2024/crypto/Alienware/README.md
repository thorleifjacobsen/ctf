# Alienware

Aliens have encrypted my very important file! Luckily they forgot to delete the software from the trash folder, can you help me decrypt it?

[⬇️ word.py](./word.py)
[⬇️ Stardust-reckoning.txt.enc](./Stardust-reckoning.txt.enc)

# Writeup

Reading the [Encryptinator 9000](./word.py) I see it does some random number XOR operations. But the random number generator is seeded with `NiceTry`. And the script replaces `8008135` with `NiceTry` when done. So guessing the seed was `8008135`. It also swaps the case on the key using swapcase.

```python 
with open(__name__, "wb") as f:
    f.write(f.read().replace(b"8008135", b"NiceTry").replace(KEY, KEY.swapcase()))
os.remove(__name__)
```

I tried to reverse the script with the seed and swapcase but I got gibberish, I tried to remove the `"` on the seed as I thought the seed was supposed to be numbers and now I got something that looked logical:

```bash
python3 word.py | head -c 20
b'StardL\x19!\x91\x1
```

Still it is mostly gibberish. No logical explanation. I finally found out that my `.enc` file was fubar and I had to download it again. After it decrypted and I got a whole lot of text and a flag!

```bash
UiTHack24{E.T._ph0ne_h0me_plsss}
```

This one was super simple but looked alienated at first. So I skipped it but that would have been some easy points! :(