# rotate64 (🪙 896)

Decrypt the file. Then spin it.

📎 [rotate64.txt](rotate64.txt)

# Writeup

In the filename they hint to rotate and base64, opening the file it seems like a base64 string. Decoding it shows a flagish string.

```bash
$ echo Y3N1ZE1EUHtJMEVfQ1oxWF9XM19CMVFSRF9CMEVYTn0= | base64 -d
csudMDP{I0E_CZ1X_W3_B1QRD_B0EXN}
```

Took it into [Cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)ROT13(true,true,false,16)&input=WTNOMVpFMUVVSHRKTUVWZlExb3hXRjlYTTE5Q01WRlNSRjlDTUVWWVRuMD0) and started spinning until I got something useful. At rot16 I got something.

# Flag

```
siktCTF{Y0U_SP1N_M3_R1GHT_R0UND}
```