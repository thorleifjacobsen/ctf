# Challenge

Check out yet another special binary:

https://htbbinaries.z1.web.core.windows.net/re-santa-2



This seems familiar, yet so different. Test your sploits at:

nc naughtylistadm.norwayeast.azurecontainer.io 4242

> **Hint:** You probably need to bring out a dragon or some other similar tool...

# Writeup

Started with strings, ltrace and strace on the file. Found nothing. Continued with Ghidra (reference "Dragon") to load the binary.

After browsing a while I found a string which matched the text I got when running the app locally. The string moved me into a function which I renamed "main". The dissasembled version looks like this:

```cpp
undefined8 main(void)

{
  int iVar1;
  undefined local_28 [32];
  
  memset(local_28,0,0x1e);
  puts("***************************************************************");
  puts("**************************RE SANTA 2 **************************");
  puts("***************************************************************");
  printf("Please enter the correct input to get the flag:");
  fflush(stdout);
  __isoc99_scanf(&DAT_001020b8,local_28);
  iVar1 = FUN_0010128f(local_28);
  if (iVar1 == 0) {
    puts("[!] Please input the correct password to get the flag");
  }
  else {
    puts("[*] Congratz!");
    FUN_00101331();
  }
  return 0;
}
```

Seems like FUN_0010128f must return other than 0 for us to pass. Lets call this function the "checkInput" and enter it:

```cpp
undefined8 checkInput(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  int local_c;
  
  sVar1 = strlen(param_1);
  if ((int)sVar1 == 0xf) {
    for (local_c = 0; local_c < 0xf; local_c = local_c + 1) {
      if (((int)param_1[local_c] ^ (uint)(byte)(&DAT_00104058)[local_c % 4]) !=
          (uint)(byte)(&DAT_00104060)[local_c]) {
        return 0;
      }
    }
    uVar2 = 1;
  }
  else {
    uVar2 = 0;
  }
  return uVar2;
}
```

Lets clean up the code a bit.

```cpp
undefined8 checkInput(char *inputCode)

{
  size_t inputLength;
  undefined8 response;
  int cnt;
  
  inputLength = strlen(inputCode);
  if ((int)inputLength == 0xf) {
    for (cnt = 0; cnt < 0xf; cnt = cnt + 1) {
      if (((int)inputCode[cnt] ^ (uint)(byte)(&exponent)[cnt % 4]) != (uint)(byte)(&password)[cnt])
      {
        return 0;
      }
    }
    response = 1;
  }
  else {
    response = 0;
  }
  return response;
}
```

So it takes our inputCode and verifies that it is 0xf length (15 characters). So we know the code must be 15 characters long.
Then it seems to do some math on each character. First I need to find the global variables I named exponent and password. 
Clicking them in Ghydra shows me their position and actual values. The Exponent seems to be ABCD (41,42,43,44), the password is a string
of random characters. Lets convert this to a JS function as that is what I know best.


```javascript
function checkInput(input = "123456789abcdef") {
    input = Buffer.from(input);

    // Found in the binary.
    let exponent = Buffer.from([0x41, 0x42, 0x43, 0x44]);
    let password = Buffer.from([0x09, 0x23, 0x35, 0x21, 0x18, 0x2d, 0x36, 0x06, 0x24, 0x27, 0x2d, 0x03, 0x71, 0x72, 0x27]);

    if (input.length == 15) { 
        for (let i=0; i<15; i++) {
            if ((input[i] ^ exponent[i % 4]) != password[i]) {
                console.log("Fail!?");
                return 0
            }            
        }
        return 1;
    }
    return 0;
}
```

Now we have the function disassembled, lets reverse it.

`x XOR y = z`

We need x so we can take z XOR y. 

```javascript
let password = Buffer.from([0x09, 0x23, 0x35, 0x21, 0x18, 0x2d, 0x36, 0x06, 0x24, 0x27, 0x2d, 0x03, 0x71, 0x72, 0x27]);
let exponent = Buffer.from([0x41, 0x42, 0x43, 0x44]);
let ans = Buffer.alloc(15)
for (let i=0; i<15; i++) {
    ans[i] = password[i] ^ exponent[i % 4]
}
console.log(ans.toString());
```

And out came the password, and it worked.

```bash
***************************************************************
********************** NAUGHTY LIST ADM ***********************
***************************************************************
Please enter the correct input to get the flag:HaveYouBeenG00d
[*] Congratz!
Ho Ho Ho! Your flag is: ${N@u647y_1i57_3v@d3d}
```