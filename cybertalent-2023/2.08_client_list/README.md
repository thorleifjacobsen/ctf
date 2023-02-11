# 2.08_client_list

Nå som jeg er tilkoblet ser jeg at her kjører en webserver for botnettet. # SKRIV MER HER


Ser man kan liste tilkoblet hosts om man vet prefix, heldigvis fant jeg prefix i konfigfilene til clienten som ligger på `shady-aggregator` med `strings`

```bash
archive@shady-aggregator:~$ curl localhost/f52e6101/list
ID               | NAME                             | LAST CHECKIN
-----------------+----------------------------------+--------------------
DEADBEEFDEADBEEF | test-3                           | 2023-01-03 22:25:55
42FD29AED93B779C | pwr-ws-caf5db                    | 2023-01-03 22:25:15
18F53CE5F533ACF7 | aurum                            | 2023-01-03 22:25:07
FLAGG            | 260c54fac22eb752739f2978fff9e021 | 2022-11-30 17:48:21
6ED230A80172B12E | pwr-ws-72fed1                    | 2022-11-16 11:00:32
F7D79C0F8995E423 | pwr-ws-64ca70                    | 2022-11-07 09:07:29
58A5FCF9FB1712B7 | pwr-ws-6d5602                    | 2022-06-30 01:47:58
93B58D54A5DB772A | pwr-ws-b5747c                    | 2022-06-11 17:25:14
CAFEBABECAFEBABE | test-2                           | 2022-02-23 08:06:40
46E894E2BEC4BD46 | pwr-ws-a8a1ce                    | 2022-02-06 22:53:02
14B6A84F08AC6887 | pwr-ws-e3fb32                    | 2022-01-27 17:24:04
DEADC0DEDEADC0DE | test-1                           | 2021-12-20 12:33:20
```

Der var flagget.

```
Kategori: 2. Oppdrag
Oppgave:  2.08_client_list
Svar:     260c54fac22eb752739f2978fff9e021
Poeng:    10

En liste over alle de infiserte klientene deres?

Den test-instansen som fortsatt sjekker inn så spennende ut...
```