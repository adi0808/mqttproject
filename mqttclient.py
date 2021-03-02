from paho.mqtt import client as mqtt_client
import time
import config


# Class to create the connection and send and receive message
class MqttClient:

    @staticmethod
    def connect_mqtt(addr, port):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client()
        client.on_connect = on_connect
        client.connect(addr, port)
        return client

    @staticmethod
    def publish(client, topic, message):

        time.sleep(1)
        result = client.publish(topic, message)
        status = result[0]
        if status == 0:
            print(f"Send `{message}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

    @staticmethod
    def subscribe(client, topic):

        print("subscribing to client: {}".format(client))

        def on_message(client, userdata, msg):
            data = msg.payload.decode()
            print(f"Received `{data}` from `{msg.topic}` topic")
            if topic not in config.data_received:
                config.data_received[topic] = [data]
            else:
                config.data_received[topic].append(data)

            print("sub1-py:  {}".format(config.data_received))

        client.subscribe(topic)
        client.on_message = on_message


client = mqtt_client.Client()


# Method to publish message to the broker
def publish_message(addr, port, topic, message):
    global client
    client = MqttClient.connect_mqtt(addr, port)
    MqttClient.publish(client, topic, message)


# Method to subscribe message to the broker
def subscribe_message(addr, port, topic):
    global client
    client = MqttClient.connect_mqtt(addr, port)
    time.sleep(1)
    MqttClient.subscribe(client, topic)
    client.loop_forever()


