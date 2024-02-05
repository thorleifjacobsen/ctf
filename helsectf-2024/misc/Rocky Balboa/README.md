# Rocky Balboa

Etter grundige undersøkelser på internett, har vårt sikkerhetsteam oppdaget en mistenkelig video. Videoen viser en hacker som bryter seg inn i et høyt sikret datasystem. Vi har også oppdaget et passordhash som ser ut til å være relatert til hackeren: `$2b$14$WpeU3BB4A1FpeOoTRa100O3/a5RSzhnvFJyxOEZ3v2z4It/gM71Eu`

Det virker som hackeren liker å høre på Rocke Deg sanger mens hen sorterer igjennom samlingen sin av forskjellige ordbøker. Ordbøker er veldig viktig når man skal knekke passord!

Oppgaven går ut på å knekke passordet fra hashen over. Passordet leveres wrappet i flaggformatet, slik: `helsectf{<passsord>}`

PS: passordet innholder opptil flere mellomrom

[⬇️ output.mp4](output.mp4)

# Writeup

On this one I was a bit out and about. First I found all songs in rocky put them in a list. Then all lyrics of all those songs. Nothing hit the hash.

I then tried `rockyou.txt` as it hints towards very heavily. The mp4 file has a hint pointing to this as well.

```
Artist                          : mr hint
Album                           : rock
Comment                         : Playing in the street, gonna be a big man someday
Genre                           : you
```

That was due to finish in around 3 weeks. 

```
:00:00:37 0.00% (ETA: 2024-02-16 12:34) 0g/s 7.291p/s 7.291c/s 7.291C/s 0123456789..sweet
```

No time for that. So after a while I was told to read it a a bit more carefully. And got a hint about the spaces in the hint. The password contains multiple spaces. So filtering out `rockyou.txt` to a `rockyou_space.txt` where it only had characters with space the hash was cracked in under 15 minutes. 

The password was:

```
being so stupid becuz of cheer
```

I also had a [solve.py](solve.py) script which I used eariler on before using john. I modified it to use multiple spaces as a requirement and it also got the flag. But that is a slow method.

# Flag

```
helsectf{being so stupid becuz of cheer}
```