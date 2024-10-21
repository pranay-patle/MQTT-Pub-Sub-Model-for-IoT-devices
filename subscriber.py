import paho.mqtt.client as mqtt

# MQTT settings
broker_ip = 'IP_ADDRESS_OF_BROKER'  # Replace with broker IP
topic = "sensor/dht11"

# Define the callback function for when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

# Create an MQTT client instance
client = mqtt.Client()

# Attach the message callback function
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_ip, 1883, 60)

# Subscribe to the topic
client.subscribe(topic)

# Start the MQTT client loop to listen for messages
client.loop_forever()
