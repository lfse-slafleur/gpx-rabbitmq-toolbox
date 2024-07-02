"""
Example taken from README https://pypi.org/project/paho-mqtt/#subscribe
"""
import paho.mqtt.client as mqtt


def on_connect(client, userdata, connect_flags, reason_code, properties):
    print('Connected to broker!')
    client.subscribe(topic='some-topic/example')


def on_connect_fail(client, userdata):
    print('Connection failed.')


def on_message_print(client, userdata, message):
    print("[Topic=%s] %s" % (message.topic, message.payload))
    userdata["message_count"] += 1
    if userdata["message_count"] >= 5:
        # it's possible to stop the program by disconnecting
        client.disconnect()


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username='root', password='1234')

client.on_connect = on_connect
client.on_connect_fail = on_connect_fail
client.on_message = on_message_print
client.user_data_set({"message_count": 0})

client.connect(host="localhost", port=1883)

client.loop_forever()
print('After client loop forever')