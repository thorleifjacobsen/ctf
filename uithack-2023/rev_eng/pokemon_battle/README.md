# Pokemon Battle

Hello there!
Welcome to the world of Pokemon!
My name is Oak!
People call me the Pokemon Prof!

Show me your Pokemon skills by beating all 5 gym leaders, and I will reward you with a flag!

# Writeup

Used strings, ghidra, ltrace, strace, but found something interesting in just typing wrong data into it when it asks what Pokèmon to use:

```
Choose a pokemon to battle with:

Charmander                    Squirtle                      Bulbasaur
Pikachu                       Gengar                        Rhydon
>> x
No cheating!
Traceback (most recent call last):
  File "main.py", line 19, in <module>
  File "main.py", line 7, in main
  File "pokemon.py", line 22, in choose_pokemon
NameError: name 'exit' is not defined
[3733183] Failed to execute script 'main' due to unhandled exception!
```

So this is not a C binary but rather a Python script. After a bit of Googling I found that it is usually possible to extract and decompile these files. So a [website](https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/specific-software-file-type-tricks/.pyc) explained about using [pyinstxtractor.py](https://raw.githubusercontent.com/extremecoders-re/pyinstxtractor/master/pyinstxtractor.py). This is a tool to extract a `ELF Compressed Python` which is what I call it.

```
└─$ python pyinstxtractor.py pokemon
[+] Processing pokemon
[+] Pyinstaller version: 2.1+
[+] Python version: 3.8
[+] Length of package: 5374392 bytes
[+] Found 28 files in CArchive
[+] Beginning extraction...please standby
[+] Possible entry point: pyiboot01_bootstrap.pyc
[+] Possible entry point: main.pyc
[!] Warning: This script is running in a different Python version than the one used to build the executable.
[!] Please run this script in Python 3.8 to prevent extraction errors during unmarshalling
[!] Skipping pyz extraction
[+] Successfully extracted pyinstaller archive: pokemon
```

Gave me a `pokemon_battle` folder which inside had `main.pyc`. Using `uncompyle6` which is a program to uncompile compiled python to python I got this output:

```
└─$ uncompyle6 pokemon_extracted/main.pyc
# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.10.8 (main, Nov  4 2022, 09:21:25) [GCC 12.2.0]
# Embedded file name: main.py
from pokemon import Pokemon
from battle import Battle
from get_flag import Flag

def main():
    user = Pokemon()
    user.choose_pokemon(0)
    for level in range(1, 6):
        ai = Pokemon()
        ai.choose_pokemon(level)
        battle = Battle(user, ai)
        battle.start(level)
    else:
        Flag().print_flag(b'a\x1a<#RT\x08ZF\x16SC\x1c\\Rh\x00\\B\x0e\\,[\x06l\x03\x0f\x04*\\\x01B\x15')


if __name__ == '__main__':
    main()
# okay decompiling pokemon_extracted/main.pyc
```

The pyinstxtractor.py gave me some errors about not having the correct version:

```
[!] Warning: This script is running in a different Python version than the one used to build the executable.
[!] Please run this script in Python 3.8 to prevent extraction errors during unmarshalling
[!] Skipping pyz extraction
```

So downgrading to 3.8.0 and running it again it extracted the pyz archive. There was 82 more files.

This gave me the `get_flag.pyc` which I decompiled:

```
└─$ /home/toffe/.local/bin/uncompyle6 pokemon_extracted/PYZ-00.pyz_extracted/get_flag.pyc
# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.10.8 (main, Nov  4 2022, 09:21:25) [GCC 12.2.0]
# Embedded file name: get_flag.py


class Flag:

    def __init__(self):
        self.key = b'4shk37chum4shk37chum4shk37chum4sh'

    def print_flag(self, flag):
        flag = self.xor(flag, self.key)
        print(f"\n        ____________________________________\n       |                                   |\n       | {flag.decode('utf-8')} |\n       |___________________________________|\n        ")

    def xor(self, data, key):
        return bytearray((a ^ b for a, b in ))
# okay decompiling pokemon_extracted/PYZ-00.pyz_extracted/get_flag.pyc
```

Now I had the flag from `main.py` and the key to decipher it in `get_flag.py`. 

Quickly made this [short script](decipher.py):

```
def xor(data, key):
    return bytearray((a ^ b for a, b in zip(data,key)))

flag=b'a\x1a<#RT\x08ZF\x16SC\x1c\\Rh\x00\\B\x0e\\,[\x06l\x03\x0f\x04*\\\x01B\x15'
key = b'4shk37chum4shk37chum4shk37chum4sh'

print(xor(flag,key))
```

The `zip(data,key)` I found online as it was missing from the decompiler. But running this it printed:

```
bytearray(b'UiTHack23{g0t7a_c47ch_3m_4ll_151}')
```