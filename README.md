# IoT MQTT Sensor Publisher

This project simulates a local sensor device (like a Raspberry Pi) acting as an edge node in an IoT pipeline. The Python script generates fake temperature and humidity readings and publishes them to an MQTT broker using the `paho-mqtt` library.

This forms the "edge" layer of a broader data pipeline that includes:
- MQTT (Mosquitto) broker
- Apache Kafka (stream processing)
- PostgreSQL (data storage)
- Grafana (visualization)

---

## 📦 Project Components

- ✅ **Raspberry Pi Publisher** – Generates and sends sensor data
- 🔄 **MQTT Broker** (e.g. Mosquitto)
- 🔁 **Kafka Producer/Bridge** – Forwards MQTT messages into Kafka topics
- 🗃 **Kafka Consumer** – Writes to a PostgreSQL database
- 📊 **Grafana Dashboard** – Visualizes real-time and historical sensor data

---

## 🍓 Raspberry Pi Script

### `sensor_publisher.py`

This Python script simulates sensor readings and publishes them to an MQTT topic every few seconds.

#### Simulated Payload:

```json
{
  "device_id": "pi-room-01",
  "timestamp": "2025-05-17T15:00:00Z",
  "temperature_c": 22.8,
  "humidity_percent": 48.2
}
