# You wouldn't download a car


You wouldn't steal a car
You wouldn't steal a handbag
You wouldn't steal a television
You wouldn't steal a movie

Downloading pirated films is stealing,
stealing is against the law,
PIRACY. IT'S A CRIME

This is a really good piece of software. You have to pay for it.

# Writeup

Strings shows

```
You wouldn't steal a handbag
You wouldn't steal a television
You wouldn't steal a movie
Downloading pirated films is stealing,
stealing is against the law,
PIRACY. IT'S A CRIME
Please insert licence key (XXXX-XXXX-XXXX-XXXX): 
```

Running it and entering a wrong key shows:

```
Invalid licence provided. Please pay for our proprietary Garbage©
```

Opening the file in `gdb` then running `info files` shows `Entry point: 0x1040`. Opening in Ghidra there is a function named: `FUN_00101040` (Ghidra has 10k offset so 0010 in the start is actually 0000). This seems like the main function, it loads a new function which seems like this:

```c
void FUN_00101700(void) {
  ulong uVar1;
  undefined local_57 [19];
  undefined local_44 [19];
  undefined local_31 [49];
  
  FUN_00101a30(1,&DAT_001041c0,0xcc);
  FUN_00101a30(1,&DAT_0010428c,0x31);
  memset(local_57,0,0x13);
  FUN_00101a60(0,local_57,0x13);
  FUN_00101870(local_44,&DAT_001042bd,&DAT_001042d0);
  uVar1 = FUN_00101560(local_57,local_44);
  if ((uVar1 & 1) == 0) {
    FUN_00101a30(1,&DAT_00104345,0x43);
  }
  else {
    FUN_001017f0(local_31,&DAT_001042e3,&DAT_00104314);
    FUN_00101a30(1,local_31,0x31);
  }
  FUN_00101a90(0);
  FUN_00103910("internal error: entered unreachable codesrc/main.rs",0x28,&DAT_00105d08);
  do {
    invalidInstructionException();
  } while( true );
}
```

`DAT_001041c0` seems to be the data position for the first line of text and the count. So `FUN_00101a30` probably is a println function. Then there is an `if` statement. It seems like the first print function shows the invalid code so I want to bypass this and get to the else part of the function. The else part seems to print the flag if we enter the valid code. So let see if I can make it skip that.

!(Image1)[image1.png]

By modifying this `JNZ` (Jump if not zero) to just `JMP` (jump) we would skip the whole if and go straight to the else statement. So right click -> patch instruction -> change `jnz` to `jmp`.

!(Image2)[image2.png]


Now I can save the file, go back to Ghidra and export this file as a PE. 

!(Image3)[image3.png]

Then run the program and we do not need a key anymore. Entering "a" will be enough:

``` 
You wouldn't steal a car
You wouldn't steal a handbag
You wouldn't steal a television
You wouldn't steal a movie

Downloading pirated films is stealing,
stealing is against the law,
PIRACY. IT'S A CRIME

Please insert licence key (XXXX-XXXX-XXXX-XXXX): a
The flag is UiTHack23{sail_the_high_seas_pirate}
```