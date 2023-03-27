# event join (500)

En samarbeidspartner ønsker å sende oss en sensitiv melding kryptert med XOR og en OTP nøkkel. Begge deler blir strømmet til oss. Er det mulig å slå sammen strømmene og lese ut informasjonen?

```
bootstrap_servers: ec2-13-49-134-84.eu-north-1.compute.amazonaws.com:9092
security_protocol: SASL_PLAINTEXT  
auto_offset_reset: earliest
username: user3
password: helsectf2023varforenkelt  
```

# Writeup

Reading the events using same [solve.py](../event%20stream/solve.py) I used in [event stream](../event%20stream/) I quicky saw two topics and a lot of data on each of them.

```python
ConsumerRecord(
    topic='event_ciphertext',
    partition=1,
    offset=5,
    timestamp=1679301641928,
    timestamp_type=0,
    key=b'%',
    value={'encrypted_byte': '0x73'},
    headers=[],
    checksum=None, serialized_key_size=1, serialized_value_size=26, serialized_header_size=-1)
ConsumerRecord(
    topic='event_key',
    partition=4,
    offset=1,
    timestamp=1679301641925,
    timestamp_type=0,
    key=b'\x0e',
    value={'key_byte': '0xd9'},
    headers=[],
    checksum=None, serialized_key_size=1, serialized_value_size=20, serialized_header_size=-1)
```

I then tried to make a script which took XOR of the key_byte and encrypted_byte in the order they came. This gave me a bunch of garbage data. After trying a bit more I thought that I need to know the order. I then tried using timestamp but many of them came in the exact same time. Then it dawned for me, the `key` is random and wierd on all of them. If I get the integer value of that byte.. Yes, there we had it. A running number between 0 and a lot. So I matched up the byte with the key in a loop and got two arrays with the correct order. One for the `key` and one for the enccrypted `byte`.

Then I just had to run it and get the flag. See full [script here.](solve.py)

# Flag

```
helsectf{t0_str0mmer_ble_til_3n}
```