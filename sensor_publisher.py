import time
import json
import random
import paho.mqtt.client as mqtt
from datetime import datetime, timezone

# Configuration 

# Replace with ip once mosquitto is installed on Z

BROKER = "100.113.6.54"

# Default MQTT port for mosquitto is 1883

PORT = 1883

# MQTT topic the fake sensor data will be published to

TOPIC = "room/conditions"

# Unique ID for device

DEVICE_ID = "Zepi"

# Simulated sensor function

def get_sensor_data():
	"""
	Simulate reading temperature and humidity from a sensor.
	
	Retruns a dictionary with:
	DEVICE_ID: ID of the device sending the data
	timestamp: Current UTC time in ISO 8601 format
	temperature_c: random temperature value in celsius
	humidity_precent: random humidity value as percentage
	"""
	return {
	"device_id": DEVICE_ID,
	"timestamp": datetime.now(timezone.utc).isoformat(),
	# random.uniform(a , b, ...) returns a random float between values
	"temperature_c": round(random.uniform(20.0, 25.0),2),
	"humidity_percent": round(random.uniform(40.0, 55.0),2)
	}

# MQTT setup and publishing loop

# Create new MQTT client instance

client = mqtt.Client()

# connect the client to MQTT broker
# IP address and port have to be reachable...

client.connect(BROKER, PORT, 60)

# start the main publishing loop
try:
	while True:
		# generate fake sensor data
		payload = get_sensor_data()

		# convert the dict to a JSON string before sending
		payload_json = json.dumps(payload)

		#publish the data to the specfied MQTT topic
		client.publish(TOPIC, payload_json)

		# print confirmation
		print(f"Published: {payload}")

		# wait 5 seconds before sending next message
		time.sleep(5)

except KeyboardInterrupt:
	# Allow clean shutdown when closing
	print("Stopped by user.")
	client.disconnect()


