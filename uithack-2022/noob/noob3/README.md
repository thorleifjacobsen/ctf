# Noob3

The right man in the wrong place can make all the difference in the world.

The username for this , is noob3.
The server name is wwww.limewire.td.org.uit.no.
Password is noob2's flag



# Writeup

Su'ed to noob3 and entered the flag as password. A zip file here. Downloaded it to my pc using scp and unzipped it.

Inside was flag.out which is an elf, strings and grep got the flag.

```bash
└─$ file flag.out   flag.out: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=386199a50ce6470d89dff48c083217803ab4613f, for GNU/Linux 3.2.0, not stripped

└─$ strings flag.out | grep -i uit
                                               .........***,*(*,,,,,,.... ....,,,*********//**(//////*/(#%&%#######.      UiTHack23{RiseAndShineMrFreeman}                            
                                                      
```