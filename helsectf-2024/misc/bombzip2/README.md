# bombzip2

Vi har en bzip2-fil som inneholder et komprimert flagg, men den utpakka fila er kjempestor. Mange, mange terabyte, og flagget ligger helt på slutten. Hvis du prøver å pakke den ut fyller du sannsynligvis harddiskene dine. Derfor er oppgaven uløselig.

[⬇️ flag.bz2](flag.bz2)

# Writeup

I had a lot of space so I just unpacked it. Jokes aside `xxd` shows a lot of repeating bytes in it. Can I just remove it with python?

```bash
└─$ xxd flag.bz2 | head
00000000: 425a 6839 3141 5926 5359 0e09 e2df 015f  BZh91AY&SY....._
00000010: 8e40 00c0 0000 0820 0030 804d 4642 a025  .@..... .0.MFB.%
00000020: a90a 8097 3141 5926 5359 0e09 e2df 015f  ....1AY&SY....._
00000030: 8e40 00c0 0000 0820 0030 804d 4642 a025  .@..... .0.MFB.%
```

The 4 bytes in the start `BZh9` is the header for a bz2 file. Then I think the repating pattern is just nullbytes to fill up the file. I wrote a python script to remove the nullbytes and then unpack the file.

```python
with open("flag.bz2", "rb") as f:
    data = f.read()

header = data[:4]
data = data[4:]
data = data.replace(b"\x31\x41\x59\x26\x53\x59\x0e\x09\xe2\xdf\x01\x5f\x8e\x40\x00\xc0\x00\x00\x08\x20\x00\x30\x80\x4d\x46\x42\xa0\x25\xa9\x0a\x80\x97", b"")

with open("flag2.bz2", "wb") as f:
    f.write(header + data)
```

This removed most of the data. Then flag2.bz2 was only 101 bytes. I unpacked it and got an error.

```bash
─$ bunzip2 flag2.bz2 

bunzip2: Data integrity error when decompressing.
        Input file = flag2.bz2, output file = flag2

It is possible that the compressed file(s) have become corrupted.
You can use the -tvv option to test integrity of such files.

You can use the `bzip2recover' program to attempt to recover
data from undamaged sections of corrupted files.

bunzip2: Deleting output file flag2, if it exists.
```

Using bzip2recover on it and i got a new file which successfully unpacked. A lot of null bytes but the flag was at the end and the file was only `12M` instead of terras. Used strings to extrac

```bash
$ strings rec00001flag2 
helsectf{b0mb3rm4n_s3nt_y0u_a_fl4g}
```

# Flag

```
helsectf{b0mb3rm4n_s3nt_y0u_a_fl4g}
````