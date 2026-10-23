from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)


pages = [
    "home",
    "laptop",
    "mobile",
    "headphones",
    "checkout"
]


actions = [
    "view",
    "click",
    "add_to_cart",
    "purchase"
]


def generate_click_event():

    event = {

        "event_type": "clickstream",

        "user_id": random.randint(1000,5000),

        "session_id": random.randint(10000,99999),

        "page": random.choice(pages),

        "action": random.choice(actions),

        "timestamp": datetime.now().isoformat()

    }

    return event



print("Clickstream producer started")


while True:

    event = generate_click_event()

    producer.send(
        "clickstream_events",
        value=event
    )

    producer.flush()

    print("Sent:", event)

    time.sleep(3)