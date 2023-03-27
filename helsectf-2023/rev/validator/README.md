# validator (498)

Du kan validere om du vet flagget, eller ikke.

# Writeup

Opened this in Ghidra showing this main command:

```cpp
undefined8 main(void) {
  int iVar1;
  undefined local_28 [32];
  
  printf("Skriv inn flagget: ");
  fread(local_28,0x1f,1,stdin);
  iVar1 = valid(local_28);
  if (iVar1 == 0) {
    puts("Nei, det var ikke riktig.");
  }
  else {
    printf("Gratulerer, du vet flagget! :-)");
  }
  return 0;
}
```

Following it checking the "valid" function

```cpp
undefined8 valid(long param_1) {
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined4 local_20;
  undefined2 local_1c;
  int local_c;
  
  local_38 = 0x584d5241515a4448;
  local_30 = 0x6e686c466e4e5264;
  local_28 = 0x6e746b685269736d;
  local_20 = 0x75516852;
  local_1c = 0x6671;
  local_c = 0;
  while( true ) {
    if (0x1d < local_c) {
      return 1;
    }
    if ((char)(*(byte *)(param_1 + (long)local_c + 1) ^ *(byte *)(param_1 + local_c)) + 0x3b !=
        (int)*(char *)((long)&local_38 + (long)local_c)) break;
    local_c = local_c + 1;
  }
  return 0;
}
```

Seeing quickly it seems to be `0x1d (29)` characters. Loops trough and check each characters agains a formula.  Converting this to python for easy reading and removing unessesary things:

```python
def validator(flag):
  flag = flag.encode() # Convert flag to bytes
  count = 0

  ct = bytearray(bytes.fromhex("6671" + "75516852" + "6e746b685269736d" + "6e686c466e4e5264" + "584d5241515a4448"))[::-1]

  while True:
    if 0x1d < count:
      return True

    if (flag[count+1] ^ flag[count]) + 0x3b != int(ct[count]):
      break

    count += 1
  return False
```

So I feel like the only method to do this is brute? I can make something that runs from the start character "h" and adds one character and checks that with the sum until I have a flag? Well lets do this:

```python
# Added 0000 padding to counter out of bounds.
ct = bytearray(bytes.fromhex("0000" + "6671" + "75516852" + "6e746b685269736d" + "6e686c466e4e5264" + "584d5241515a4448"))[::-1]

testFlag = "helsectf{" # I know this part, save some time.

for l in range(0,100):
  for nextByte in range(32,127):
    prevByte = ord(testFlag[-1]) # Last letter
   
    if (prevByte ^ nextByte) + 0x3b == int(ct[len(testFlag)-1]):
      testFlag += chr(nextByte)
      print(testFlag)
      break    
```

Yields:

```
helsectf{R
helsectf{RE
helsectf{REV
helsectf{REVe
helsectf{REVen
helsectf{REVen_
helsectf{REVen_r
helsectf{REVen_rA
helsectf{REVen_rAs
helsectf{REVen_rAsK
helsectf{REVen_rAsKe
helsectf{REVen_rAsKer
helsectf{REVen_rAsKer_
helsectf{REVen_rAsKer_o
helsectf{REVen_rAsKer_oV
helsectf{REVen_rAsKer_oVe
helsectf{REVen_rAsKer_oVer
helsectf{REVen_rAsKer_oVer_
helsectf{REVen_rAsKer_oVer_I
helsectf{REVen_rAsKer_oVer_Is
helsectf{REVen_rAsKer_oVer_IsE
helsectf{REVen_rAsKer_oVer_IsEn
```

Do not have enough data to find more, so guessing `}` is the last. The validator program did accept that without the `}` due to the if'check in the start of the while loop. So adding a `}` and submitting. Green light! Wohoo

# Flag

```
helsectf{REVen_rAsKer_oVer_IsEn}
```