# fingeravtrykk (500)

Jan Aksel den tredje (JA3) elsker fingeravtrykk. Det beste han vet er å ta fingeravtrykk av intetanende besøkende på nettstedet sitt selv om de bruker HTTPS.

Med et fingeravtrykk kan han gjenkjenne hvilken klientapplikasjon som brukes.

Det Jan Aksel hater aller mest i hele verden er ondsinnet kode, og spesielt Emotet. Hvis Emotet kobler til nettstedet vil det få en kraftig advarsel.

NB! Oppgaven har et selv-signert sertifikat, dette er ikke viktig og inneholder ikke noe ifm å løse oppgaven.

https://0.cloud.chals.io:15185/

# Writeup

Task opens a website where I get a JA3 hash of my browsers fingerprint. Chrome seems to randomize thihs as I get a new on for every request. But my CURL gives the same. 

```
$ curl 'https://0.cloud.chals.io:15185/' --insecure
<html><head><title>Et nettsted</title></head><h1>Dette er Jan Aksel den tredje (JA3) sitt nettsted.</h1><br><h1>Ditt JA3 hash er 110d16d6deea0918fb3fec92406ba693</h1><br><h1>Du er ikke Emotet</h1></html>                                                                                                                                                                                            ```

Guessing it is detecting who you are based on some kind of ssl fingerprint or something? 