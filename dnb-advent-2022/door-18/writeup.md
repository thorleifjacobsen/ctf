# Challenge

So we managed to get a rootkit onto the Grinch's computer. We exfiltrated some files. I wonder what secrets they hide?

https://htbbinaries.z1.web.core.windows.net/grinchfiles.gz

> **Hint:** Stegosaurus comes to mind... but wait is there more?

# Writeup

Unpacked the gz file with ```gzip -d grinchfiles.gz```, this gave me grinchfiles. When running ```file grinchfiles``` it says ```grinchfiles: POSIX tar archive (GNU)``` so ```tar xvf grinchfiles``` and I have data. Regretting the V flag.... Takes ages..

First I started to do a base64 run on all the files in .secret/.docs. Script ran through and decoded all and outputted the text if it was ascii character only. No dice. 

Then I started with the two equal photos, xor images gave me a text, then adjust some levels and I got "Not all your base belong to 64..." 

We also have all those files:

```
doc2235P5OXL6735LLPJOFKPB4HQ7ZYHVK4OJO26GYJH367QLAS67V2NBATFUUUKAUKS2LK6CNTTDJHYPQFS26ZUG5JLMELC6W5V5XVGSCFNPIRFJWUFQ6DPS5VKYWSYXFNXJQUVSZFN5XCDBJAZS265JR3DHKOZNE4F7LTPQFVCKJTODMAZKSVQILHMEZK7ARYYW2O7K53426KM===.txt

doc225XKQZYKOG7B2AGWPBEJV2LDR3ZDJOU6V5CK4AJE4YLWR73PDJQQ36KWVOK5V6L5NVRA4NNCFY5XD5SKCYHRICQKEHQPVKSQLUWRPI5ZXG4F3L6POX6XSWMWVYG4DKZRUUWBPLVWBJQTO5X7V3HY7F4SVJAAWVX6X5PV7OYH6HPWOYR7JYUI6FNWIEHPR5SVTW54QLFLGLVU===.txt
```

Seems like they are ```doc<hash>.txt```. Doing base64 does not give anything neither does any other I feel like. I'm continuing.

In docs the `drunk.doc` is actually a image, renamed to `drunk.jpg`. The exif data says:

```
Author                          : WCH says: KNGEUQCGOBBTM7KAIVZUAPZWFI3EKTQ=
```

Into cyberchef testing different bases, hit on base32. Seems like something, so running a rot13, nothing, rot47! Bingo.. 

```
${youAreNotDoneYet}
```

As there is 2.5 attempts on this flagg I guess many jumped the gun so I'll take his word for it.

A bit of coop with DoS shows me the key.pdf is actually an image. I did extract it but gave me a zlib file. But he just altered the header to the pdf header and bingo.

Now seeing that key.png is actually the image from the photos. I tell him maybe we should xor the image with the puzzle pieces. So I put my girlfriend together with the key.png and all the pices into photoshop. After 10-15 minutes she puzzled the image. I save it and send it to DoS and try to use stego app to xor them. And there is some text, impossible to read with the app I have. I'm cooking so not the time to do more research but DoS actually did it before me and got the flag. 

It seems to match what I got so far. So bingo! Flag is:

${43y!_743_6r|nc4_57013_my_p|c5!!!!}

Little did I know that the image was already pre-puzzled inside of the damn Photos folder. So I could just use that apparently.

# Curious

I'm still curious on how much else there is here, what is all those files? What do they do? DoS had writtem them all to a PNG file of 3 MB but it seems corrupt. So the order might be wrong?

And the rudolph images, are there something there?
