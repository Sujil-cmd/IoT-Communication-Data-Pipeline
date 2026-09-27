import json, queue, sqlite3, random
from datetime import datetime

messages = queue.Queue()

for _ in range(5):
    payload = {
        "device_id": "ESP32_SIM_01",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "temperature_c": round(random.uniform(24,30),2),
        "humidity_percent": round(random.uniform(50,70),2)
    }
    messages.put(json.dumps(payload))
    print("PUBLISHED:", payload)

db = sqlite3.connect("local_demo.db")
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS sensor_readings(
id INTEGER PRIMARY KEY AUTOINCREMENT, device_id TEXT,
timestamp TEXT, temperature_c REAL, humidity_percent REAL)""")

while not messages.empty():
    d = json.loads(messages.get())
    cur.execute("""INSERT INTO sensor_readings
    (device_id,timestamp,temperature_c,humidity_percent)
    VALUES(?,?,?,?)""",
    (d["device_id"],d["timestamp"],d["temperature_c"],d["humidity_percent"]))
    print("STORED:", d)

db.commit(); db.close()
print("Pipeline demo completed: Publish -> Subscribe -> Store")
