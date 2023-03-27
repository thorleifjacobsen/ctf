from kafka import KafkaConsumer

bootstrap_servers = 'ec2-13-49-134-84.eu-north-1.compute.amazonaws.com:9092'
security_protocol = 'SASL_PLAINTEXT'
sasl_mechanism = 'PLAIN'
auto_offset_reset = 'earliest'
username = 'user1'
password = 'helsectf2023erkjempeg0y'

# Create Kafka-consumer
consumer = KafkaConsumer(
    bootstrap_servers=bootstrap_servers,
    security_protocol=security_protocol,
    sasl_mechanism=sasl_mechanism,
    auto_offset_reset=auto_offset_reset,
    sasl_plain_username=username,
    sasl_plain_password=password
)

# Subscribe to any topic
for topic in consumer.topics():
    print(f"Subscribing to topic: {topic}")
    consumer.subscribe(topic)

# Read all
for message in consumer:
    print(message.value)
