# ditto (🪙 453)

My friend sent me this textfile, but I do not understand what it says.
Can you help me?

📎 [ditto.txt](ditto.txt)

# Writeup

Textfile is binary, ran the file to reval the real filetype:

```bash
$ file ditto.txt 
ditto.txt: JPEG image data, JFIF standard 1.01, resolution (DPI), density 300x300, segment length 16, Exif Standard: [TIFF image data, little-endian, direntries=7, orientation=upper-left, xresolution=98, yresolution=106, resolutionunit=2, software=GIMP 2.10.30, datetime=2023:08:01 12:33:42], progressive, precision 8, 1280x720, components 3
```

Changing extensions to jpg shows this image:

![ditto.jpg](ditto.jpg)

# Flag

```
siktCTF{TH1S_1S_A_JPG_F1L3}
```