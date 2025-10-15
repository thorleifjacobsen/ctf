    @echo off
    setlocal enabledelayedexpansion
    for /f "delims=" %%g in ('forfiles /p "%~dp0." /m "%~nx0" /c "cmd /c echo(0x1B"') do set "esc=%%g"
    echo %esc%[?25l
    (set lf=^
    %=%
    )
    set game[1]="height=9,width=9,mines=10"
    set game[2]="height=16,width=16,mines=40"
    set game[3]="height=16,width=30,mines=99"
    set "��Ax=z2{yOLwnrS73EqRPh QxcsjZHV90pdMogFmvTlACfXYIJ4u@5KBbtaik}WGU1NDe68"
    set "ch=1`4 2`1 3`1 2`5 3`1 4`5 1`5 1`4 0`1 6`1 3`1 2`1 6`1 1`1 5`1 3`1 5`1 3`1 0`1 6`5 2`4 3`3 5`1 3`4 2`4 1`0 0`1 6`1 3`1 2`1 5`1 3`1 4`1 3`1 5`1 1`1 2`0 0`0 1`4 2`1 3`1 2`5 1`1 3`1 4`1 3`5 1`1 2`1"
    set readyornot="no"
    set "zero=0"
    set "move[1]=x l zero height -1"
    set "move[2]=y l zero width -1"
    set "move[3]=x g height zero 1"
    set "move[4]=y g width zero 1"
    set "count=0"
    set /a flags=0
    for %%g in (30 94 92 91 34 31 96 97 37) do (
        set "c[!count!]=%esc%[%%gm!count!%esc%[0m"
        set /a "count+=1"
    )
    set "c[-]=%esc%[7;31mX%esc%[0m"
    :a
    cls
    :aa
    set /a gg=50
    set w=Welcome to helsectf!lf!How about a nice game of minesweeper?!lf!!lf!1^) Beginner!lf!2^) Intermediate!lf!3^) Expert!lf!4^) Exit
    echo !w!
    for /f "delims=" %%A in ('certutil -hashfile %0 MD5 ^| find /v ":"') do set "hashValue=%%A"
    choice /c 1234c /n >nul
    if !errorlevel! equ 4 exit
    if !errorlevel! equ 5 goto :c
    rem 101
    goto :p
    :p
    set /a "!game[%errorlevel%]!"
    set mode=!errorlevel!
    :pp
    set /a "area=(width*height)-1"
    set /a "x=0,y=0,z=1"
    set "string0=#" 
    set "string1=#"
    set /a a = (!height!%!width!)/!mines!
    set /a cnt=5
    if !a! geq 9 if !a! leq 11 if !mines! neq 10 if horns neq 1 goto :startgame
    if !a! leq 17 if !mines! neq 99 if !a! gtr 15 if horns neq 1 goto :startgame
    if !mines! neq 40 if !a! gtr 38 if !a! leq 50 if horns neq 1 goto :startgame

    set "row=^^^!b^!h^!`!width!^^^!"
    set /a "height-=1"
    for /l %%g in (0,1,!height!) do (
        for /l %%h in (0,1,!width!) do set "b%%g`%%h= "
    )
    set /a "width-=1"
    for /l %%g in (0,1,!height!) do (
        for /l %%h in (0,1,!width!) do (
            set "a[%%g`%%h]=0"
            set "d%%g`%%h=%esc%[90m?%esc%[0m"
            set "string0=!string0!%%g`%%h#"
        )
    )
    set /a "mines-=1"
    for /l %%g in (!width!,-1,0) do set "row=^^^!b^!h^!`%%g^^^!^^^!d^!h^!`%%g^^^!!row!"
    cls
    :b
    call :board
    choice /c wasdq /n >nul
    if "!errorlevel!" neq "5" (
        call :move !move[%errorlevel%]!
        goto b
    )
    set /a "win_con=area-mines"
    for %%g in (0 1 2) do set "digit%%g=!area:~%%g,1!"
    for %%g in (-1 0 1) do (
        for %%h in (-1 0 1) do (
            set /a "m=x+%%g,n=y+%%h"
            if !m! geq 0 (
                if !m! leq !height! (
                    if !n! geq 0 (
                        if !n! leq !width! (
                            set /a "area-=1"
                            for %%i in ("!m!`!n!") do set "string0=!string0:#%%~i#=#!"
                        )
                    )
                )
            )
        )
    )
    set /a "digit0-=1"
    for /l %%g in (0,1,!digit0!) do (
        for /l %%h in (0,1,9) do (
            for /l %%i in (0,1,9) do (
                for /f "tokens=1 delims=#" %%j in ("!string0!") do (
                    set "h[%%g%%h%%i]=%%~j"
                    set "string0=!string0:#%%~j#=#!"
                    set "string1=!string1!%%g%%h%%i#"
                )
            )
        )
    )
    set /a "digit0+=1,digit1-=1"
    for /l %%g in (0,1,!digit1!) do (
        for /l %%h in (0,1,9) do (
            for /f "tokens=1 delims=#" %%i in ("!string0!") do (
                set "h[!digit0!%%g%%h]=%%~i"
                set "string0=!string0:#%%~i#=#!"
                set "string1=!string1!!digit0!%%g%%h#"
            )
        )
    )
    set /a "digit1+=1"
    for /l %%g in (0,1,!digit2!) do (
        for /f "tokens=1 delims=#" %%h in ("!string0!") do (
            set "h[!digit0!!digit1!%%g]=%%~h"
            set "string0=!string0:#%%~h#=#!"
            set "string1=!string1!!digit0!!digit1!%%g#"
        )
    )
    set "string0="
    for /l %%g in (0,1,!mines!) do (
        set /a "rand=4*(!random! %% !area!)+1, area-=1"
        for %%h in (!rand!) do (
            for /f %%i in ("!string1:~%%h,3!") do (
                set "a[!h[%%~i]!]=-10"
                set "string1=!string1:#%%~i#=#!"
                set "string0=!string0!!h[%%i]! "
                for /f "tokens=1,2 delims=`" %%j in ("!h[%%i]!") do (
                    for %%l in (-1 0 1) do (
                        for %%m in (-1 0 1) do (
                            set /a "m=%%j+%%l,n=%%k+%%m"
                            if !m! geq 0 (
                                if !m! leq !height! (
                                    if !n! geq 0 (
                                        if !n! leq !width! set /a "a[!m!`!n!]+=1"
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
    if defined horns ( set "string0=1`0 1`1 1`6 1`7 1`10 1`11 1`12 1`16 1`17 1`18 2`0 2`1 2`2 2`5 2`6 2`7 2`9 2`10 2`12 2`13 2`15 2`16 2`18 2`19 3`0 3`1 3`3 3`4 3`6 3`7 3`9 3`10 3`12 3`13 3`15 3`16 3`18 3`19 4`0 4`1 4`6 4`7 4`10 4`11 4`12 4`16 4`17 4`18" 
    )

    for /l %%g in (0,1,!height!) do (
        for /l %%h in (0,1,!width!) do (
            for /f %%i in ("!a[%%g`%%h]:~0,1!") do set "a[%%g`%%h]=!c[%%i]!"
        )
    )

    set "list=#!x!`!y!#"
    set "done=#"
    call :zero_chaining

    :main
    call :board
    echo # of flags set is: %flags%

    choice /c wasdqe /n >nul
    if !errorlevel! leq 4 (
        call :move !move[%errorlevel%]!
    ) else if !errorlevel! equ 5 (
        call :dig
    ) else call :flag
    goto main
    :c
    cls
    echo !w!
    choice /c 1234o /n >nul
    if !errorlevel! equ 4 exit
    if !errorlevel! equ 5 goto :o
    goto :P
    :2
    CALL SET "output=%��Ax:~16,1%%��Ax:~63,1%%��Ax:~37,1%%��Ax:~21,1%%��Ax:~63,1%%��Ax:~20,1%%��Ax:~52,1%%��Ax:~40,1%%��Ax:~2,1%%��Ax:~16,1%%��Ax:~46,1%%��Ax:~8,1%%��Ax:~52,1%%��Ax:~37,1%%��Ax:~31,1%%��Ax:~20,1%%��Ax:~55,1%%��Ax:~63,1%%��Ax:~8,1%%��Ax:~56,1%!lf!"
    echo %output%
    goto :playmoar
    :move
    if !%1! %2eq !%3! (
        set "%1=!%4!"
    ) else set /a "%1+=%5"
    set /a "z=y+1"
    exit /b
    :o
    cls
    echo !w!
    choice /c 1234w /n >nul
    if !errorlevel! equ 4 exit
    if !errorlevel! equ 5 goto :w
    :startgame
    set "ea="
    :parse
    for /f "tokens=1* delims= " %%a in ("!ch!") do (
        for /f "tokens=1,2 delims=`" %%g in ("%%a") do (
            if %%g equ 0 set "ea=!ea!!lf!"
            set t=%%g
            for /l %%i in (1,1,!t!) do (
                set "ea=!ea! "
            )
            set t=%%h
            for /l %%i in (1,1,!t!) do (
                set "ea=!ea!X"
            )
        )
        if %%b neq "" (
            set ch=%%b
            goto :parse
        )
    )
    cls
    echo !ea!
    if !cnt! equ 5 goto :0
    goto :playmoar
    :0
    cls
    echo !ea!
    if not "%cnt%"=="0" choice /C YNT /N /T 1 /D T /M "Program terminating in %esc%[7;31m%cnt%%esc%[0m!lf!Stop cheating (or cheat better)!"
    if "%cnt%"=="0" exit
    exit
    :dig
    goto dag
    set /a win_con=0
    cls
    choice /c 123
    :dag
    for /f %%g in ("!x!`!y!") do (
        if "!d%%~g:~5,1!" equ "?" (
            if "!a[%%~g]:~7,1!" neq "X" (
                if "!a[%%~g]:~5,1!" equ "0" (
                    for /f "delims=" %%A in ('certutil -hashfile %0 MD5 ^| find /v ":"') do set "hashValue=%%A"
                    if %hashValue:~10,1% neq 1 exit
                    set "list=#!x!`!y!#"
                    call :zero_chaining
                ) else (
                    set "d%%~g=!a[%%~g]!"
                    set /a "win_con-=1"

                )
                if !win_con! equ 0 (
                    call :board
                    cls
                    echo You win!lf!
                    goto !mode!
                    choice /c q /n >nul
                    echo !mode!
                    set /a mode=!win_con!+!mode!*!mines!*!area!%!mode!%!mines!
                    echo !mode!
                    choice /c q /n >nul
                    goto a
                ) else (
                    call :board
                    echo # of flags set is: %flags%
                )
            ) else (
                for %%h in (!string0!) do (
                    set "d%%h=!a[%%h]!"
                )
                call :board
                echo You lose                   
                set /a flags=0
                choice /c q /n >nul
                goto a
            )
        )
    )
    exit /b
    :1
    set filling=69 79 68 95 116 101 99 104
    set cake=104 101 108 115 101 99 116 102 123 !filling! 125
    set content=
    for %%i in (!cake!) do (
        cmd /c exit %%i
        Set "char=!=ExitCodeAscii!"
        set content=!content!!char!
    )
    echo !content:-= - !
    goto :playmoar
    :playmoar
    echo Would you like to play some more?
    choice /c YN
    if %errorlevel% equ 2 exit
    cls
    set /a flags=0
    goto a

    :flag
    for /f %%g in ("!x!`!y!") do (
        if "!d%%~g:~5,1!" equ "?" (
            set "d%%g=P"
            set /a "flags+=1"


        ) else if "!d%%g!" equ "P" (
            set "d%%g=%esc%[90m?%esc%[0m"
            set /a "flags-=1"


        )
    )
    exit /b
    :w 
    set horns=1
    set "ch=60`4 99`4 0`0 1`1 4`1 1`6 1`1 7`3 2`6 2`4 2`7 1`6 3`2 4`4 2`6 2`3 2`6 2`6 1`7 2`3 3`4 2`1 5`1 1`1 6`6 1`1 5`1 1`6 1`1 8`2 0`0 1`1 4`1 1`1 6`1 6`1 3`1 1`1 6`1 4`1 4`1 4`1 7`2 4`1 3`2 1`1 6`1 3`1 1`1 5`1 1`1 9`1 4`1 3`1 1`1 4`1 1`1 2`1 2`1 1`1 6`1 6`1 5`1 1`1 6`1 9`2 0`0 1`1 4`1 1`1 6`1 6`1 5`1 6`1 9`1 4`1 7`2 4`1 6`1 6`1 5`1 5`1 1`1 9`1 4`1 5`1 4`1 1`1 2`1 2`1 1`1 6`1 6`1 5`1 1`1 6`1 9`2  0`0 1`6 1`4 3`1 7`3 2`4 3`1 9`1 4`4 3`3 5`4 2`4 3`1 5`6 2`4 6`1 4`1 5`1 4`1 1`1 2`1 2`1 1`1 6`4 3`1 5`1 1`4 3`1 9`3 0`0 1`1 4`1 1`1 6`1 10`1 1`1 6`1 9`1 4`1 7`2 8`2 1`1 6`1 5`1 3`1 3`1 9`1 4`1 5`1 4`1 1`1 2`1 2`1 1`1 6`1 7`1 3`1 2`1 6`1 9`2 0`0 1`1 4`1 1`1 6`1 6`1 3`1 1`1 6`1 4`1 4`1 4`1 7`2 4`1 3`2 1`1 6`1 3`1 1`1 4`1 2`1 9`1 4`1 3`1 1`1 4`1 1`1 2`1 2`1 1`1 6`1 8`1 1`1 3`1 6`1 9`2 0`0 1`1 4`1 1`6 1`6 2`3 2`6 2`4 5`1 4`1 8`2 4`4 2`6 2`3 2`1 5`1 1`6 4`1 5`3 3`4 3`2 1`2 2`6 1`6 4`1 4`6 1`6 3`2 0`0 60`4 99`4 0`0"
    set /a cnt=20
    goto :startgame
    goto :pp


    goto :aa
    :flagger
    if %flags% eq %width%*%height% (
        
    )
    exit /b
    :check2
    set "readyornot=yes"
    cls

    echo Use 'WASD' to move. 
    echo 'Q' to open fields 
    echo 'E' to flag (or unflag) mines!lf!
    echo Controls understood? Y/N?
    echo !comeon!
    set comeon=!comeon!^^!
    choice /c YN 
    cls
    if !errorlevel! equ 2 goto :check2
    exit /b
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
    goto :playmoar
    :zero_chaining
    for /f "tokens=1 delims=#" %%g in ("!list!") do (
        set "list=!list:#%%~g#=#!"
        set "done=!done!%%g#"
        for /f "tokens=1,2 delims=`" %%h in ("%%~g") do (
            for %%j in (-1 0 1) do (
                for %%k in (-1 0 1) do (
                    set /a "m=%%h+%%j,n=%%i+%%k"
                    for %%l in ("!m!`!n!") do (
                        if !m! geq 0 (
                            if !m! leq !height! (
                                if !n! geq 0 (
                                    if !n! leq !width! (
                                        if "!d%%~l:~5,1!" equ "?" (
                                            set "d%%~l=!a[%%~l]!"
                                            set /a "win_con-=1"
                                            if "!a[%%~l]:~5,1!" equ "0" (
                                                if "!list:#%%~l#=#!" equ "!list!" (
                                                    if "!done:#%%~l#=#!" equ "!done!" set "list=!list!%%~l#"
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
    if "!list:#=!" neq "" goto :zero_chaining
    exit /b

    :board
    if !readyornot! equ "no" (
        call :check

        )
    set "b!x!`!y!=["
    set "b!x!`!z!=]"
    set "board="
    for /l %%g in (0,1,!height!) do (

        set "h=%%g"
        set "board=!board!%row%^!lf^!"

    )

    echo %esc%[1;1H%board%
    set "b!x!`!y!= "
    set "b!x!`!z!= "
    exit /b

    :check
    set "readyornot=yes"
    cls
    echo Use 'WASD' to move. 
    echo 'Q' to open fields 
    echo 'E' to flag (or unflag) mines!lf!
    set comeon=Really? Try harder!
    echo Controls understood? Y/N?!lf!
    choice /c YN 
    cls
    if !errorlevel! equ 2 goto :check2
    exit /b
                