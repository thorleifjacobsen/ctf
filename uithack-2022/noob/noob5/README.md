# Noob5

There might be ways around what you are not allowed on this server. A lot happens under the hood you know, running in silence, serving bigger purposes revealing a piece of cloth or similar material, typically oblong or square, attachable by one edge to a pole or rope and used as the symbol or emblem of a country or institution or as a decoration during public festivities.

The username for this , is noob5.
The server name is wwww.limewire.td.org.uit.no.
Password is noob4's flag

# Writeup

Hinting is about something else running. Checked `ss -nlp` found port 80 and 8080 running. Curl on 80 shows default nginx welcome screen. Curl on 8080 shows a program and in there is a flag.

```
noob5@limewire:/tmp$ curl --silent localhost:8080 | grep UiT
    <p style="color:white;">UiTHack23{cant_grep_this}</p>
var english = "UiTHack23{cant_grep_this}";
```