print("Producer started")

from kafka import KafkaProducer
import json
import time
from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)


products = [
    "Laptop",
    "Mobile",
    "Headphones",
    "Keyboard",
    "Mouse"
]


def generate_order():

    order = {
        "event_type": "order_created",
        "order_id": random.randint(10000,99999),
        "customer_id": random.randint(1000,5000),
        "product": random.choice(products),
        "quantity": random.randint(1,5),
        "price": random.randint(500,80000),
        "event_time": datetime.now().isoformat()
    }

    return order



while True:

    order_event = generate_order()

    producer.send(
        "order_events",
        value=order_event
    )

    producer.flush()

    print("Sent:", order_event)

    time.sleep(5)