# Randomness

Become the admin user

http://rsxc.no:9003

# Writeup

First glance I get an unique cookie with a PHPSESSION id. 

My user is `39342` with the id `4d7a6b7a4e44493d6d65345249334575`

FromHex returns: `MzkzNDI=me4RI3Eu`, this is two parts: 

```
Part 1: MzkzNDI= (base64 for 39342)
Part 2: me4RI3Eu
```

Seeing the source code there is a hint:

```html
<!-- Hint: No content discovery or guess work is needed. Work on the values at hand, which you are sending to the application. -->
```

This is kinda what I've already discovered but atleast that hint will keep me on this path, so what is the second part. Guessing it is what kind of an user I am? Or checksum. Well I try a few things including changing the first part to the number 1 which results in this hex `4d413d3d6d65345249334575` but this results in:

```
Become admin to win this game. You are user: #1 �
```

After a lot of testing I come to think maybe the last bit is .. just what the task is named `Randomness`. So I discard the last 8 bytes just setting them as `FF`s. And see that it seems to require 8 bytes. Maybe I just need to pad the 1? to `00001`. This results in 16 bytes where the 8 first are the `00001`

`4d4441774d44453dFFFFFFFFFFFFFFFF`

Voila.. So simple yet so hard to think of.. 

```
Wow! You actually did it! You're the admin! Here is your flag: RSXC{SEQUENCING_FINDS_RANDOMNESS_FLAWS}
```

# Flag

```
RSXC{SEQUENCING_FINDS_RANDOMNESS_FLAWS}
```