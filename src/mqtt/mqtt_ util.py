import paho.mqtt.client as mqtt
import json as json
import ssl

class MqttUtil:

    def __init__(self, ip: str, port: int, username: str, password: str, ca: str, ):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_log = self.on_log

        self.ip = ip
        self.port = port
        self.keep_alive = 60
        self.username = username
        self.password = password
        self.ca = ca

        self.topic_to_listen = "#"
        self.running = False
        self.subscribed = False
        self.received_messages = []

    def setup(self):
        self.client.tls_set(self.ca, tls_version=ssl.PROTOCOL_TLSv1_2)
        self.client.tls
        self.client.connect(self.ip, self.port)



    def subscribe_topic(self, client, topic: str):
        client.subscribe(topic)

    def publish_data(self, topic: str, payload: str):
        self.client.publish(topic, payload)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to broker on ip:" + str(self.ip))

    def on_message(self, client, userdata, msg):
        json_data = json.loads(msg.payload)
        mqtt_resp = (msg.topic, json_data)
        self.received_messages.append(mqtt_resp)
        
    def on_log(self, client, userdata, level, buf):
        print("log: ", buf)

    def start_listening(self):
        self.client.loop_start()
        self.running = True

    def stop_listening(self):
        self.client.loop_stop()
        self.running = False
