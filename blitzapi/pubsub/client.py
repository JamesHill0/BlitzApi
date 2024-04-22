import paho.mqtt.client as mqtt
import time

class PubSubClient:
    def __init__(self, url='localhost', port=1883):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.url = url
        self.port = port
        self.mfa_code = None  # Variable to store the MFA code
        self.received_code = False  # Flag to check if code is received
        self.topic = 'nationwide/J.Greer@biltd.com'

        # Bind instance methods as callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

    def on_connect(self, client, userdata, flags, reason_code, properties=None):
        print(f"Connected with result code {reason_code}")

    def on_disconnect(self, client, userdata, flags, reason_code, properties=None):
        print("Disconnected from the MQTT broker with result code", reason_code)

    def on_message(self, client, userdata, msg):
        print(f"Received message on {msg.topic}: {msg.payload.decode()}")
        if msg.topic == self.topic:
            self.mfa_code = msg.payload.decode()
            self.received_code = True

    def connect(self):
        self.client.connect(self.url, self.port, 60)
        self.client.loop_start()

    def subscribe_for_code(self, timeout=15):
        self.connect()
        self.client.subscribe(self.topic)
        start_time = time.time()

        while not self.received_code and (time.time() - start_time) < timeout:
            time.sleep(0.5)  # Wait for messages to arrive

        self.client.unsubscribe(self.topic)  # Unsubscribe after receiving the code or after the timeout
        self.disconnect()

    def publish_code(self, message):
        
        self.connect()

        self.client.publish(self.topic, message)

        self.disconnect()

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

