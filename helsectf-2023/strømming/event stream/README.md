# event stream (499)

Vi har mottatt påkoblingsinformasjon til en strøm med etterretningsinformasjon. Kan du lese strømmen og rapportere eventuelle interessante funn?

```
bootstrap_servers: ec2-13-49-134-84.eu-north-1.compute.amazonaws.com:9092
security_protocol: SASL_PLAINTEXT  
auto_offset_reset: earliest
username: user1
password: helsectf2023erkjempeg0y
```

# Writeup

A bit of googling shows this is some kafka streams. I'm not used to play with this but I managed to cook up a [script](solve.py) which read the topics where I found `evnet_stream` as the only topic. Then I used the subscribe function to connect to that and a lot of data was spit out.

```
...
b'{"feed": "emergingthreats", "source": "https://rules.emergingthreats.net/blockrules/compromised-ips.txt", "action": "create", "intel": [{"type": "ip", "value": "188.10.38.83"}]}'
b'{"feed": "emergingthreats", "source": "https://rules.emergingthreats.net/blockrules/compromised-ips.txt", "action": "create", "intel": [{"type": "ip", "value": "188.127.254.248"}]}'
b'{"feed": "helsectf", "source": "https://helsectf2023-6ac4e1c6d8855c1bd96a.ctfd.io/", "action": "create", "intel": [{"type": "flag", "value": "helsectf{3n_STr0m_meD_eV3ntS}"}]}'
b'{"feed": "emergingthreats", "source": "https://rules.emergingthreats.net/blockrules/compromised-ips.txt", "action": "create", "intel": [{"type": "ip", "value": "188.166.224.80"}]}'
b'{"feed": "emergingthreats", "source": "https://rules.emergingthreats.net/blockrules/compromised-ips.txt", "action": "create", "intel": [{"type": "ip", "value": "188.166.228.173"}]}'
...
```

And there we foudn the flag.

# Flag

```
helsectf{3n_STr0m_meD_eV3ntS}
```