# Tools

Here is a list of tools I've used during this CTF

## Basic linux commands

- hexdump (gets a full hexdump from the file)
- strings (gets strings from binary)
- pwn checksec <file> (shows sec of file)

# External websites

- [CyberChef](https://gchq.github.io/CyberChef) - Great tool to do data manupilation
- [CrackStation](https://crackstation.net/) - Great tool to do reverse hashes. Also one of the largest password text files for bruteforce exists here. 
- [Image Diff Checker](https://www.diffchecker.com/image-compare/) - Quickly xor images 
- [DotNet Fiddle](https://dotnetfiddle.net/)
- [RSA Information](https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-1/)
- [Image stegsolver all in one tool](https://www.aperisolve.com/)
- [Webhook Site](https://www.webhook.site/)

# Linux Software

- Ghidra - Reverse engineer a binary
- John the Ripper - Bruteforce passwords
- Hashcat - Bruteforce passwords

# Code snippets

- [Finding ELF Entrypoint](_notes/find_elf_entrypoint.md)

# Random commands I have used

These might be useful in the future or be a future `_notes`

```
cat /proc/`pidof tamagotchi`/maps
```

# Stego toolkit

`docker run -it --rm -v $(pwd)/data:/data dominicbreuker/stego-toolkit /bin/bash`