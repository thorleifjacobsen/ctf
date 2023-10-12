# onion (🪙 775)

An onion have many layers, how many layers does this onion have?

📎 [onion.jpg](onion.jpg)

# Writeup

I'm doing all the strings, exiftool e.t.c. Not seeing much, `binwalk` shows a zip archive. I do not totally understand how binwalk works yet. But it seems to have a image + a zip archive.. Named layer1?

```bash
$ binwalk onion.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
172586        0x2A22A         Zip archive data, at least v1.0 to extract, name: Layer_1/
172652        0x2A26C         Zip archive data, at least v2.0 to extract, compressed size: 628853, uncompressed size: 644480, name: 
801745        0xC3BD1         End of Zip archive, footer length: 22Layer_1/onion.jpg
```

Trying and failing I see that it is another onion inside that zip with Layer_2.. So I made this command to just repeat until it failed:

```bash
$ binwalk -e onion.jpg && cd _*/L* && ls
```

After 5 layers `flag.txt` came.

# Flag

```
siktCTF{L4y3r_By_14y3r}
```