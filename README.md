# mqtt-rf-bridge
A small Python app to converse between MQTT messages and 433MHz RF signals.
This acts as a bridge between [Paho MQTT](https://github.com/eclipse/paho.mqtt.python) and [rpi-rf](https://github.com/milaq/rpi-rf).
Requirements: `pip3 install paho-mqtt rpi-rf yaml`

Implemented:
- [x] Configuration file definitions for topics, GPIO pins, RF transmit/recieve codes
- [x] Subscribing to MQTT Topic
- [x] Writing data to RF Transmitter
- [ ] Systemd user service ([for example](https://nts.strzibny.name/systemd-user-services/))
- [ ] Receiving data from RF Reciever
- [ ] Publishing to MQTT Topic

---
## `config.yaml`
- `hostname` : MQTT Broker hostname
- `topics` : A list of MQTT Topics to subscribe to. For each topic you can define:
  - `rf_codes`: On/Off codes to be sent to your RF Transmitter
  - `gpio` : The GPIO connections for the transmitter/receiver.
---
  
