# IoT Communication & Data Pipeline - Mission 2

This project demonstrates an MQTT-based IoT data pipeline using Python.

## Pipeline
Sensor simulator → MQTT Publisher → MQTT Broker → MQTT Subscriber → SQLite Database

## Technologies
Python, Paho MQTT, MQTT, Mosquitto/public MQTT broker, JSON, SQLite, CSV, Matplotlib.

## Files
- `publisher.py` - publishes simulated sensor readings.
- `subscriber.py` - receives MQTT messages and stores them in SQLite.
- `local_pipeline_demo.py` - offline demonstration of Publish → Subscribe → Store.
- `sensor_data.csv` - sample sensor dataset.
- `sensor_pipeline_plot.png` - sensor visualization.
- `iot_data.db` - sample database.
- `architecture.md` - architecture and data flow.
- `Mission2_IoT_MQTT_Report.pdf` - project report.
- `requirements.txt` - dependencies.

## Run
1. `pip install -r requirements.txt`
2. Start `python subscriber.py`
3. In another terminal run `python publisher.py`

If an MQTT broker is unavailable, run:
`python local_pipeline_demo.py`

## Example JSON
```json
{"device_id":"ESP32_SIM_01","timestamp":"2026-09-27T10:00:00","temperature_c":27.25,"humidity_percent":61.4}
```
