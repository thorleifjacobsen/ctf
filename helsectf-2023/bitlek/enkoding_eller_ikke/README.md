# enkoding_eller_ikke (493)

Jeg har hørt at XOR (^) er sin egen invers (A ^ A = 0)da burde det vel gå greit å dekryptere denne?

[source.py](source.py) [output.txt](output.txt)

# Writeup

Here I managed to write a prorgam which started outputting correct data:

```python
ct = 30102120926570861509131351147532197169703687627473236038968351950588475608640746216
while ct > 0:
    print(chr((ct & 0b11111111) ^ 128), end="")
    ct = ct >> 7

# Output: hemsecug{OS_es_eo_eesusukuiw_oqesaskoo}
```

The way they bitshift only 7 bits one bit is overwritten randomly so some of the characters are pushed one character forward.

I dont believe there is a way to fix this, but some manual work fixes everything:

```python
hemsecug{OS_es_eo_eesusukuiw_oqesaskoo} # Rot 0
^^v^^^vv|^v|^v|^v|v^^vv^^v^v|^v^v^^v^v|
gdlrdbtf{NR_dr_dn_ddrtrtjthv_npdrzrjnn} # Rot -1
```

So I basically just knew the first part, and then I just tried to create something that made sence. E.g. `OS` does not make sense, neither does `NS` the last alternative is `OR` which makes sense. Then I did that word for word until I found something that made sense. Text basically says `OR is a destructive operation`. Using `^` for the upper characters, `v` for the lower and `|` for neither works. 

# Flag

```
helsectf{OR_er_en_destruktiv_operasjon}
```