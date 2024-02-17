# Exfiltration

Congratulations, Agent! You've successfully infiltrated the enigmatic alien base and managed to steal their highly classified code. However, it seems that it is written in some weird foreign language. Your next mission is to find out what their code does!

[⬇️ exfiltraded.js](./exfiltraded.js)

# Writeup

I saw that when using `forEach` function manually with `UiTHack` it gave me the same encrypted string as the one in the file, except for the last character. It seems to be using the character after the one it is encrypting in the calulation. So I made a quick [solve.js](solve.js) script to do bruteforce it by trying a known string `UiTHack` then appending two more characters and check if the second last is the same as the encrypted string we have.

So basically bruting it one by one. Using my [solve.js](./solve.js) script I got the flag:

```bash
$ node solve.js
Flag: UiTH
Flag: UiTHa
Flag: UiTHac
Flag: UiTHack
Flag: UiTHack2
Flag: UiTHack24
Flag: UiTHack24{
Flag: UiTHack24{j
Flag: UiTHack24{j4
Flag: UiTHack24{j4v
Flag: UiTHack24{j4v4
Flag: UiTHack24{j4v4s
Flag: UiTHack24{j4v4sc
Flag: UiTHack24{j4v4scr
Flag: UiTHack24{j4v4scr1
Flag: UiTHack24{j4v4scr1p
Flag: UiTHack24{j4v4scr1p7
Flag: UiTHack24{j4v4scr1p7_
Flag: UiTHack24{j4v4scr1p7_1
Flag: UiTHack24{j4v4scr1p7_15
Flag: UiTHack24{j4v4scr1p7_15_
Flag: UiTHack24{j4v4scr1p7_15_a
Flag: UiTHack24{j4v4scr1p7_15_an
Flag: UiTHack24{j4v4scr1p7_15_an_
Flag: UiTHack24{j4v4scr1p7_15_an_4
Flag: UiTHack24{j4v4scr1p7_15_an_4l
Flag: UiTHack24{j4v4scr1p7_15_an_4l1
Flag: UiTHack24{j4v4scr1p7_15_an_4l1e
Flag: UiTHack24{j4v4scr1p7_15_an_4l1en
Flag: UiTHack24{j4v4scr1p7_15_an_4l1en_
Flag: UiTHack24{j4v4scr1p7_15_an_4l1en_l
Flag: UiTHack24{j4v4scr1p7_15_an_4l1en_l4
Flag: UiTHack24{j4v4scr1p7_15_an_4l1en_l4n
Flag: UiTHack24{j4v4scr1p7_15_an_4l1en_l4ng
Flag: UiTHack24{j4v4scr1p7_15_an_4l1en_l4ngu
Flag: UiTHack24{j4v4scr1p7_15_an_4l1en_l4ngu4
Flag: UiTHack24{j4v4scr1p7_15_an_4l1en_l4ngu4g
Flag: UiTHack24{j4v4scr1p7_15_an_4l1en_l4ngu4g3
Flag: UiTHack24{j4v4scr1p7_15_an_4l1en_l4ngu4g3}
```