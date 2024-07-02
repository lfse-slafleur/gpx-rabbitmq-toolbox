# Simple RabbitMQ example

# Start the broker
To start RabbitMQ as broker:
```bash
docker compose up
```

Use the `-d` flag if you want to start it in the background.
We will use the default root user `root` with password `1234` and not use separate
user accounts for this example. The Web UI is available at `http://localhost:15672/`.

RabbitMQ listens on port 1883 for any MQTT connections and on port 5672 for any AMQP connections.

# To start the subscriber and publisher
An example subscriber is provided which prints all messages received on the topic
`some-topic/example`. The RabbitMQ MQTT plugin will create a queue per subscriber which are
bound to the routing key `some-topic/example`. So as long as the MQTT publisher publishes
to the MQTT topic `some-topic/example`, RabbitMQ will route the messages correctly.

To setup the Python environment to run the subscriber and publisher:
```bash
python3 -m venv ./.venv/
. .venv/bin/activate
pip install -r ./requirements.txt
```

Then to run the subscriber:
```bash
. .venv/bin/activate # This activates the Python virtual environment. Should be run if virtual environment was not already activated.
python3 simple_subscriber.py
```

The subscriber will print any message it receives on the topic `some-topic/example` as text. 

Then to send a single message with the current time:
```bash
. .venv/bin/activate # This activates the Python virtual environment. Should be run if virtual environment was not already activated.
python3 simple_publisher.py
```

The publisher is expected to print nothing.
