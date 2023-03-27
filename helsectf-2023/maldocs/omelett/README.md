# omelett (499)

Maldocs bruker som regel exploits eller makroer for å kjøre kode. Dette maldocet bruker en makro.

Kanskje makroen inneholder et flagg også...?

Zipfilen kan åpnes med passord: "helsectf"

[Du_kan_ikke_lage_omelett_uten_a_knuse_noen_egg.zip](Du_kan_ikke_lage_omelett_uten_a_knuse_noen_egg.zip)

# Writeup

```
$ olevba Du\ kan\ ikke\ lage\ omelett\ uten\ å\ knuse\ noen\ egg.docm 
-------------------------------------------------------------------------------
VBA MACRO NewMacros.bas 
in file: word/vbaProject.bin - OLE stream: 'VBA/NewMacros'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Function DecodeBase64(b64$)
    Dim b
    With CreateObject("Microsoft.XMLDOM").createElement("b64")
        .DataType = "bin.base64": .Text = b64
        b = .nodeTypedValue
        With CreateObject("ADODB.Stream")
            .Open: .Type = 1: .Write b: .Position = 0: .Type = 2: .Charset = "utf-8"
            DecodeBase64 = .ReadText
            .Close
        End With
    End With
End Function

Sub eggjakt()
Debug.Print DecodeBase64(eggeskall) + vbCrLf + eggehvite; vbCrLf; DecodeBase64(eggeskall)

End Sub
Function eggeskall()
Dim skall As String
*removed unessesary data*

red_herring = "helsectf{ ... }"

eggeskall = skall

End Function
Function eggehvite()
Dim Eggejakt As Boolean

If Eggejakt Then
    eggehvite = "                  _ /"
    eggehvite = eggehvite + Eggeplomme(1)
    eggehvite = eggehvite + "\ "
    eggehvite = eggehvite + vbCrLf + "|_  _ | _ _  _ |_(_( "
    eggehvite = eggehvite + Eggeplomme(2)
    eggehvite = eggehvite + "  )" + vbCrLf
    eggehvite = eggehvite + "| )(-`|_)(-`(_ |_|  \"
    eggehvite = eggehvite + Eggeplomme(3) + "/ "
Else
    eggehvite = "                  _ /"
    eggehvite = eggehvite + "                                                           " + "\ "
    eggehvite = eggehvite + vbCrLf + "|_  _ | _ _  _ |_(_( "
    eggehvite = eggehvite + "                                                          " + "  )" + vbCrLf
    eggehvite = eggehvite + "| )(-`|_)(-`(_ |_|  \"
    eggehvite = eggehvite + "                                                           " + "/ "
End If

End Function
Function Eggeplomme(i As Integer)

Select Case i
    Case 3
        Eggeplomme = "|  |/--\|__|__/\__/\__\__/|   |    \/ /--\| \ |  ||| \|\__)"
    Case 1
        Eggeplomme = "            __  __  __ __  __  __          __           __ "
    Case 2
        Eggeplomme = "|\/| /\ |  |  \/  \/  /  \|__)|__)\  / /\ |__)|\/|||\ |/ _ "

End Select

End Function

Sub AutoOpen()
eggjakt
MsgBox ("Nothing to see here" + vbCrLf + "https://www.youtube.com/watch?v=NuAKnbIr6TE")
End Sub
```

Moving the `eggeplomme` correctly shows:

```
Eggeplomme = "            __  __  __ __  __  __          __           __ "
Eggeplomme = "|\/| /\ |  |  \/  \/  /  \|__)|__)\  / /\ |__)|\/|||\ |/ _ "
Eggeplomme = "|  |/--\|__|__/\__/\__\__/|   |    \/ /--\| \ |  ||| \|\__)"
```

Moving this over to a python script to print correctly gives me this:

```
                  _ /            __  __  __ __  __  __          __           __ \ 
|_  _ | _ _  _ |_(_( |\/| /\ |  |  \/  \/  /  \|__)|__)\  / /\ |__)|\/|||\ |/ _   )
| )(-`|_)(-`(_ |_|  \|  |/--\|__|__/\__/\__\__/|   |    \/ /--\| \ |  ||| \|\__)/ 
```

Clearly I see `helsectf{MALDOCOPPVARMING}`

# Flag

```
helsectf{MALDOCOPPVARMING}
```