import json, sqlite3
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER_HOST = "test.mosquitto.org"
BROKER_PORT = 1883
TOPIC = "vertexmind/iot/sensor"
DB_NAME = "received_sensor_data.db"

db = sqlite3.connect(DB_NAME, check_same_thread=False)
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS sensor_readings(
id INTEGER PRIMARY KEY AUTOINCREMENT,
device_id TEXT, timestamp TEXT, temperature_c REAL,
humidity_percent REAL, received_at TEXT)""")
db.commit()

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected. Subscribing to", TOPIC)
    client.subscribe(TOPIC, qos=1)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        cur.execute("""INSERT INTO sensor_readings
        (device_id,timestamp,temperature_c,humidity_percent,received_at)
        VALUES(?,?,?,?,?)""",
        (data["device_id"], data["timestamp"], data["temperature_c"],
         data["humidity_percent"], datetime.now().isoformat(timespec="seconds")))
        db.commit()
        print("Received and stored:", data)
    except Exception as e:
        print("Invalid message:", e)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="mission2-subscriber")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_HOST, BROKER_PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Subscriber stopped.")
finally:
    client.disconnect()
    db.close()
