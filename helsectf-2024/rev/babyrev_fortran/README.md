# babyrev_fortran

En babyrev husker gamle fortellinger fra sin bestefar som programmerte i et litt utdatert programmeringsspråk. Heldigvis kom det en senere revisjon på 90-tallet som er noe enklere å bruke.

Greier du å printet ut flagget i klartekst?

[⬇ babyrev_fortran](./babyrev_fortran)

# Writeup

Opened it in Ghidra to find the main function.

```cpp
void MAIN__(void) {
  undefined local_258 [64];
  undefined4 local_218;
  undefined4 local_214;
  char *local_210;
  undefined4 local_208;

  local_210 = "main.f90";
  local_208 = 0x22;
  local_218 = 0x80;
  local_214 = 6;
  _gfortran_st_write(&local_218);
  _gfortran_transfer_character_write(&local_218,"flag=",5);
  // This is the interesting part as this is what gets the flag of 0x33 length into local_258 which is printed on the next line
  __a_MOD_b(local_258,0x33,""); 
  _gfortran_transfer_character_write(&local_218,local_258,0x33);
  _gfortran_st_write_done(&local_218);
  return;
}
```

So we see that the flag is stored in `local_258` and that it is 0x33 bytes long.

```cpp
void __a_MOD_b(void *param_1,undefined8 param_2,int *param_3) {
  memmove(param_1,__a_MOD_flag,0x33); // This moves the encrypted flag into the address of local_258 which is the first parameter here.
  if (0 < *param_3) { // This is never true 
    __a_MOD_d(param_1,0x33); // This is interesting. 
  }
  return;
}
```

I tried to patch that if to be always true but when I did the program just hang. I saw the `__a_MOD_d` did some math on the flag and cleaned it up so prolly the reversing function for the encrypted flag.

```cpp
void __a_MOD_d(long param_1,int param_2) {
  uint uVar1;
  undefined4 local_238;
  undefined4 local_234;
  char *local_230;
  undefined4 local_228;
  char *local_1e8;
  undefined8 local_1e0;
  char local_21;
  uint local_20;
  int local_1c;

  // The flag is param1 and length is param2 so it seems like this loops trough from 1 to 0x33 (51)
  for (local_1c = 1; local_1c <= param_2; local_1c = local_1c + 1) {
    // This gets the letter as a byte at the inndex of local_1c - 1 so 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ... 0x33
    local_20 = (uint)*(byte *)(param_1 + -1 + (long)local_1c);
    local_230 = "main.f90";
    local_228 = 0x13;
    local_1e8 = "(a,$) is the real flag, not this: flag=";
    local_1e0 = 5;
    local_238 = 0x1000;
    local_234 = 6;
    _gfortran_st_write(&local_238);
    uVar1 = local_1c - 1;
    // This seems to do some math on that byte. 
    local_21 = (char)local_20 -
               ((char)uVar1 +
                ((byte)((ulong)(uVar1 ^ (int)uVar1 >> 0x1f) * 0x55555556 >> 0x20) ^
                (byte)((int)uVar1 >> 0x1f)) * -3 + -1);
    _gfortran_transfer_character_write(&local_238,&local_21,1);
    _gfortran_st_write_done(&local_238);
  }
  local_230 = "main.f90";
  local_228 = 0x15;
  local_1e8 = "(a,$) is the real flag, not this: flag=";
  local_1e0 = 5;
  local_238 = 0x1000;
  local_234 = 6;
  _gfortran_st_write(&local_238);
  _gfortran_transfer_character_write(&local_238," is the real flag, not this: flag=",0x1d);
  _gfortran_st_write_done(&local_238);
  return;
}
```

So all this hints that this function does something with the encrypted flag. So I make [a python script](./solve.py) to reverse the flag.

```python
flag="gemredsf|k3oFe`r1E2n`e02j_qqoh`MNdR8d_j^Fpqts`n`80~"

for i in range(len(flag)):
    letter=ord(flag[i])
    letterTransformed = letter - (i + (((i ^ i >> 0x1f) * 0x55555556 >> 0x20) ^ (i >> 0x1f)) * -3 + -1)

    print(chr(letterTransformed), end="")
```

And that prints the flag

# Flag

```
helsectf{l3nGe_s1D3n_f01k_progaMMeR7e_i_Fortran_90}
```