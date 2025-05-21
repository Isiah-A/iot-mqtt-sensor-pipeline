import paho.mqtt.client as mqtt
import mysql.connector
import json

MQTT_BROKER = '100.105.177.28'
MQTT_PORT = 1883
MQTT_TOPIC = 'sensor/temperature'

# Mysql Database config

DB_HOST = 'mysql' #name for sql containter for docker
DB_PORT = '3306' #default port for mysql
DB_NAME = 'temperature_db'
DB_USER = 'user'
DB_PASSWORD = 'password'


# Define the callback whe a message is recieved

def on_message(client, userdata, msg):
    print(f"Recieved message: {msg.payload.decode()}")
    data = json.loads(msg.payload.decode())

# Insert data into mysql
try:
    connection = mysql.connector.connect(
    host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature_data (timestamp, temperature) VALUES (%s, %s)",(data['timestamp'], data['temperature']))
    connection.commit()
    cursor.close()
    connection.close()
    print("Data inserted successfully.")
except mysql.connector.Error as err:
    print(f"Error inserting data into database: {err}")

# Setup MQTT client

client = mqtt.Client()
client.on_message = on_message

# Connect to the MQTT broker

client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Subscribe to the MQTT topic

client.subscribe(MQTT_TOPIC)

# Start the MQTT client loop

client.loop_forever()
