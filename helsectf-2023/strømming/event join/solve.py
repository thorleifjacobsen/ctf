from kafka import KafkaConsumer
import json

bootstrap_servers = 'ec2-13-49-134-84.eu-north-1.compute.amazonaws.com:9092'
security_protocol = 'SASL_PLAINTEXT'
sasl_mechanism = 'PLAIN'
auto_offset_reset = 'earliest'
username = 'user3'
password = 'helsectf2023varforenkelt'

# Create Kafka-consumer
consumer = KafkaConsumer(
    bootstrap_servers=bootstrap_servers,
    security_protocol=security_protocol,
    sasl_mechanism=sasl_mechanism,
    auto_offset_reset=auto_offset_reset,
    sasl_plain_username=username,
    sasl_plain_password=password,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

consumer.subscribe(pattern=".*")

key_byte = []
encrypted_byte = []

message_batch = consumer.poll(timeout_ms=1000, max_records=500)
for tp, messages in message_batch.items():
    for message in messages:
        if message.topic == "event_key":
            key = message.key[0]
            eb = int(message.value['key_byte'],0)
            key_byte.append(f"{key} {eb}")
        if message.topic == "event_ciphertext":
            key = message.key[0]
            eb = int(message.value['encrypted_byte'],0)
            encrypted_byte.append(f"{key} {eb}")

encrypted_byte = sorted(encrypted_byte, key=lambda x: int(x.split()[0]))
key_byte = sorted(key_byte, key=lambda x: int(x.split()[0]))

for idx, x in enumerate(key_byte):
    key = int(x.split()[1])
    eb = int(encrypted_byte[idx].split()[1])
    print(chr(eb^key), end="")