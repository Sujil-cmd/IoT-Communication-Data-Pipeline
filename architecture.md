# MQTT Architecture

Sensor/ESP32 Simulator → MQTT Publisher → MQTT Broker → MQTT Subscriber → SQLite → Analysis

**Broker:** test.mosquitto.org  
**Port:** 1883  
**Topic:** vertexmind/iot/sensor  
**QoS:** 1  
**Payload:** JSON

For a local Mosquitto broker, change `BROKER_HOST` in `publisher.py` and `subscriber.py` to `localhost`.
