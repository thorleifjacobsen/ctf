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

# Linux Software

- Ghidra - Reverse engineer a binary
- John the Ripper - Bruteforce passwords

# Code snippets

## Find start address of elf

At 452540 is the start address. But little endian so reversing that the start of this example program is actually `s402545`

```bash
┌──(toffe㉿kali)-[~/Projects/uithack/pokemon]
└─$ xxd -l 64 pokemon_v2 
00000000: 7f45 4c46 0201 0100 0000 0000 0000 0000  .ELF............
00000010: 0200 3e00 0100 0000 4525 4000 0000 0000  ..>.....E%@.....
00000020: 4000 0000 0000 0000 a09b 5a00 0000 0000  @.........Z.....
00000030: 0000 0000 4000 3800 0b00 4000 1c00 1b00  ....@.8...@.....
```

## Dont know but it is useful:

cat /proc/`pidof tamagotchi`/maps



https://github.com/x41x41x41/hackingpotato/blob/master/techniques/stenography.md