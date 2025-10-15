# Kontantkort

<Redacted> needs to refill his prepaid sim, and telenor just deployed a new refilling system but he has forgotten his number, can you find his number and test the system?

https://kontant.telenor.live

# Writeup

Found his website and the number, inputted it and saw the flag in a request to `/lade/valider/<number>`.

```json
{"prepaid":true,"balanceExceeded":false,"name":"<Redacted>>","flag":"telenor{the_database_messed_up}"}
```


# Flag

```
telenor{the_database_messed_up}
```