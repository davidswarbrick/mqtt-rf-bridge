from yaml import safe_load
from rpi_rf import RFDevice
import paho.mqtt.client as mqtt
import logging

class RFTransmitSingleBitFromTopic(RFDevice):
    def __init__(self, config, topic):
        super().__init__(config["topics"][topic]["gpio"]["transmit"])
        self.enable_tx()
        self.output_state = False
        self.rf_codes = config["topics"][topic]["rf_codes"]

    def set(self, val=True):
        self.tx_code(self.rf_codes[val])
        logging.debug("Transmitted: ", self.rf_codes[val])
        self.output_state = val

    def toggle(self):
        self.set(not self.output_state)


with open("config.yaml", "r") as cfg_file:
    config = safe_load(cfg_file)


topic_rf_dict = {}
for topic in config["topics"]:
    topic_rf_dict[topic] = RFTransmitSingleBitFromTopic(config, topic)


def on_connect(client, userdata, flags, rc):
    logging.info("Connected with result code" + str(rc))
    for topic in userdata.keys():
        client.subscribe(topic)


def on_message(client, userdata, msg):
    logging.debug("Topic:   ", msg.topic)
    logging.debug("Payload: ", msg.payload)
    if msg.payload == b"0" or msg.payload == b"1":
        logging.info("Setting value: ", msg.payload)
        userdata[topic].set(int(msg.payload.decode("utf-8")))
    else:
        logging.info("Toggling value")
        userdata[topic].toggle()


client = mqtt.Client(userdata=topic_rf_dict)
client.on_connect = on_connect
client.on_message = on_message

client.connect(config["hostname"])
client.loop_forever()
# rf_transmitter.cleanup()
