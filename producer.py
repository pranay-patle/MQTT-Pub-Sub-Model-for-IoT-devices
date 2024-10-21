import time
import paho.mqtt.client as mqtt
import Adafruit_DHT

# Sensor configuration
sensor = Adafruit_DHT.DHT11
gpio_pin = 4  # Use GPIO pin where the DHT11 is connected

# MQTT settings
broker_ip = '192.168.122.234'  # Replace with broker IP
topic = "sensor/dht11"

# Define callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message {mid} published")

# Create an MQTT client instance
client = mqtt.Client()

# Assign callbacks
client.on_connect = on_connect
client.on_publish = on_publish

try:
    # Connect to the MQTT broker
    client.connect(broker_ip, 1883, 60)

    # Start the MQTT client loop
    client.loop_start()

    while True:
        # Read data from the DHT11 sensor
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_pin)

        if humidity is not None and temperature is not None:
            # Create a message payload
            payload = f"Temperature: {temperature}C, Humidity: {humidity}%"
            print(f"Publishing: {payload}")
            
            # Publish the payload to the MQTT broker
            client.publish(topic, payload)
        else:
            print("Failed to retrieve data from the sensor")
        
        # Wait for 5 seconds before reading the data again
        time.sleep(5)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Stop the MQTT client loop (optional when ending the program)
    client.loop_stop()
