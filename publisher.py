import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")


client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", 1883)

topic = input("Enter the MQTT topic: ")
client.loop_start()

while True:
    message = input("Enter message to publish (or 'q' to quit): ")

    if message.lower() == 'q':
        break

    # Publish the message to the topic
    client.publish(topic, message)

# Disconnect from the MQTT broker
client.loop_stop()
client.disconnect()
