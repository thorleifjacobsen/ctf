# Hide and Seek

Som følge av et stadig økende trusselbilde, spesielt ifra sydligere strøk, har Nordpolar sikkerhetstjeneste etablert en intern enhet som skal beskytte tjenestens egne digitale systemer mot angrep. Enheten består av nøye selekterte tidligere alveteknologer som har god erfaring med bekjempelse av sydpolare aktører.

Grunnet tidligere prestasjoner på Nordpolen har NISSEN selv navngitt enheten til Julens Utvalgte Lærde Elektronisk databehandlende Sikkerhets og Operative Center, forkortet JULESOC. JULESOCen kan blant annet bidra til å finne ondsinnede fugler i datasystemene til Julenissens verksted, grave i sildcoin transaksjoner og analyse av speilglatte kopier.

JULESOC har nylig mottatt en speilkopi av en arbeidsstasjon lokalisert på Julenissens verksted. Det er mistanke om at noen uautoriserte har vært inne på maskinen og tukla. Vi trenger at du graver frem noen spor.

- Mellomleder

📎image.raw.gz

# Writeup

Unpacking the image then running file reveals the following:

```
$ file image.raw 
image.raw: DOS/MBR boot sector; partition 1 : ID=0x83, start-CHS (0x0,32,33), end-CHS (0x19,159,6), startsector 2048, 409600 sectors; partition 2 : ID=0x83, start-CHS (0x19,159,7), end-CHS (0x4c,157,17), startsector 411648, 819200 sectors; partition 3 : ID=0x83, start-CHS (0x4c,157,18), end-CHS (0x66,28,54), startsector 1230848, 409600 sectors
```

So lets start with partition 1:

```bash
$ mkdir mount
$ sudo mount -o loop,offset=$((2048*512)) image.raw ./mount
```

First partition only gave me a QR Code with a google search:

```
https://www.google.com/search?channel=fs&client=ubuntu-sn&q=YmxpbmRzcG9yIGRlc3N2ZXJyZSwgbGV0IHZpZGVyZQ%3D%3D
```

The base64 tells you that this is a blind track. So lets look at the second partition:

```bash
$ sudo umount mount
$ sudo mount -o loop,offset=$((411648*512)) image.raw ./mount
```

Here is a santa code generator, a santa text with some curly braces. But lets look at the third one first:

```bash
$ sudo umount mount
$ sudo mount -o loop,offset=$((1230848*512)) image.raw ./mount
```

So what I have is this:

```
└── partitions
    ├── 1
    │   ├── Documents
    │   ├── lost+found
    │   └── Pictures
    │       └── qr-code.png
    ├── 2
    │   ├── backup1
    │   ├── gammelt
    │   ├── lost+found
    │   ├── nissetekst
    │   └── programmer
    │       └── nissekodegenerator.py
    └── 3
        └── hemmelig
            └── code
```

