# Pokemon Battle V2

The feedback for the V1 of the Pokemon Battle has been reviewed, and the following changes have been made:

Gym leaders have less hp
The amount of gym leaders have been reduced from 5 to 3
Patched unintended way to view the flag

# Writeup

> This part I did before the first Pokemon Battle. I did not know this one was the `???` one until I read the Discord later down here.

I started the binary with no secret code and guessed my moves.

```
Secret Code?: 
Choose a pokemon to battle with:

Charmander                    Squirtle                      Bulbasaur
Pikachu                       Gengar                        Rhydon
>> Pikachu

Brock wants to fight! 
Brock sent out Snorlax!
Go Pikachu!

Snorlax has 32 hp!
Pikachu has 51 hp!

>> thunderbolt
Pikachu used thunderbolt!
Snorlax has 0 hp!
You have defeated Brock!

Misty wants to fight!
Misty sent out Rhydon!
Go Pikachu!

Rhydon has 32 hp!
Pikachu has 51 hp!

Choose a move:
thrash              thunder
thunderbolt         pound

>> pound
Pikachu used pound!
Rhydon has 0 hp!
You have defeated Misty!

Sabrina wants to fight!
Sabrina sent out Gengar!
Go Pikachu!

Gengar has 77 hp!
Pikachu has 51 hp!

Choose a move:
thrash              thunder
thunderbolt         pound

>> trash
Your pokemon does not know this move!

Choose a move:
thrash              thunder
thunderbolt         pound

>> thrash
Pikachu used thrash!
Gengar has 26 hp!
Gengar used acid!
Pikachu has 34 hp!

Choose a move:
thrash              thunder
thunderbolt         pound

>> thrash
Pikachu used thrash!
Gengar has 0 hp!
You have defeated Sabrina!

You are the new Pokemon Champion!

This might be useful for you
 _______________________________
|                               |
| Secret Code: C0mpl3te_P0ked3x |
|_______________________________|

Here is your flag:

b'd\x089\x0fQ\n\x05U|\x15m^A;\x17A]+B\x1d\x10*\x05E\x1eF\x18\x1a\x1b*\x16\x1dA\x18\x05\x1cE\x1cN'
```

It seems like that secret code allows me to bypass and show the binary data again:

```
Secret Code?: C0mpl3te_P0ked3x

Welcome back Champion!

b'd\x089\x0fQ\n\x05U|\x15m^A;\x17A]+B\x1d\x10*\x05E\x1eF\x18\x1a\x1b*\x16\x1dA\x18\x05\x1cE\x1cN'
```

> I read the Discord and understood that this one was supposed to come after the `Pokemon Battle` one. I did the other pokemon battle in between here so I have some knowledge about what is going on. The above is xor'ed key and I might need to decompile the elf? :)

Lets continue. Quickly moved over the [pyinstxtractor.py](pyinstxtractor.py) and run it in Python 3.8 as the other challenge was in this. And bingo:

```bash
$ python pyinstxtractor.py pokemon_v2
[+] Processing pokemon_v2
[+] Pyinstaller version: 2.1+
[+] Python version: 3.8
[+] Length of package: 5887907 bytes
[+] Found 31 files in CArchive
[+] Beginning extraction...please standby
[+] Possible entry point: pyiboot01_bootstrap.pyc
[+] Possible entry point: main.pyc
[+] Found 86 files in PYZ archive
[+] Successfully extracted pyinstaller archive: pokemon_v2

You can now use a python decompiler on the pyc files within the extracted directory
```

Quickly uncompiled pokemon_v2 and saw it was `pyarmor protected`

```python
$ uncompyle6 pokemon_v2_extracted/main.pyc     

# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.10.8 (main, Nov  4 2022, 09:21:25) [GCC 12.2.0]
# Embedded file name: dist/obf/main.py
from pytransform import pyarmor_runtime
pyarmor_runtime()
__pyarmor__(__name__, __file__, b'PYARMOR\x00\x00\x03\x08\x00U\r\r\n\t4\xe0\x02\x00\x00\x00\x00\x01\x00\x00\x00@\x00\x00\x00\xc4\x12\x00\x00\x00\x00\x00\x18-\x8a\x9b<\xe8/\xab7.\xcf\x88\xb6Y ..... a lot more.... 
```

So looking at [this](https://0xdf.gitlab.io/flare-on-2022/challenge_that_shall_not_be_named) challenge I understood that I could run the pyc files. So I started running the main.pyc:

```bash
$ python pokemon_v2_extracted/main.pyc
Traceback (most recent call last):
  File "dist/obf/main.py", line 1, in <module>
ModuleNotFoundError: No module named 'pytransform'
```

Well, I can make that one by using `pyarmor obfuscate filewithprintonly.py`. This gives me dist folder with the `pytransform` folder. 'Move that into `pokemon_v2_extracted` and we run again:

```bash
$ python pokemon_v2_extracted/main.pyc
Traceback (most recent call last):
  File "<dist/obf/main.py>", line 3, in <module>
  File "<frozen main>", line 4, in <module>
ModuleNotFoundError: No module named 'pokemon'
```

So I just make `pokemon.py` with the same class as the previous challenge:

```python
class Pokemon:
    def __init__(self):
        pass
```

Next

```bash
$ python pokemon_v2_extracted/main.pyc
Traceback (most recent call last):
  File "<dist/obf/main.py>", line 3, in <module>
  File "<frozen main>", line 5, in <module>
ModuleNotFoundError: No module named 'battle'
```

Did the same, just with "Battle" as module name. Next!

```bash
$ python pokemon_v2_extracted/main.pyc
Traceback (most recent call last):
  File "<dist/obf/main.py>", line 3, in <module>
  File "<frozen main>", line 7, in <module>
ModuleNotFoundError: No module named 'get_flag'
```

Now we are going somewhere. I can make my own get flag. Based on the previous pokemon_battle I know the `get_flag` file so I make this one:

```python
class Flag:

    def __init__(self):
        pass
        
    def print_flag(self, flag):
        print(flag)
```

Trying again:

```bash
$ python pokemon_v2_extracted/main.pyc
Traceback (most recent call last):
  File "<dist/obf/main.py>", line 3, in <module>
  File "<frozen main>", line 109, in <module>
  File "<frozen main>", line 104, in protect_pytransform
  File "<frozen main>", line 96, in check_lib_pytransform
RuntimeError: unexpected /home/toffe/Projects/ctf/uithack-2023/rev_eng/pokemon_battle_v2/pokemon_v2_extracted/pytransform/_pytransform.so
```

Oh, prolly wrong `_pytranform.so`, there is one extracted by `pyinstxtractor.py` so I'll use that instead. Replace the one I made with PyArmor.

```bash
$ python pokemon_v2_extracted/main.pyc
Secret Code?: C0mpl3te_P0ked3x

Welcome back Champion!
b'UiTHack23{Y0u_ar3_7he_p0k3mon_ch4mpi0n}' 
```
Bingo