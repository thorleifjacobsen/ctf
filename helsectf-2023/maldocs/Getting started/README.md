# Getting started (477)

Maldocs bruker som regel exploits eller makroer for å kjøre kode. Dette maldocet bruker en makro.

Et verktøy for å analysere dokument med makroer er olevba. Et verktøy i oletools. Det finnes andre verktøy, herunder oledump, og man kan se på makroer direkte via word eller med å unzippe filene. Vi anbefaler oletools for makroanalyse.

Zipfilen kan åpnes med passord: "helsectf"

[Getting_started.zip](Getting_started.zip)

# Writeup

Found flag quickly using `strings`

```
$ strings Getting_started.doc | grep helsectf{
helsectf{anbefaler_aa_hente_flagget_med_oletools}
```

But I'll use OleTools to analyze the script, `olevba` 

```
$ olevba Getting_started.doc
XLMMacroDeobfuscator: pywin32 is not installed (only is required if you want to use MS Excel)
olevba 0.60.1 on Python 3.10.8 - http://decalage.info/python/oletools
===============================================================================
FILE: Getting_started.doc
Type: OLE
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls 
in file: Getting_started.doc - OLE stream: 'Macros/VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
(empty macro)
-------------------------------------------------------------------------------
VBA MACRO Module1.bas 
in file: Getting_started.doc - OLE stream: 'Macros/VBA/Module1'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    Private Sub Document_Open()
    flagg = "helsectf{anbefaler_aa_hente_flagget_med_oletools}"

    End Sub

+----------+--------------------+---------------------------------------------+
|Type      |Keyword             |Description                                  |
+----------+--------------------+---------------------------------------------+
|AutoExec  |Document_Open       |Runs when the Word or Publisher document is  |
|          |                    |opened                                       |
+----------+--------------------+---------------------------------------------+
```

This shows that it wil run a script on open, but luckily it is not malicious. 

# Flag

```
helsectf{anbefaler_aa_hente_flagget_med_oletools}
```