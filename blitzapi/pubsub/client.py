# File: blitzapi/pubsub/client.py
import paho.mqtt.client as mqtt

class PubSubClient:
    def __init__(self, url, port):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.url = url
        self.port = port
        # Bind instance methods as callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, reason_code, properties=None):
        print(f"Connected with result code {reason_code}")
        # You might want to add auto-subscription to topics here if needed

    def on_message(self, client, userdata, msg):
        print(f"Received message on {msg.topic}: {msg.payload.decode()}")

    def connect(self):
        self.client.connect(self.url, self.port, 60)
        self.client.loop_start()

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def publish(self, topic, message):
        self.client.publish(topic, message)

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
