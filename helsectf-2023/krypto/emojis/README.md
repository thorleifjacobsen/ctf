# emojis (500)

Peder Påskekylling fant noen rare tegn på maskinen sin:

🦵🦲🦹🧀🦲🦰🧁🦳🧈🦲🦺🥽🦷🥾🧀🦬🦯🦀🦴🧆🦛🦻🦲🦿🦬🦮🦮🦬🦯🦙🦶🦬🦼🦝🦽🦯🦿🦢🦸🧁🦬🦠🥽🦺🦬🦐🦡🦓🦬🦼🦽🦝🦴🦮🧃🦀🥮🧊

På samme plass fant han også en kodesnutt som han ikke helt forstår:

```
import struct  
melding = ""
for f in FLAG:
  melding += struct.pack('<I', 0x1F900 + f + 77).decode("utf-32le")
print(melding)
```

Er det mulig å finne flagget?

# Attempt

analyzing the above code it seems to get each characters in `FLAG` as a integer. So by testing `FLAG = "helsectf".encode()` I see the same emojies. So using the ASCII code for each character and packing that into a 32bit unsigned Little Endian integer (represented by `<I`). Which is decoded to be able to display as emojies.

So going backwards I need to get out 32 bits so 4 bytes at a time. Then unpack it, remove the `0x1F900` and `77` and what I'm left with is the ASCII representation of a regular character. 

```
melding = "🦵🦲🦹🧀🦲🦰🧁🦳🧈🦲🦺🥽🦷🥾🧀🦬🦯🦀🦴🧆🦛🦻🦲🦿🦬🦮🦮🦬🦯🦙🦶🦬🦼🦝🦽🦯🦿🦢🦸🧁🦬🦠🥽🦺🦬🦐🦡🦓🦬🦼🦽🦝🦴🦮🧃🦀🥮🧊".encode("utf-32le")
FLAG = ""
for i in range(0, len(melding), 4):
    chunk = melding[i:i+4]
    code_point = struct.unpack("<I", chunk)[0]
    original_code_point = code_point - 0x1F900 - 77
    FLAG += chr(original_code_point)
```

# Flag

```helsectf{em0j1s_b3gyNner_aa_bLi_oPpbrUkt_S0m_CTF_opPgav3!}```