from kafka import KafkaConsumer
import json


def deserialize_message(value):

    if value is None:
        return None

    return json.loads(value.decode("utf-8"))



consumer = KafkaConsumer(
    "order_events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="retail-consumer-group",
    value_deserializer=deserialize_message
)


print("Consumer started. Waiting for messages...")


for message in consumer:

    if message.value is None:
        print("Skipping empty message")
        continue


    print("\nReceived Event:")
    print(message.value)