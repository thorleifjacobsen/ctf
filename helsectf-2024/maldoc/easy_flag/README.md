# easy_flag

Du har fått i oppgave å analysere et Excel-ark for å se om det kan inneholde en skjult melding.

I god stil er oppgavefilen pakket i en kryptert zip. (passord infected)

[⬇️ easy_flag.zip](easy_flag.zip)

# Writeup

Unpacked the zip and got a file called `easy_flag.xlsm`. Ran `olevba` on it and got the flag.

```vb
olevba 0.60.1 on Python 3.10.12 - http://decalage.info/python/oletools
===============================================================================
FILE: easy_flag.xlsm
Type: OpenXML
WARNING  For now, VBA stomping cannot be detected for files in memory
-------------------------------------------------------------------------------
VBA MACRO ThisWorkbook.cls
in file: xl/vbaProject.bin - OLE stream: 'VBA/ThisWorkbook'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Private Sub Workbook_Open()
    flag = "helsectf{maldoc=malicious_document}"
End Sub
-------------------------------------------------------------------------------
VBA MACRO Sheet1.cls
in file: xl/vbaProject.bin - OLE stream: 'VBA/Sheet1'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(empty macro)
+----------+--------------------+---------------------------------------------+
|Type      |Keyword             |Description                                  |
+----------+--------------------+---------------------------------------------+
|AutoExec  |Workbook_Open       |Runs when the Excel Workbook is opened       |
|Suspicious|Hex Strings         |Hex-encoded strings were detected, may be    |
|          |                    |used to obfuscate strings (option --decode to|
|          |                    |see all)                                     |
+----------+--------------------+---------------------------------------------+
```

# Flag

```
helsectf{maldoc=malicious_document}
```
