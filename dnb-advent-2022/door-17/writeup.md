# Challenge
So santa just got this outline for DJ Oilers symphony! It is a work in progress... so don't judge him to harshly...

https://htbbinaries.z1.web.core.windows.net/oilerstrack.mid

> **Hint:** Wov that music sounds... rough. Definitely not up to code...

# Writeup

Opened the file in a online midi to [json format decoder](https://tonejs.github.io/Midi/). Example of one beat here.

```json
{
    "duration": 0.5,
    "durationTicks": 960,
    "midi": 87,
    "name": "D#6",
    "ticks": 0,
    "time": 0,
    "velocity": 0.7086614173228346
}
```

Saw the midi tag seems like ascii. So I did some clever regexp search & replace in vscode to remove all but the number in the midi track and got this

Replace `^((?!midi).)*$\n` with blank line. Clean up a few lines. `\s*"midi": "(.*?)",\n` replace with `$1 ` and I have all notes on a newline.

```
87 101 108 108 32 73 32 103 117 101 115 115 32 104 97 108 102 32 97 32 102 108 97 103 32 105 115 32 98 101 116 116 101 114 32 116 104 97 110 32 110 111 32 102 108 97 103 46 46 46 10 36 123 52 64 49 70 95 119 64 121 95 112 48 105 110 55 10 72 111 112 101 32 121 111 117 32 102 105 110 100 32 116 104 101 32 114 101 115 116 46 46 46
```

Moved into [CyberChef](s://gchq.github.io/CyberChef) and I got this:

```Half Way Point
Well I guess half a flag is better than no flag...
${4@1F_w@y_p0in7
Hope you find the rest...
```

So looking at the other fields:

* duration is 0.5 on all
* durationTicks is 960 on all
* midi is used
* name is the note in text for midi
* ticks is +960 every note so cant be this.
* time is incrementing 0.5 every note matching duration
* velocity is the same on all.

Googling the Midi format I found [this](http://www.music.mcgill.ca/~ich/classes/mumt306/StandardMIDIfileformat.html#:~:text=MIDI%20Files%20are%20made%20up,the%20chunk%20type%20is%20introduced.)

Using this I found 

```
All meta-events begin with FF, then have an event type byte (which is always less than 128), and then have the length of the data stored as a variable-length quantity
```

Looking at the HxD I can see 3 occurances of FF 01 XX and 01 seems to be Text events. So just containing some text. But that might be something?

```
FF 01 len text Text Event

1st: FF 01 06 30 43 62 64 66 30 (0Cbdf0)
2nd: FF 01 08 48 6F 64 30 63 62 43 62 (Hod0cbCb)
3rd: FF 01 0B 30 6F 60 60 30 6F 60 5F 3F 65 4E (0o``0o`_?eN)
```

Could not find anything out with that at this moment. Late at night so maybe tomorrow. But quickly I'll also note the velocity, weird number?

```
0.7086614173228346
```

And the track name: `From Oiler With Love`.

Googling a bit and looking around at this moment. SLEEP TIME!

New day, started with the text meta events from the midi file. I tossed the hexes into [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')ROT47(47)&input=MzAgNDMgNjIgNjQgNjYgMzAKNDggNkYgNjQgMzAgNjMgNjIgNDMgNjIKMzAgNkYgNjAgNjAgMzAgNkYgNjAgNUYgM0YgNjUgNEUK) and it seems like it is just gibberish But after a while I test all the "brute force" methods. Searching for a string ending with }. XOR with a key using Track Name = Nothing, ROT13 = Nothing, ROT47 and there.. At the 47th.. So it is plain ROT57! 

```_r357_w@5_43r3_@11_@10n6}```

Full flag:

```${4@1F_w@y_p0in7_r357_w@5_43r3_@11_@10n6}```