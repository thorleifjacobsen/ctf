# WEB //   🪄 Kind of Magic
 
Why generate thumbnails locally, when there's a web service to do it remotely?

[⬇️ kind-of-magic.zip](./kind-of-magic.zip)

# Writeup

According to the dockerfile they use imagemagick which seems to be a vulnerable one:

```
curl https://archive.archlinux.org/packages/i/imagemagick/imagemagick-7.1.0.49-1-x86_64.pkg.tar.zst > imagemagick-7.1.0.49.tar.zst
```

Here is a [POC](https://github.com/agathanon/cve-2022-44268) for the exploit cve-2022-44268 which is a local file inclusion in imagemagick with this version. It exploits a vulnerability where you can set a file to be read which will be populated in the `Raw Profile Type`. 

The dockerfile shows flag is stored in `/flag` so we can just try to use this image og Mike the Hacker to get the flag. Using [craft.py](./craft.py) we can craft a payload to get the flag:

```bash
$ python3 craft.py mike.png exploit.png /flag
```

Then we upload `exploit.png` and download the result, we can use `extract.py` to extract the flag:

```bash
└─$ python3 extract.py exploit_resized.png 
1753c{there_is_magic_in_the_air_its_called_CVE_2022_44268}
```