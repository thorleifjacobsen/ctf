            ;-- rip:
            ; DATA XREF from entry0 @ 0x10d8
/ 1333: int main (uint32_t argc, char **argv);
|           ; var char **var_a0h @ rbp-0xa0
|           ; var uint32_t var_94h @ rbp-0x94
|           ; var int64_t var_8ch @ rbp-0x8c
|           ; var int64_t var_8bh @ rbp-0x8b
|           ; var int64_t var_8ah @ rbp-0x8a
|           ; var int64_t var_89h @ rbp-0x89
|           ; var int64_t var_88h @ rbp-0x88
|           ; var int64_t var_87h @ rbp-0x87
|           ; var int64_t var_86h @ rbp-0x86
|           ; var int64_t var_85h @ rbp-0x85
|           ; var int64_t var_84h @ rbp-0x84
|           ; var int64_t var_83h @ rbp-0x83
|           ; var int64_t var_82h @ rbp-0x82
|           ; var int64_t var_81h @ rbp-0x81
|           ; var int64_t var_80h @ rbp-0x80
|           ; var int64_t var_7fh @ rbp-0x7f
|           ; var int64_t var_7eh @ rbp-0x7e
|           ; var int64_t var_7dh @ rbp-0x7d
|           ; var int64_t var_7ch @ rbp-0x7c
|           ; var int64_t var_7bh @ rbp-0x7b
|           ; var int64_t var_7ah @ rbp-0x7a
|           ; var int64_t var_79h @ rbp-0x79
|           ; var int64_t var_78h @ rbp-0x78
|           ; var int64_t var_77h @ rbp-0x77
|           ; var int64_t var_76h @ rbp-0x76
|           ; var int64_t var_75h @ rbp-0x75
|           ; var int64_t var_74h @ rbp-0x74
|           ; var int64_t var_73h @ rbp-0x73
|           ; var int64_t var_72h @ rbp-0x72
|           ; var int64_t var_71h @ rbp-0x71
|           ; var int64_t var_70h @ rbp-0x70
|           ; var int64_t var_6fh @ rbp-0x6f
|           ; var int64_t var_6eh @ rbp-0x6e
|           ; var int64_t var_6dh @ rbp-0x6d
|           ; var int64_t var_6ch @ rbp-0x6c
|           ; var int64_t var_6bh @ rbp-0x6b
|           ; var int64_t var_6ah @ rbp-0x6a
|           ; var int64_t var_69h @ rbp-0x69
|           ; var int64_t var_68h @ rbp-0x68
|           ; var int64_t var_67h @ rbp-0x67
|           ; var int64_t var_66h @ rbp-0x66
|           ; var int64_t var_65h @ rbp-0x65
|           ; var int64_t var_64h @ rbp-0x64
|           ; var int64_t var_63h @ rbp-0x63
|           ; var int64_t var_62h @ rbp-0x62
|           ; var int64_t var_61h @ rbp-0x61
|           ; var int64_t var_60h @ rbp-0x60
|           ; var signed int64_t var_5ch @ rbp-0x5c
|           ; var char *s @ rbp-0x58
|           ; var char *var_50h @ rbp-0x50
|           ; var int64_t var_48h @ rbp-0x48
|           ; var int64_t var_40h @ rbp-0x40
|           ; var int64_t var_38h @ rbp-0x38
|           ; var int64_t var_35h @ rbp-0x35
|           ; var int64_t var_2dh @ rbp-0x2d
|           ; var int64_t var_18h @ rbp-0x18
|           ; var int64_t var_8h @ rbp-0x8
|           ; arg uint32_t argc @ rdi
|           ; arg char **argv @ rsi
|           0x0000124b      f30f1efa       endbr64
|           0x0000124f      55             push rbp
|           0x00001250      4889e5         mov rbp, rsp
|           0x00001253      53             push rbx
|           0x00001254      4881ec980000.  sub rsp, 0x98
|           0x0000125b      89bd6cffffff   mov dword [var_94h], edi    ; argc
|           0x00001261      4889b560ffff.  mov qword [var_a0h], rsi    ; argv
|           0x00001268      64488b042528.  mov rax, qword fs:[0x28]
|           0x00001271      488945e8       mov qword [var_18h], rax
|           0x00001275      31c0           xor eax, eax
|           0x00001277      b800000000     mov eax, 0
|           0x0000127c      e828ffffff     call sym.dont_buffer
|           0x00001281      488d05882d00.  lea rax, obj.msg            ; 0x4010 ; "here is the flag: "
|           0x00001288      4889c7         mov rdi, rax                ; const char *s
|           0x0000128b      e8f0fdffff     call sym.imp.puts           ; int puts(const char *s)
|           0x00001290      488d056d0d00.  lea rax, str.1337           ; 0x2004 ; "1337"
|           0x00001297      488945a8       mov qword [s], rax
|           0x0000129b      83bd6cffffff.  cmp dword [var_94h], 2
|       ,=< 0x000012a2      7516           jne 0x12ba
|       |   0x000012a4      48838560ffff.  add qword [var_a0h], 8
|       |   0x000012ac      488b8560ffff.  mov rax, qword [var_a0h]
|       |   0x000012b3      488b00         mov rax, qword [rax]
|       |   0x000012b6      488945a8       mov qword [s], rax
|       |   ; CODE XREF from main @ 0x12a2
|       `-> 0x000012ba      48c745b00000.  mov qword [var_50h], 0
|           0x000012c2      48c745b80000.  mov qword [var_48h], 0
|           0x000012ca      48c745c00000.  mov qword [var_40h], 0
|           0x000012d2      48c745c80000.  mov qword [var_38h], 0
|           0x000012da      48c745cb0000.  mov qword [var_35h], 0
|           0x000012e2      48c745d30000.  mov qword [var_2dh], 0
|           0x000012ea      c68574ffffff.  mov byte [var_8ch], 0x58    ; 'X'
|           0x000012f1      c68575ffffff.  mov byte [var_8bh], 0x40    ; elf_phdr
|           0x000012f8      c68576ffffff.  mov byte [var_8ah], 0x6c    ; 'l'
|           0x000012ff      c68577ffffff.  mov byte [var_89h], 0x52    ; 'R'
|           0x00001306      c68578ffffff.  mov byte [var_88h], 0x40    ; elf_phdr
|           0x0000130d      c68579ffffff.  mov byte [var_87h], 0x55    ; 'U'
|           0x00001314      c6857affffff.  mov byte [var_86h], 0x52    ; 'R'
|           0x0000131b      c6857bffffff.  mov byte [var_85h], 0x5b    ; '['
|           0x00001322      c6857cffffff.  mov byte [var_84h], 0x40    ; elf_phdr
|           0x00001329      c6857dffffff.  mov byte [var_83h], 0x5b    ; '['
|           0x00001330      c6857effffff.  mov byte [var_82h], 0x5b    ; '['
|           0x00001337      c6857fffffff.  mov byte [var_81h], 0x4e    ; 'N'
|           0x0000133e      c6458058       mov byte [var_80h], 0x58    ; 'X'
|           0x00001342      c6458154       mov byte [var_7fh], 0x54    ; 'T'
|           0x00001346      c6458243       mov byte [var_7eh], 0x43    ; 'C'
|           0x0000134a      c6458345       mov byte [var_7dh], 0x45    ; 'E'
|           0x0000134e      c6458447       mov byte [var_7ch], 0x47    ; 'G'
|           0x00001352      c6458554       mov byte [var_7bh], 0x54    ; 'T'
|           0x00001356      c645866e       mov byte [var_7ah], 0x6e    ; 'n'
|           0x0000135a      c6458743       mov byte [var_79h], 0x43    ; 'C'
|           0x0000135e      c6458845       mov byte [var_78h], 0x45    ; 'E'
|           0x00001362      c645896c       mov byte [var_77h], 0x6c    ; 'l'
|           0x00001366      c6458a50       mov byte [var_76h], 0x50    ; 'P'
|           0x0000136a      c6458b5f       mov byte [var_75h], 0x5f    ; '_'
|           0x0000136e      c6458c6c       mov byte [var_74h], 0x6c    ; 'l'
|           0x00001372      c6458d41       mov byte [var_73h], 0x41    ; 'A'
|           0x00001376      c6458e40       mov byte [var_72h], 0x40    ; elf_phdr
|           0x0000137a      c6458f5c       mov byte [var_71h], 0x5c    ; '\\'
|           0x0000137e      c645905a       mov byte [var_70h], 0x5a    ; 'Z'
|           0x00001382      c6459154       mov byte [var_6fh], 0x54    ; 'T'
|           0x00001386      c6459248       mov byte [var_6eh], 0x48    ; 'H'
|           0x0000138a      c6459354       mov byte [var_6dh], 0x54    ; 'T'
|           0x0000138e      c6459456       mov byte [var_6ch], 0x56    ; 'V'
|           0x00001392      c6459558       mov byte [var_6bh], 0x58    ; 'X'
|           0x00001396      c6459655       mov byte [var_6ah], 0x55    ; 'U'
|           0x0000139a      c6459740       mov byte [var_69h], 0x40    ; elf_phdr
|           0x0000139e      c6459845       mov byte [var_68h], 0x45    ; 'E'
|           0x000013a2      c645995e       mov byte [var_67h], 0x5e    ; '^'
|           0x000013a6      c6459a6c       mov byte [var_66h], 0x6c    ; 'l'
|           0x000013aa      c6459b5f       mov byte [var_65h], 0x5f    ; '_'
|           0x000013ae      c6459c6c       mov byte [var_64h], 0x6c    ; 'l'
|           0x000013b2      c6459d5d       mov byte [var_63h], 0x5d    ; ']'
|           0x000013b6      c6459e5b       mov byte [var_62h], 0x5b    ; '['
|           0x000013ba      0fbe957effff.  movsx edx, byte [var_82h]
|           0x000013c1      488d45b0       lea rax, [var_50h]
|           0x000013c5      89d6           mov esi, edx                ; int64_t arg2
|           0x000013c7      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000013ca      e83ffeffff     call sym.add
|           0x000013cf      0fbe5591       movsx edx, byte [var_6fh]
|           0x000013d3      488d45b0       lea rax, [var_50h]
|           0x000013d7      89d6           mov esi, edx                ; int64_t arg2
|           0x000013d9      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000013dc      e82dfeffff     call sym.add
|           0x000013e1      0fbe558b       movsx edx, byte [var_75h]
|           0x000013e5      488d45b0       lea rax, [var_50h]
|           0x000013e9      89d6           mov esi, edx                ; int64_t arg2
|           0x000013eb      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000013ee      e81bfeffff     call sym.add
|           0x000013f3      0fbe9578ffff.  movsx edx, byte [var_88h]
|           0x000013fa      488d45b0       lea rax, [var_50h]
|           0x000013fe      89d6           mov esi, edx                ; int64_t arg2
|           0x00001400      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001403      e806feffff     call sym.add
|           0x00001408      0fbe9577ffff.  movsx edx, byte [var_89h]
|           0x0000140f      488d45b0       lea rax, [var_50h]
|           0x00001413      89d6           mov esi, edx                ; int64_t arg2
|           0x00001415      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001418      e8f1fdffff     call sym.add
|           0x0000141d      0fbe558a       movsx edx, byte [var_76h]
|           0x00001421      488d45b0       lea rax, [var_50h]
|           0x00001425      89d6           mov esi, edx                ; int64_t arg2
|           0x00001427      4889c7         mov rdi, rax                ; int64_t arg1
|           0x0000142a      e8dffdffff     call sym.add
|           0x0000142f      0fbe5583       movsx edx, byte [var_7dh]
|           0x00001433      488d45b0       lea rax, [var_50h]
|           0x00001437      89d6           mov esi, edx                ; int64_t arg2
|           0x00001439      4889c7         mov rdi, rax                ; int64_t arg1
|           0x0000143c      e8cdfdffff     call sym.add
|           0x00001441      0fbe9579ffff.  movsx edx, byte [var_87h]
|           0x00001448      488d45b0       lea rax, [var_50h]
|           0x0000144c      89d6           mov esi, edx                ; int64_t arg2
|           0x0000144e      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001451      e8b8fdffff     call sym.add
|           0x00001456      0fbe5592       movsx edx, byte [var_6eh]
|           0x0000145a      488d45b0       lea rax, [var_50h]
|           0x0000145e      89d6           mov esi, edx                ; int64_t arg2
|           0x00001460      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001463      e8a6fdffff     call sym.add
|           0x00001468      0fbe5582       movsx edx, byte [var_7eh]
|           0x0000146c      488d45b0       lea rax, [var_50h]
|           0x00001470      89d6           mov esi, edx                ; int64_t arg2
|           0x00001472      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001475      e894fdffff     call sym.add
|           0x0000147a      0fbe957bffff.  movsx edx, byte [var_85h]
|           0x00001481      488d45b0       lea rax, [var_50h]
|           0x00001485      89d6           mov esi, edx                ; int64_t arg2
|           0x00001487      4889c7         mov rdi, rax                ; int64_t arg1
|           0x0000148a      e87ffdffff     call sym.add
|           0x0000148f      0fbe5581       movsx edx, byte [var_7fh]
|           0x00001493      488d45b0       lea rax, [var_50h]
|           0x00001497      89d6           mov esi, edx                ; int64_t arg2
|           0x00001499      4889c7         mov rdi, rax                ; int64_t arg1
|           0x0000149c      e86dfdffff     call sym.add
|           0x000014a1      0fbe9576ffff.  movsx edx, byte [var_8ah]
|           0x000014a8      488d45b0       lea rax, [var_50h]
|           0x000014ac      89d6           mov esi, edx                ; int64_t arg2
|           0x000014ae      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000014b1      e858fdffff     call sym.add
|           0x000014b6      0fbe5596       movsx edx, byte [var_6ah]
|           0x000014ba      488d45b0       lea rax, [var_50h]
|           0x000014be      89d6           mov esi, edx                ; int64_t arg2
|           0x000014c0      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000014c3      e846fdffff     call sym.add
|           0x000014c8      0fbe5595       movsx edx, byte [var_6bh]
|           0x000014cc      488d45b0       lea rax, [var_50h]
|           0x000014d0      89d6           mov esi, edx                ; int64_t arg2
|           0x000014d2      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000014d5      e834fdffff     call sym.add
|           0x000014da      0fbe558d       movsx edx, byte [var_73h]
|           0x000014de      488d45b0       lea rax, [var_50h]
|           0x000014e2      89d6           mov esi, edx                ; int64_t arg2
|           0x000014e4      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000014e7      e822fdffff     call sym.add
|           0x000014ec      0fbe957affff.  movsx edx, byte [var_86h]
|           0x000014f3      488d45b0       lea rax, [var_50h]
|           0x000014f7      89d6           mov esi, edx                ; int64_t arg2
|           0x000014f9      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000014fc      e80dfdffff     call sym.add
|           0x00001501      0fbe5594       movsx edx, byte [var_6ch]
|           0x00001505      488d45b0       lea rax, [var_50h]
|           0x00001509      89d6           mov esi, edx                ; int64_t arg2
|           0x0000150b      4889c7         mov rdi, rax                ; int64_t arg1
|           0x0000150e      e8fbfcffff     call sym.add
|           0x00001513      0fbe559a       movsx edx, byte [var_66h]
|           0x00001517      488d45b0       lea rax, [var_50h]
|           0x0000151b      89d6           mov esi, edx                ; int64_t arg2
|           0x0000151d      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001520      e8e9fcffff     call sym.add
|           0x00001525      0fbe5599       movsx edx, byte [var_67h]
|           0x00001529      488d45b0       lea rax, [var_50h]
|           0x0000152d      89d6           mov esi, edx                ; int64_t arg2
|           0x0000152f      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001532      e8d7fcffff     call sym.add
|           0x00001537      0fbe957cffff.  movsx edx, byte [var_84h]
|           0x0000153e      488d45b0       lea rax, [var_50h]
|           0x00001542      89d6           mov esi, edx                ; int64_t arg2
|           0x00001544      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001547      e8c2fcffff     call sym.add
|           0x0000154c      0fbe5586       movsx edx, byte [var_7ah]
|           0x00001550      488d45b0       lea rax, [var_50h]
|           0x00001554      89d6           mov esi, edx                ; int64_t arg2
|           0x00001556      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001559      e8b0fcffff     call sym.add
|           0x0000155e      0fbe5597       movsx edx, byte [var_69h]
|           0x00001562      488d45b0       lea rax, [var_50h]
|           0x00001566      89d6           mov esi, edx                ; int64_t arg2
|           0x00001568      4889c7         mov rdi, rax                ; int64_t arg1
|           0x0000156b      e89efcffff     call sym.add
|           0x00001570      0fbe5584       movsx edx, byte [var_7ch]
|           0x00001574      488d45b0       lea rax, [var_50h]
|           0x00001578      89d6           mov esi, edx                ; int64_t arg2
|           0x0000157a      4889c7         mov rdi, rax                ; int64_t arg1
|           0x0000157d      e88cfcffff     call sym.add
|           0x00001582      0fbe5588       movsx edx, byte [var_78h]
|           0x00001586      488d45b0       lea rax, [var_50h]
|           0x0000158a      89d6           mov esi, edx                ; int64_t arg2
|           0x0000158c      4889c7         mov rdi, rax                ; int64_t arg1
|           0x0000158f      e87afcffff     call sym.add
|           0x00001594      0fbe558f       movsx edx, byte [var_71h]
|           0x00001598      488d45b0       lea rax, [var_50h]
|           0x0000159c      89d6           mov esi, edx                ; int64_t arg2
|           0x0000159e      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000015a1      e868fcffff     call sym.add
|           0x000015a6      0fbe559b       movsx edx, byte [var_65h]
|           0x000015aa      488d45b0       lea rax, [var_50h]
|           0x000015ae      89d6           mov esi, edx                ; int64_t arg2
|           0x000015b0      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000015b3      e856fcffff     call sym.add
|           0x000015b8      0fbe5593       movsx edx, byte [var_6dh]
|           0x000015bc      488d45b0       lea rax, [var_50h]
|           0x000015c0      89d6           mov esi, edx                ; int64_t arg2
|           0x000015c2      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000015c5      e844fcffff     call sym.add
|           0x000015ca      0fbe559c       movsx edx, byte [var_64h]
|           0x000015ce      488d45b0       lea rax, [var_50h]
|           0x000015d2      89d6           mov esi, edx                ; int64_t arg2
|           0x000015d4      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000015d7      e832fcffff     call sym.add
|           0x000015dc      0fbe558e       movsx edx, byte [var_72h]
|           0x000015e0      488d45b0       lea rax, [var_50h]
|           0x000015e4      89d6           mov esi, edx                ; int64_t arg2
|           0x000015e6      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000015e9      e820fcffff     call sym.add
|           0x000015ee      0fbe5590       movsx edx, byte [var_70h]
|           0x000015f2      488d45b0       lea rax, [var_50h]
|           0x000015f6      89d6           mov esi, edx                ; int64_t arg2
|           0x000015f8      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000015fb      e80efcffff     call sym.add
|           0x00001600      0fbe5598       movsx edx, byte [var_68h]
|           0x00001604      488d45b0       lea rax, [var_50h]
|           0x00001608      89d6           mov esi, edx                ; int64_t arg2
|           0x0000160a      4889c7         mov rdi, rax                ; int64_t arg1
|           0x0000160d      e8fcfbffff     call sym.add
|           0x00001612      0fbe957dffff.  movsx edx, byte [var_83h]
|           0x00001619      488d45b0       lea rax, [var_50h]
|           0x0000161d      89d6           mov esi, edx                ; int64_t arg2
|           0x0000161f      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001622      e8e7fbffff     call sym.add
|           0x00001627      0fbe558c       movsx edx, byte [var_74h]
|           0x0000162b      488d45b0       lea rax, [var_50h]
|           0x0000162f      89d6           mov esi, edx                ; int64_t arg2
|           0x00001631      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001634      e8d5fbffff     call sym.add
|           0x00001639      0fbe5587       movsx edx, byte [var_79h]
|           0x0000163d      488d45b0       lea rax, [var_50h]
|           0x00001641      89d6           mov esi, edx                ; int64_t arg2
|           0x00001643      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001646      e8c3fbffff     call sym.add
|           0x0000164b      0fbe559e       movsx edx, byte [var_62h]
|           0x0000164f      488d45b0       lea rax, [var_50h]
|           0x00001653      89d6           mov esi, edx                ; int64_t arg2
|           0x00001655      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001658      e8b1fbffff     call sym.add
|           0x0000165d      0fbe9574ffff.  movsx edx, byte [var_8ch]
|           0x00001664      488d45b0       lea rax, [var_50h]
|           0x00001668      89d6           mov esi, edx                ; int64_t arg2
|           0x0000166a      4889c7         mov rdi, rax                ; int64_t arg1
|           0x0000166d      e89cfbffff     call sym.add
|           0x00001672      0fbe9575ffff.  movsx edx, byte [var_8bh]
|           0x00001679      488d45b0       lea rax, [var_50h]
|           0x0000167d      89d6           mov esi, edx                ; int64_t arg2
|           0x0000167f      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001682      e887fbffff     call sym.add
|           0x00001687      0fbe5589       movsx edx, byte [var_77h]
|           0x0000168b      488d45b0       lea rax, [var_50h]
|           0x0000168f      89d6           mov esi, edx                ; int64_t arg2
|           0x00001691      4889c7         mov rdi, rax                ; int64_t arg1
|           0x00001694      e875fbffff     call sym.add
|           0x00001699      0fbe5580       movsx edx, byte [var_80h]
|           0x0000169d      488d45b0       lea rax, [var_50h]
|           0x000016a1      89d6           mov esi, edx                ; int64_t arg2
|           0x000016a3      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000016a6      e863fbffff     call sym.add
|           0x000016ab      0fbe559d       movsx edx, byte [var_63h]
|           0x000016af      488d45b0       lea rax, [var_50h]
|           0x000016b3      89d6           mov esi, edx                ; int64_t arg2
|           0x000016b5      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000016b8      e851fbffff     call sym.add
|           0x000016bd      0fbe5585       movsx edx, byte [var_7bh]
|           0x000016c1      488d45b0       lea rax, [var_50h]
|           0x000016c5      89d6           mov esi, edx                ; int64_t arg2
|           0x000016c7      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000016ca      e83ffbffff     call sym.add
|           0x000016cf      0fbe957fffff.  movsx edx, byte [var_81h]
|           0x000016d6      488d45b0       lea rax, [var_50h]
|           0x000016da      89d6           mov esi, edx                ; int64_t arg2
|           0x000016dc      4889c7         mov rdi, rax                ; int64_t arg1
|           0x000016df      e82afbffff     call sym.add
|           0x000016e4      c745a0000000.  mov dword [var_60h], 0
|           0x000016eb      c745a4000000.  mov dword [var_5ch], 0
|       ,=< 0x000016f2      eb5b           jmp 0x174f
|       |   ; CODE XREF from main @ 0x1753
|      .--> 0x000016f4      8b45a0         mov eax, dword [var_60h]
|      :|   0x000016f7      4863d0         movsxd rdx, eax
|      :|   0x000016fa      488b45a8       mov rax, qword [s]
|      :|   0x000016fe      4801d0         add rax, rdx
|      :|   0x00001701      0fb600         movzx eax, byte [rax]
|      :|   0x00001704      88459f         mov byte [var_61h], al
|      :|   0x00001707      8b45a0         mov eax, dword [var_60h]
|      :|   0x0000170a      83c001         add eax, 1
|      :|   0x0000170d      4863d8         movsxd rbx, eax
|      :|   0x00001710      488b45a8       mov rax, qword [s]
|      :|   0x00001714      4889c7         mov rdi, rax                ; const char *s
|      :|   0x00001717      e874f9ffff     call sym.imp.strlen         ; size_t strlen(const char *s)
|      :|   0x0000171c      4889c1         mov rcx, rax
|      :|   0x0000171f      4889d8         mov rax, rbx
|      :|   0x00001722      ba00000000     mov edx, 0
|      :|   0x00001727      48f7f1         div rcx
|      :|   0x0000172a      4889d1         mov rcx, rdx
|      :|   0x0000172d      4889c8         mov rax, rcx
|      :|   0x00001730      8945a0         mov dword [var_60h], eax
|      :|   0x00001733      8b45a4         mov eax, dword [var_5ch]
|      :|   0x00001736      4898           cdqe
|      :|   0x00001738      0fb64405b0     movzx eax, byte [rbp + rax - 0x50]
|      :|   0x0000173d      32459f         xor al, byte [var_61h]
|      :|   0x00001740      89c2           mov edx, eax
|      :|   0x00001742      8b45a4         mov eax, dword [var_5ch]
|      :|   0x00001745      4898           cdqe
|      :|   0x00001747      885405b0       mov byte [rbp + rax - 0x50], dl
|      :|   0x0000174b      8345a401       add dword [var_5ch], 1
|      :|   ; CODE XREF from main @ 0x16f2
|      :`-> 0x0000174f      837da42a       cmp dword [var_5ch], 0x2a
|      `==< 0x00001753      7e9f           jle 0x16f4
|           0x00001755      488d45b0       lea rax, [var_50h]
|           0x00001759      4889c7         mov rdi, rax                ; const char *s
|           0x0000175c      e81ff9ffff     call sym.imp.puts           ; int puts(const char *s)
|           0x00001761      b800000000     mov eax, 0
|           0x00001766      488b55e8       mov rdx, qword [var_18h]
|           0x0000176a      64482b142528.  sub rdx, qword fs:[0x28]
|       ,=< 0x00001773      7405           je 0x177a
|       |   0x00001775      e826f9ffff     call sym.imp.__stack_chk_fail
|       |   ; CODE XREF from main @ 0x1773
|       `-> 0x0000177a      488b5df8       mov rbx, qword [var_8h]
|           0x0000177e      c9             leave
\           0x0000177f      c3             ret