# Needle in the Haystack

While walkin around in the home base a soldier comes running up to you.

THE KEY LIST, WE LOST IT!

After calming him down he starts to explain in more detail:

Every day the enemy broadcasts an unencrypted message saying which key to use from the list. In secret we managed to steal a copy of the list, but it has now been lost. We know the pattern of the list, but manually writing it out would take years. You must help us solve this problem.

The pattern is:

1 letter between "c" and "m" - 1 digit - 2 letters between "f" and "z" - 1 number between 2 and 7 - 1 number between 1 and 5
I remember key number 0 and 1 were c0ff21 and c0ff22 respectively.

and the correct key today is key number 585937

The flag will be in the form "UiTHack24{insert key}"

# Writeup

This one I found kinda boring. I did not just want to write a long script to do this so I asked ChatGPT. And he delivered both in Python and NodeJS. I used the [NodeJS](solve.js) one and got the flag.

```javascript
UiTHack24{g4lg32}
```