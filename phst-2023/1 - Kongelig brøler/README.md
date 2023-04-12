# Kongelig brøler

Hei Toffe,

godt å se at du finner deg til rette. Her er det første du må løse for oss. Du vil få flere oppdrag til og med søndag 9.4.

Pen GWYN gjorde en skikkelig brøler og ble tatt i forbifarten ved sikkerhetskontrollen på flyplassen. Under armen hadde han et sammenleggbart sjakkbrett med et dokument inni. Dokumentet ser ut til å være kryptert.

Undersøk filen og rapporter funn.

Mellomleder

[📎 FEN.txt](FEN.txt)

# Writeup

Googled "FEN chess" saw that was a thing to decode positions of the pieces. Googled for a viewer which landed me [here](http://www.ee.unb.ca/cgi-bin/tervo/fen.pl).

Decoded all one by one, knewing it started with `PST{`. Every time I found one that was equal to another I marked up all them to not decode same letter multiple times.

The 3 last one seems to be a full board of black and white, this might be an egg. 

[1](1.png) = `bwbbbwbw bwbbbwww bwbbbwww bwwwwbww bwbbwbww bwwwbwbw bwwbwwbb bwwbbwbw`

[2](2.png) = `bwbwwwww bwwwbbww bwwbwbwb bwwbbbbw bwwbwbww bwwbwbww bwwwbwwb bwwbbbbw`

[3](3.png) = `bwwwbbwb bwwbwbbw bwwbbbbw bwwbwwwb bwwwbwbb bwwbbwbw bwwwbbwb bwwwwwbw`


Running this trough [cyberchef](https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Regex','string':'b'%7D,'0',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'w'%7D,'1',true,false,true,false)From_Binary('Space',8)&input=YndiYmJ3YncgYndiYmJ3d3cgYndiYmJ3d3cgYnd3d3did3cgYndiYndid3cgYnd3d2J3YncgYnd3Ynd3YmIgYnd3YmJ3YncKYndid3d3d3cgYnd3d2Jid3cgYnd3Yndid2IgYnd3YmJiYncgYnd3Yndid3cgYnd3Yndid3cgYnd3d2J3d2IgYnd3YmJiYncKYnd3d2Jid2IgYnd3YndiYncgYnd3YmJiYncgYnd3Ynd3d2IgYnd3d2J3YmIgYnd3YmJ3YncgYnd3d2Jid2IgYnd3d3d3Ync) I get an EGG.

# Flag

```
PST{NOEN_UVANLIGE_STILLINGER}
```

# Egg 

```
EGG{Kule_sjakkvarianter}
``` 