# Pass or fail?

.bat - filer kan gjøre ganske mye. Denne bat-filen vil ikke kjøre noe skummelt om du kjører den. Finn ut hva den gjør. Evt hva du kan mate den med (input) for å få ønsket resultat.

Flagget gjemmer seg i en pass, ikke en fail.

Passord for zip-fil er standard (infected).

[⬇️ pass_or_fail.zip](pass_or_fail.zip)

# Writeup

I started of with this on a very tedious way. So for a quicker solution see the second writeup below.

The first line is a hint on how to solve this.

```batch
@%public:~5,1%%public:~14,1%ho off
```

We all know thhey want to hide all their commands so `echo off` will disable output of each command executed to the console. The hint here is that they produce `E` and `C` by some weird string manupulation. The `~5,1` means that we want to start at index 5 and take 1 character. So `echo %public:~5,1%` will output `e`. The same goes for `c`. So the first line is just a fancy way of writing `echo off`.

In batch `%public%` is a variable which points to the public folder. So `%public:~14,1%` will output `c` as the 14th character in the path is `c`.

```batch
C:\>echo %public%
C:\Users\Public
```

And skip 5 characters and take 1 `C:\Users\Public` gives an `e`. And skip 14 characters and take 1 `C:\Users\Public` gives a `c`.

Now that this is out of the way we can decode the file. I've made a script to do this because I'm lazy. (little did I know of the lazier method I found later on)

I ran [solve.js](solve.js) and got this output:

```powershell
@echo off
set "饿饿尔艾=wrUnsT7NBeCfiljYRb5cPF2oQ8SWZzG@VJpvXxO6K3HI LadgAqDmu14h=MEkty09"
@set "斯尔色斯=Kt@4oE2uzLIZ80qiR1YpOldD SjNe7bWskfvUMCwVBnrGgFHamPJhxXAyQ536c9=T"
@set "饿阿豆豆=ybVIQN=SoEOikuHCcfa2 LhB3KUA6rzXxY0Dw7nJg4sM9tjG85d1ZqePlWRv@FTpm"
@set "尔色爱德=NaY35kTOpHZ@2E0hI=yrxjm SUbKF6eiCW7R9fslt8wJuzdoDLA1Gv4nQgMXVPcBq"
@set "斯尔贝贝=RzxkNpCdKhS3@2efquTcowElvU8W9rLHVa 6AZDG7Q0Yy5JijnFO4MPbgXmBtI1s="
for /l %%y in (1,1,1) do @echo off
if 1 EQU 1 set "abc2=https://youtu.be/YZf0Q-v3u-k?feature=6e6569746865722069732074686973"
for /l %%y in (1,1,1) do set "abc3=https://youtu.be/3xYXUeSmb-Y?feature=54686973206973206e6f742074686520666c6167"
if 46 EQU 0 (@exit) else set "abc4=G@nd@lf"
if 1 EQU 1 set "abc1=https://youtu.be/qybUFnY7Y8w?feature="
if 1 LsS 109 set "abc7=explorer.exe"
if 1 EQU 1 if not "%~1" equ "" goto usage
for /l %%y in (1,1,1) do goto end
:usag^e  lli^iliii%ヾ(⌐■_■)ノヾ(⌐■_■)ノヾ(⌐■_■)ノヾ(⌐■_■)ノヾ(⌐■_■)^ノヾ(⌐■_■)ノ%%┌( ಠ_ಠ)┘┌( ಠ_ಠ)┘(⊙ω⊙)^ヾ(⌐■_■)ノ┌( ಠ_ಠ)┘(⊙ω⊙)%l%(⊙ω⊙)(◕‿◕)ヾ(⌐■_■)ノ(⊙ω⊙)(⊙ω⊙)┌( ಠ^_ಠ)┘%il   l^%سﮱ◯ﺹﺼ^ك%%﷽ت^ﮕﺖﯔﮚ%l%تﮱﭫ^ﺼﺹ◯%ililllili
if 1 LsS 109 set "abc5=68656c73656374667b746869"
if 1 LsS 109 if %1==G@nd@lf (set "abc6=735f325f7368616c6c5f706173737d"
if 1 LsS 109 set "abc7=https://youtu.be/qybUFnY7Y8w?feature=68656c73656374667b746869735f325f7368616c6c5f706173737d"
) else (start https://youtu.be/YZf0Q-v3u-k?feature=6e6569746865722069732074686973)
if 1 LsS 109 start https://youtu.be/qybUFnY7Y8w?feature=68656c73656374667b746869735f325f7368616c6c5f706173737d
if 1 LsS 109 exit
:en^d  lilll^il%此護秘無^神製%%息被護貼製複^%%息秘是無^貼已%lill   lii%┌( ಠ_ಠ)┘(⊙ω⊙)┌( ಠ_ಠ)┘(◕‿◕)┌( ಠ_ಠ)┘┌( ಠ_ಠ^)┘%ll%┌( ಠ_ಠ)┘ヾ^(⌐■_■)ノヾ(⌐■_■)ノ(◕‿◕)(◕‿◕)(⊙ω⊙)%lll%┌( ಠ_ಠ)┘(⊙ω⊙)ヾ(⌐■_■)ノ(◕‿◕)(◕‿◕)^(⊙ω⊙)%l^il
for /l %%y in (1,1,1) do start https://youtu.be/3xYXUeSmb-Y?feature=54686973206973206e6f742074686520666c6167
```

I saw a few hex strings and tried them all in cyberchef (`From Hex`). On this URL the last bit is the flag.

```
https://youtu.be/qybUFnY7Y8w?feature=68656c73656374667b746869735f325f7368616c6c5f706173737d
```

Decoding this gives us the flag.

# Writeup 2

Instead of doing any code you can take one and one line and paste with an "echo" in front in a cmd window. This will give you the output of each line. Then if the line is creating a variable by using `set` you run that as well then continue down. I'm clearing the screen once it is filled so I can see the output of each line.

![image](Animation.gif)

# Flag

```
helsectf{this_2_shall_pass}
```