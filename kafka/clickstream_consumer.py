from kafka import KafkaConsumer
import json


def deserialize_message(value):

    if value is None:
        return None

    return json.loads(value.decode("utf-8"))



consumer = KafkaConsumer(

    "clickstream_events",

    bootstrap_servers="localhost:9092",

    auto_offset_reset="earliest",

    enable_auto_commit=True,

    group_id="clickstream-consumer-group",

    value_deserializer=deserialize_message

)



print("Clickstream consumer started. Waiting for events...")



for message in consumer:


    if message.value is None:
        print("Skipping empty message")
        continue


    print("\nReceived Clickstream Event:")

    print(message.value)