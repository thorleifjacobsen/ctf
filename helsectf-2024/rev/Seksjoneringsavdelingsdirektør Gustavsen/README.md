# Seksjoneringsavdelingsdirektør Gustavsen

De jobber i feil seksjon, hr. Gustavsen!

[⬇ gustavsen](./gustavsen)

# Writeup

When running this elf you get a message that you're in the wrong section. After a quick google I learned about the sections of the ELF. Using `readelf -S gustavsen` I got this (removed some unessesary data)

```
There are 39 section headers, starting at offset 0x4a80:

Section Headers:
  [Nr] Name              Type             Address           Offset
       Size              EntSize          Flags  Link  Info  Align
  [ 0]                   NULL             0000000000000000  00000000
  [ 1] .interp           PROGBITS         0000000000000318  00000318
  [ 2] .note.gnu.pr[...] NOTE             0000000000000338  00000338
  [ 3] .note.gnu.bu[...] NOTE             0000000000000368  00000368
  [ 4] .note.ABI-tag     NOTE             000000000000038c  0000038c
  [ 5] .gnu.hash         GNU_HASH         00000000000003b0  000003b0
  [ 6] .dynsym           DYNSYM           00000000000003d8  000003d8
  [ 7] .dynstr           STRTAB           00000000000005d0  000005d0
  [ 8] .gnu.version      VERSYM           00000000000006ec  000006ec
  [ 9] .gnu.version_r    VERNEED          0000000000000718  00000718
  [10] .rela.dyn         RELA             0000000000000768  00000768
  [11] .rela.plt         RELA             0000000000000840  00000840
  [12] .init             PROGBITS         0000000000001000  00001000
  [13] .plt              PROGBITS         0000000000001020  00001020
  [14] .plt.got          PROGBITS         0000000000001110  00001110
  [15] .plt.sec          PROGBITS         0000000000001120  00001120
  [16] .text             PROGBITS         0000000000001200  00001200
  [17] .fini             PROGBITS         000000000000169c  0000169c
  [18] .rodata           PROGBITS         0000000000002000  00002000
  [19] .eh_frame_hdr     PROGBITS         0000000000002084  00002084
  [20] .eh_frame         PROGBITS         00000000000020c0  000020c0
  [21] .init_array       INIT_ARRAY       0000000000003d40  00002d40
  [22] .fini_array       FINI_ARRAY       0000000000003d48  00002d48
  [23] .dynamic          DYNAMIC          0000000000003d50  00002d50
  [24] .got              PROGBITS         0000000000003f50  00002f50
  [25] .data             PROGBITS         0000000000004000  00003000
  [26] .bss              NOBITS           0000000000004020  00003010
  [27] .comment          PROGBITS         0000000000000000  00003010
  [28] .debug_aranges    PROGBITS         0000000000000000  0000303b
  [29] .debug_info       PROGBITS         0000000000000000  0000306b
  [30] .debug_abbrev     PROGBITS         0000000000000000  00003773
  [31] .debug_line       PROGBITS         0000000000000000  00003967
  [32] .debug_str        PROGBITS         0000000000000000  00003b02
  [33] .debug_line_str   PROGBITS         0000000000000000  00003f92
  [34] .pewpew           PROGBITS         0000000000000000  000040d0
  [35] .symdata          PROGBITS         0000000000000000  00004100
  [36] .symtab           SYMTAB           0000000000000000  00004138
  [37] .strtab           STRTAB           0000000000000000  00004600
  [38] .shstrtab         STRTAB           0000000000000000  00004901
```

What caught my attention was that `.pewpew`. It sounds unusual. I tried to dump it with `objdump -s -j .pewpew gustavsen` and got this:

```
gustavsen:     file format elf64-x86-64

Contents of section .pewpew:
 0000 faaafeee 12345678 56517612 7d56341d  .....4VxVQv.}V4.
 0010 60143f58 74513f14 32473313 615e3916  `.?XtQ?.2G3.a^9.
 0020 3e143e0a 3c14110d 6140370e 61513859  >.>.<...a@7.aQ8Y
```

That gave me nothing, so I decompiled the elf with IDA to find [main.c](main.ida.c). Walking through this code with a lot of googling every function it seems to start by getting the first argument of the file `elf_file = *argv;` which always are itself. Then it opens that file, using some elf functions. 

Then it reads all the sections until it finds a section that starts with a magic number. When it does it extracts a key and xor's the rest of the section with that key. Then it prints the result.

```c
magic = -285299974;
if ( *(_DWORD *)section_data == -285299974 ) {
    key = *((_DWORD *)section_data + 1);
    data = xor(section_data + 8, shdr.sh_size - 8, (char *)&key);
    puts(data);
    free(section_data);
    free(data);
    elf_end(elf);
    close(fd);
    return 0;
}
```

I could not find this magic number anywhere but using Ghidra to see [main.c](main.ghidra.c] it shows this on the same spot:

```c
local_3c = 0xeefeaafa;
if (*local_38 == -0x11015506) {
    local_8c = local_38[1];
    local_48 = (char *)xor(local_38 + 2,local_68 - 8,&local_8c);
    puts(local_48);
    free(local_38);
    free(local_48);
    elf_end(local_28);
    close(local_1c);
}
```

This matches the start bytes of the `.pewpew` section with different endianess. `faaafeee 12345678 56517612 7d56341d` and the second 4 bytes are the key `12345678`. Using this logic where you got 4 bytes magic, 4 bytes key I wrote the python script to xor the data:

```python
from pwn import *
import string

context.log_level = 'warn'

# Function to perform XOR operation
def xor(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

# Is printable
def isPrintable(bytes):
    for byte in bytes:
        if byte < 32 or 128 < byte:
            return False
    return True

# Process each ELF file in the current directory
elf = ELF("./gustavsen")

# Iterate through sections in the ELF file
for section in elf.iter_sections():
    # Get the data from the section
    section_data = section.data()

    # Assuming the magic number and key are the first 8 bytes
    magic = section_data[:4]
    key = section_data[4:8]
    data_to_xor = section_data[8:]

    # XOR the data with the key
    result = xor(data_to_xor, key)

    # Check if data contains unprintable characters
    if not isPrintable(result):
        continue

    result = result.decode()
    print(f"Section {section.name}: ", end="")
    print(result)
```

which resulted in this:

```bash
$ python3 solve.py 
Section : 
Section .init_array: 
Section .fini_array: 
Section .pewpew: De jobber i feil seksjon, hr. Gustavsen!
Section .symdata: helsectf{eg_er_i_ein_seksjon_hr_Gustavsen}
```

# Flag

```
helsectf{eg_er_i_ein_seksjon_hr_Gustavsen}
```