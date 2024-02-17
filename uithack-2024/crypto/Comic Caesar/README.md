# Cosmic Caesar

While traveling through the debris of exploded planets, a signal arrived. We've determined the alien alphabet used, but the message is still encrypted. Your mission is to decrypt the secret message.

[⬇️ encrypt.py](./encrypt.py)
[⬇️ flag.txt.enc](./flag.txt.enc)

# Writeup

I copied the [encrypt.py](encrypt.py) to [solve.py](solve.py) and changed the `encrypt` function to `decrypt` and the operators on the formulas from `+` to `-` and vise versa. Then I just ran the script and got the flag.

```bash
UiTHack24{1nt3rg4lact1c_ca3s4r}
```