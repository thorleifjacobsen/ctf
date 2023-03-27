# årsrapport_2021 (454)

En årvåken påskekylling har mottatt en epost fra en ukjent avsender med "Årsrapport 2021 Norsk Helsenett" som vedlegg.

Kyllingen synes dette virket veldig mistenkelig, og ønsker at en kyllinganalytiker gjør en vurdering på om det er trygt å åpne vedlegget eller om noen har modifisert vedlegget på noen som helst måte.

Originalfilen kan man finne på Norsk Helsenett sine nettsider.

[Arsrapport_2021_Norsk_Helsenett.pdf](Arsrapport_2021_Norsk_Helsenett.pdf)

# Writeup

Downloaded the file and ran `strings` and there I found it 

```
$ strings Arsrapport_2021_Norsk_Helsenett.pdf | grep helse 
helsectf{heldigvis_var_ikke_dette_ondsinnet_kode}
```

# Flag

```
helsectf{heldigvis_var_ikke_dette_ondsinnet_kode}
```