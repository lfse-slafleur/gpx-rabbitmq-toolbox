"""
Example taken from README https://pypi.org/project/paho-mqtt/#publish
"""
from datetime import datetime

import paho.mqtt.publish as publish



publish.single(topic="some-topic/example",
               payload=f"Hello from example! The time is: {datetime.now()}".encode(),
               hostname="localhost",
               port=1883,
               auth={"username": "root", "password": "1234"})
