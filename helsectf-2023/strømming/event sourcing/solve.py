from kafka import KafkaConsumer
import json

bootstrap_servers = 'ec2-13-49-134-84.eu-north-1.compute.amazonaws.com:9092'
security_protocol = 'SASL_PLAINTEXT'
sasl_mechanism = 'PLAIN'
auto_offset_reset = 'earliest'
username = 'user2'
password = 'helsectf2023ersuperduper'

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

# Sub to all
consumer.subscribe(pattern=".*")

data = []
message_batch = consumer.poll(timeout_ms=1000, max_records=5000)
for tp, messages in message_batch.items():
    for message in messages:
        
        ts = int(message.timestamp)
        order = message.key[0]
        value = message.value["intel"][0]["value"]
        data.append([ts, order, value])

data = sorted(data, key=lambda x: x[0])

string = [""] * 50

for idx, x in enumerate(data):
    if 1679480045000 <= x[0] <= 1679485045000:
        string[x[1]] = x[2]

print("".join(string))

