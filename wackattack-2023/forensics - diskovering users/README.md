# Diskovering Users (beginner)

I think the user had something going on. Could you look into it?

Author: taschmex

Download: http://ctf.wackattack.eu/static/diskovery.img.gz

# Writeup

Quickly checking the image

```
└─$ file diskovery.img
diskovery.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0x2c,190,18), startsector 2048, 716800 sectors
```

Mounting it on my computer 

```
└─$ sudo mount -t ext4 -o loop,offset=$((2048 * 512)) diskovery.img /mnt/ctfchallenge
```

Now inside the home folder there is a user with a flag file:

# Flag

```
wack{w0W_5uCh_Im4g3_mUCh_di5k}
```