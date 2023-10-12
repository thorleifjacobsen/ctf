# meta (🪙 718)

I downloaded this picture from the internet, I wonder who made it?

📎 [meta.png](meta.png)

# Writeup

Title says it most. I quickly downloaded, checked exiftool and saw this under Author:

```
Author                          : c2lrdENURntEQUxMLUVfTUFEM19USDFTfQ==
```

Base64 decoded it and got the flag:

```bash
$ echo "c2lrdENURntEQUxMLUVfTUFEM19USDFTfQ==" | base64 -d
siktCTF{DALL-E_MAD3_TH1S}
```