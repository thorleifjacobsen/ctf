# event sourcing (500)

Det viser seg at motparten har gjort en del endringer i sin etterretningsinformasjonen. Heldigvis har vi fått tilgang til endringsloggen slik at vi kan gjenskape tilstanden til riktig tid. Riktig informasjon befinner seg et sted rundt epoch "1679485045".

```
bootstrap_servers: ec2-13-49-134-84.eu-north-1.compute.amazonaws.com:9092
security_protocol: SASL_PLAINTEXT  
auto_offset_reset: earliest
username: user2
password: helsectf2023ersuperduper
```

# Writeup

Been tearing my head hairless nearly (in my mind).. There was a bug in this one where there was no messages to the topic. Fixed now so finally I can see it. I've cleaned up the messages to the things I think is meaningful.

```python
timestamp=1679483480000 key=b'\x03', value={'feed': 'helsectf', 'source': 'https://helsectf2023-6ac4e1c6d8855c1bd96a.ctfd.io/', 'action': 'create', 'intel': [{'type': 'flag', 'value': 's'}]}
timestamp=1679483480000 key=b'\x19', value={'feed': 'helsectf', 'source': 'https://helsectf2023-6ac4e1c6d8855c1bd96a.ctfd.io/', 'action': 'create', 'intel': [{'type': 'flag', 'value': '?'}]}
timestamp=1679483480000 key=b'\x1a', value={'feed': 'helsectf', 'source': 'https://helsectf2023-6ac4e1c6d8855c1bd96a.ctfd.io/', 'action': 'create', 'intel': [{'type': 'flag', 'value': '?'}]}
timestamp=1679483497000 key=b'\x1f', value={'feed': 'helsectf', 'source': 'https://helsectf2023-6ac4e1c6d8855c1bd96a.ctfd.io/', 'action': 'update', 'intel': [{'type': 'flag', 'value': 'y'}]}
timestamp=1679483666000 key=b'\x18', value={'feed': 'helsectf', 'source': 'https://helsectf2023-6ac4e1c6d8855c1bd96a.ctfd.io/', 'action': 'update', 'intel': [{'type': 'flag', 'value': '='}]}
timestamp=1679483670000 key=b'\x18', value={'feed': 'helsectf', 'source': 'https://helsectf2023-6ac4e1c6d8855c1bd96a.ctfd.io/', 'action': 'update', 'intel': [{'type': 'flag', 'value': 'a'}]}
timestamp=1679483738000 key=b'\x19', value={'feed': 'helsectf', 'source': 'https://helsectf2023-6ac4e1c6d8855c1bd96a.ctfd.io/', 'action': 'update', 'intel': [{'type': 'flag', 'value': 'k'}]}
timestamp=1679483751000 key=b'\x19', value={'feed': 'helsectf', 'source': 'https://helsectf2023-6ac4e1c6d8855c1bd96a.ctfd.io/', 'action': 'update', 'intel': [{'type': 'flag', 'value': 'l'}]}
timestamp=1679483814000 key=b'.',    value={'feed': 'helsectf', 'source': 'https://helsectf2023-6ac4e1c6d8855c1bd96a.ctfd.io/', 'action': 'update', 'intel': [{'type': 'flag', 'value': 'g'}]}
timestamp=1679483889000 key=b'\x1b', value={'feed': 'helsectf', 'source': 'https://helsectf2023-6ac4e1c6d8855c1bd96a.ctfd.io/', 'action': 'update', 'intel': [{'type': 'flag', 'value': 'k'}]}
timestamp=1679483907000 key=b'\t',   value={'feed': 'helsectf', 'source': 'https://helsectf2023-6ac4e1c6d8855c1bd96a.ctfd.io/', 'action': 'update', 'intel': [{'type': 'flag', 'value': 'N'}]}
```

Looks like there is 3 create actions with a whole lots of update actions. It has a json object. I quickly tried to use `key` as a order and value as the letter like I did no the [event join](../event%20join/) challenge. This gave no sense for me. 

```
esefs58s\ssns*sNEt"ptb~tat.tJt+t$H|r?JUr\rrrr1rreIwRe{eeeeaea<auaavaa/aLa"m1RymmmhmmR~_|?_U__-otttWttt/tttpPt?OD6i?paa&aau?0|bZb,bbb?llJlZJlK_jAlellla6Je"eeee{*eee|etj,_<_P'?_?dddI6tdru*yuuuqa`a2a#?MaaaZ=a,,lllll>|\l?klD%l]ie?t0ttt?vbst#`kUX1y:<yyyFy>?@r$T=78eFbbbbbU]mkFS#by0yI/.y2rynoy]y'yyf":d}___:_?T%4]_qe=eoomSet#e^QAvvvTvvvovTqv()ge./,ue<?v+yeeecen[u|=TTonn+n*?n:"V?3ttqtH_{_%*__!_+_&uvW[[s4s/sB4sssssDoKsoo?-.^>u?u;iu$uSunu`usu/uu_rr,rr~rrp+yc/?cbc&cW@ij?KeniI0ii~nbna%y?,nnH`mg+gWMge(Px?lgG}
```

I totally forgot the epoch time given in the challenge. This homes it down. So the correct data is around: 1679485045. What I did was to loop through all messages, put them in a nice array or arrays `[timestamp, order, value]` then sort that array by the timestamp. 

```python
[
    [1679488142000, 42, 'r']
    [1679488148000, 19, 'l']
    [1679488153000, 44, 'j']
    [1679488162000, 16, 'J']
    [1679488168000, 29, '7']
    [1679488172000, 18, '&']
    [1679488175000, 42, 'p']
    [1679488182000, 35, ',']
    [1679488192000, 29, '_']
    [1679488201000, 27, '<']
    ...n
]
```

Now I could loop through the array, ignoring all except the values within a given period and add the letter at correct order:

```python
string = [""] * 50

for idx, x in enumerate(data):
    if 1679480045000 <= x[0] <= 1679485045000:
        string[x[1]] = x[2]

print("".join(string))
```

After a bit of trial and failure I found the perfect time to give the correct flag. I just adjusted the numbers +- some until it hits.

# Flag

```
helsectf{stream_table_duality_by_event_sourcing}
```