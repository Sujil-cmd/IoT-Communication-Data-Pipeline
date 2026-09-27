import json, random, time
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER_HOST = "test.mosquitto.org"
BROKER_PORT = 1883
TOPIC = "vertexmind/iot/sensor"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="mission2-publisher")
client.connect(BROKER_HOST, BROKER_PORT, 60)

try:
    for _ in range(10):
        payload = {
            "device_id": "ESP32_SIM_01",
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "temperature_c": round(random.uniform(24, 30), 2),
            "humidity_percent": round(random.uniform(50, 70), 2)
        }
        result = client.publish(TOPIC, json.dumps(payload), qos=1)
        result.wait_for_publish()
        print("Published:", payload)
        time.sleep(2)
finally:
    client.disconnect()
