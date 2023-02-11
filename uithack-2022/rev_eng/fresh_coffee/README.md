# Fresh Coffee

I wrote a program to start the coffee machine. I was so tired that I forgot the key to start the machine. Can you help me find the key?

# Writeup

Loaded the Keygen.class in Ghidra and found a "checkPassword" command 

```java
boolean checkPassword_java.lang.String_boolean(Keygen this,String param1)

{
  int iVar1;
  char cVar2;
  
  iVar1 = param1.length();
  if ((((((iVar1 == 0x21) && (cVar2 = param1.charAt(2), cVar2 == 'n')) &&
        (cVar2 = param1.charAt(0x1c), cVar2 == 'f')) &&
       (((cVar2 = param1.charAt(3), cVar2 == 'T' && (cVar2 = param1.charAt(0xc), cVar2 == '_')) &&
        ((cVar2 = param1.charAt(0x1d), cVar2 == '0' &&
         ((cVar2 = param1.charAt(6), cVar2 == '3' && (cVar2 = param1.charAt(0x18), cVar2 == 'u')))))
        ))) && (cVar2 = param1.charAt(0x10), cVar2 == '_')) &&
     (((((((cVar2 = param1.charAt(8), cVar2 == 'l' && (cVar2 = param1.charAt(0), cVar2 == 'd')) &&
          (cVar2 = param1.charAt(10), cVar2 == 'm')) &&
         ((cVar2 = param1.charAt(9), cVar2 == '_' && (cVar2 = param1.charAt(0xb), cVar2 == '3'))))
        && (cVar2 = param1.charAt(0xd), cVar2 == 'y')) &&
       ((((cVar2 = param1.charAt(0x17), cVar2 == 'r' && (cVar2 = param1.charAt(0x1e), cVar2 == 'r'))
         && (((cVar2 = param1.charAt(0xf), cVar2 == 'u' &&
              (((cVar2 = param1.charAt(0xe), cVar2 == '0' &&
                (cVar2 = param1.charAt(1), cVar2 == '0')) &&
               (cVar2 = param1.charAt(0x11), cVar2 == 'u')))) &&
             (((cVar2 = param1.charAt(0x14), cVar2 == 'd' &&
               (cVar2 = param1.charAt(0x1f), cVar2 == 'c')) &&
              (cVar2 = param1.charAt(0x12), cVar2 == 's')))))) &&
        ((cVar2 = param1.charAt(0x13), cVar2 == '3' && (cVar2 = param1.charAt(0x15), cVar2 == '_')))
        ))) && (((cVar2 = param1.charAt(5), cVar2 == 't' &&
                 (((cVar2 = param1.charAt(0x16), cVar2 == 'b' &&
                   (cVar2 = param1.charAt(4), cVar2 == '_')) &&
                  (cVar2 = param1.charAt(0x19), cVar2 == 't')))) &&
                (((cVar2 = param1.charAt(0x1b), cVar2 == '_' &&
                  (cVar2 = param1.charAt(7), cVar2 == 'l')) &&
                 ((cVar2 = param1.charAt(0x1a), cVar2 == '3' &&
                  (cVar2 = param1.charAt(0x20), cVar2 == '3')))))))))) {
    return true;
  }
  return false;
}
```

Manually made this reversed script:

```javascript
let char = []
char[2] = "n"
char[0x1c] = "f"
char[3] = "T"
char[0xc] = "_"
char[0x1d] = "0"
char[6] = "3"
char[0x18] = "u"
char[0x10] = "_"
char[8] = "l"
char[0] = "d"
char[10] = "m"
char[9] = "_"
char[0xb] = "3"
char[0xd] = "y"
char[0x17] = "r"
char[0x1e] = "r"
char[0xf] = "u"
char[0xe] = "0"
char[1] = "0"
char[0x11] = "u"
char[0x14] = "d"
char[0x1f] = "c"
char[0x12] = "s"
char[0x13] = "3"
char[0x15] = "_"
char[5] = "t"
char[0x16] = "b"
char[4] = "_"
char[0x19] = "t"
char[0x1b] = "_"
char[0x1b] = "_"
char[7] = "l"
char[0x1a] = "3"
char[0x20] = "3"
console.log(char.join(""))
```

Output when running:

```
d0nT_t3ll_m3_y0u_us3d_brut3_f0rc3
```

Guessed that I should surrender it with UiTHack23{...} and that was correct. Flag was:

```
UiTHack23{d0nT_t3ll_m3_y0u_us3d_brut3_f0rc3}
```