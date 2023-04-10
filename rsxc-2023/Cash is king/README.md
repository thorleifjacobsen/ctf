# Cash is king

Can you trick the system into giving you some more money?

http://rsxc.no:9004

# Writeup

I get a message:

```
River Security cash machine.

Get >= 500 cash for Easter spending.

Cash:100
User:Easter Bunny
```

Source code shows a input field with a long hash.

```
<input type="hidden" method="GET" name="data" value="383d81e4af618e23c1ee3ca2f47e85d39e71770d2b196fd55d0db20fd91ece729574e91de1fbbf893a90ae35b95fd5fd" />
```

Putting this in the `?data=hash` gives the same result. But once I put in some weird values I get som error output:

```
Warning: hex2bin(): Hexadecimal input string must have an even length in /var/www/html/index.php on line 24
Warning: mcrypt_decrypt(): Received initialization vector of size 0, but size 16 is required for this encryption mode in /var/www/html/index.php on line 35
```

So adding 16 valid hex characters `http://rsxc.no:9004/?data=11221122112211221122112211221122` this was the output:

```
River Security cash machine.

Get >= 500 cash for Easter spending.

�H߽2��l��D�zna�
```

So the text is a direct result of the bytes. So changing bytes I see that I get different values. So if I treat each letter as a byte, and goes to the 6th byte and modify it with 1.. 

`383d81e4af 61 8e23c1ee3ca2f47e85...`

Change it to 62. Now I suddenly have 200 cash. So adding a few more `65` I get 500 and a flag.

```
383d81e4af658e23c1ee3ca2f47e85d39e71770d2b196fd55d0db20fd91ece729574e91de1fbbf893a90ae35b95fd5fd
```

# Flag

```
RSXC{CRYPTO_FAIL_MAKES_EASTER_WIN}
```