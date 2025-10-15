# Minesweeper_beginner

Husker du gode gamle minesweeper? Her er det totalt fire flagg å hente. Her kan du levere flagget for beginner.

Flagget her kan enkelt hentes med å vinne beginner. Bare dobbeltklikk batfilen (i windows...) for å spille. Evt kan du reverse...

[⬇️ minesweeper.bat](./minesweeper.bat)

# Writeup

I just hate these obfuscation tasks, but let's see what we can do.

Guessing the flag is in here `` so just pasting that into a cmd window, then finding anything that uses `��Ax`

`CALL SET "output=%��Ax:~16,1%%��Ax:~63,1%%��Ax:~37,1%%��Ax:~21,1%%��Ax:~63,1%%��Ax:~20,1%%��Ax:~52,1%%��Ax:~40,1%%��Ax:~2,1%%��Ax:~16,1%%��Ax:~46,1%%��Ax:~8,1%%��Ax:~52,1%%��Ax:~37,1%%��Ax:~31,1%%��Ax:~20,1%%��Ax:~55,1%%��Ax:~63,1%%��Ax:~8,1%%��Ax:~56,1%!lf!"`

This sets `output` so running `echo %output%` gives us the flag `helsectf{hurtlocker}` This was the answer for `Minesweeper_intermediate` as it was under the `:2` jump instruction.

Now I went back to `:1`

```batch
:1
set filling=69 79 68 95 116 101 99 104
set cake=104 101 108 115 101 99 116 102 123 !filling! 125
set content=
for %%i in (!cake!) do ( cmd /c exit %%i; Set "char=!=ExitCodeAscii!"; set content=!content!!char! )
echo !content:-= - !
```

Guessing the filling is the flag, tthe cake is `helsectf{<filling>}` looks like DEC representation, [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Decimal('Space',false)&input=MTA0IDEwMSAxMDggMTE1IDEwMSA5OSAxMTYgMTAyIDEyMyA2OSA3OSA2OCA5NSAxMTYgMTAxIDk5IDEwNCAxMjU&oenc=65001) fixed it quickly to be `helsectf{EOD_tech}`.

Now for the thirds finding :3

```batch
:3
set "erewego="
set list=(15,62,36,20,62,19,51,39,1)

set erewego=!erewego!!w:~11,8!
set /a test=1+1
CALL set "output=%%��Ax:~!test!,1%%%"
set erewego=!erewego!!output!!w:~45,4!
set /a genrjkn=!height:~1,1!+!height:~0,1!
call set "op=%%��Ax:~!genrjkn!,1%%%"
set erewego=!erewego!!op!
set /a ewfgfd=!mines!-92+!mines!
cmd /c exit %ewfgfd%
Set "op=!=ExitCodeAscii!"
set erewego=!erewego!!op!
for /f "delims=" %%A in ('certutil -hashfile %0 MD5 ^| find /v ":"') do set "op=%%A"
set /a genr=%op:~10,1%+114
call set "op=%%��Ax:~!genr!,1%%%"
set erewego=!erewego!%op:~10,1%
set /a genrjkn=!width!-14
call set "op1=%%��Ax:~!genrjkn!,1%%%"

set /a genrjkn=!win_con!*29-31-!win_con!*30+42
call set "op2=%%��Ax:~!genrjkn!,1%%%"
cmd /c exit 137
Set "pop=!=ExitCodeAscii!"
set erewego=!erewego!!op1!!op2!r!mode!r!pop!!op!+%��Ax:~56,1%!lf!
echo !erewego!
```

Stepping through adding missing stuff e.t.c. while we go I end up with this:

```batch
set "flag2=z2{yOLwnrS73EqRPh QxcsjZHV90pdMogFmvTlACfXYIJ4u@5KBbtaik}WGU1NDe68"
set mode=3
set width=30
set height=16
set area=30*16
set mines=99
:: win_con = area - mines = 381
set win_con=381
set list=(15,62,36,20,62,19,51,39,1)
set "erewego=helsectf{"
set erewego=%erewego%%output%%w:~45,4%
set /a genrjkn=%height:~1,1%+%height:~0,1%
call set "op=%%flag2:~%genrjkn%,1%%%"
set erewego=%erewego%%op%
set /a ewfgfd=%mines%-92+%mines%
cmd /c exit %ewfgfd%
Set "op=%=ExitCodeAscii%"
set erewego=%erewego%%op%
:: for /f "delims=" %A in ('certutil -hashfile minesweeper.bat MD5 ^| find /v ":"') do set "op=%%A"
: The above just stes "op" = md5 sum of minesweeper.bat
set op=57557c553095405fbea8b53ed4c2152f
set /a genr=%op:~10,1%+114
call set "op=%flag2:~%genr%,1%"
set erewego=%erewego%%op:~10,1%
set /a genrjkn=%width%-14
call set "op1=%flag2:~%genrjkn%,1%"

set /a genrjkn=%win_con%*29-31-%win_con%*30+42
call set "op2=%flag2:~%genrjkn%,1%"
cmd /c exit 137
Set "pop=%=ExitCodeAscii%"
set erewego=%erewego%%op1%%op2%r%mode%r%pop%%op%+%flag2:~56,1%%lf%
echo %erewego%
```



# Flag

```
helsectf{hurtlocker}
```