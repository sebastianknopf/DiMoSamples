import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Verbindung erfolgreich!")

        client.subscribe("#")
    else:
        print("Verbindungsfehler, Code:", rc)

def on_message(client, userdata, msg):
    topic = msg.topic
    print(f"Nachricht auf Topic '{topic}' eingegangen.")


if __name__ == '__main__':
    
    client: mqtt.Client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("test.mosquitto.org", 1883, 60)

    client.loop_forever()

        