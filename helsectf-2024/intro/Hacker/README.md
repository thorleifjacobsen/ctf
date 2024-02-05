# Hacker

Lyst å hacke sykehus og kommuner? Liker du å grave til du treffer fjell? Har du lyst å finne, teste og rapportere om svakheter som kan ha stor indirekte samfunnsmessig effekt? Vi i Helse- og KommuneCERT ønsker å styrke vårt red-team. Se om du tar vår utfordring:

https://www.finn.no/job/fulltime/ad.html?finnkode=336880016

# Writeup

On the ad there was a single line of assembly. (I see later on that it has been expanded to be a bit more clean). I tried to clean it up like this:

```nasm
global _start
section .text 

global _start
section .data 

hemmelig db 0x2a,0x27,0x2e,0x31,0x27,0x21,0x36,0x24,\
            0x39,0x31,0x36,0x23,0x36,0x31,0x23,0x37,\
            0x36,0x2d,0x30,0x2b,0x31,0x27,0x30,0x36,\
            0x1d,0x2a,0x23,0x21,0x29,0x27,0x30,0x3f,\
            0x48 

_fix: 
    mov eax, [hemmelig + ecx] ; Load byte 0 from hemmelig into eax
    xor edi, edi              ; xor edi to 0
    add edi, 0x41             ; add 0x41 to edi
    add edi, 1                ; add 1 to edi, edi is now 0x42
    xor eax, edi              ; xor eax with edi
    mov [hemmelig+ecx], al    ; store the result in same byte position for hemmelig
    add ecx, 1                ; increment ecx by 1
    mov esi, 0x21             ; move 0x21 to esi
    cmp ecx, esi              ; compare ecx with esi
    jle _fix                  ; if ecx is less than or equal to esi jump to _fix
    ret                       ; if not it will return to the caller 
  
_start: 
    xor ecx, ecx              ; xor a number with itself is 0
    call _fix                 ; call the fix function
    mov eax, 4                ; move 4 to eax
    mov ebx, 1                ; move 1 to ebx
    mov ecx, hemmelig         ; move the address of hemmelig to ecx
    mov edx, 0x21             ; move 0x21 to edx
    int 0x80                  ; call the kernel
    mov eax, 1                ; move 1 to eax
    xor ebx,ebx               ; xor ebx with itself is 0
    int 0x80                  ; call the kernel
```

By the looks of it t seems like it loads one byte from the `hemmelig` variable and then XOR's it with `0x42` and then stores it back in the same position. It does this 0x21 times. So I wrote a [script](solve.py) to do this for me.

```python
#!/usr/bin/env python3
b=[0x2a,0x27,0x2e,0x31,0x27,0x21,0x36,0x24,0x39,0x31,0x36,0x23,0x36,0x31,0x23,0x37,0x36,0x2d,0x30,0x2b,0x31,0x27,0x30,0x36,0x1d,0x2a,0x23,0x21,0x29,0x27,0x30,0x3f,0x48]
for i in range(0x21):
    b[i] ^= 0x42

# convert to ascii
print(''.join([chr(x) for x in b]))
```

# Flag

```
helsectf{statsautorisert_hacker}
```