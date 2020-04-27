import paho.mqtt.client as mqtt
import log
import re
import json
import cmdhandler

logger = log.NewLogger(__name__)
MQTT_TOPIC = 'result/device/+/#'
Dev_name = 'device/([^/]+)'   # strip device_id
MQTT_CLIENT_ID = 'Design_Client'
MQTT_ADDRESS = '127.0.0.1'

class MqClient:
    def __init__(self):
        self.mqtt = mqtt.Client(
            client_id=MQTT_CLIENT_ID,
            clean_session=True
        )
        self.mqtt.enable_logger(logger)
        self.mqtt.on_message = self.on_message
        self.mqtt.on_connect = self.on_connect
        self.mqtt.on_disconnect = self.on_disconnect

    def on_connect(self,mqtt,obj,flags,rc):
        if rc == 0:
            logger.debug(
                "Connected to MQTT broker %s",(MQTT_ADDRESS)
            )
        logger.debug("Subscribing to topic %s" % MQTT_TOPIC)
        self.mqtt.subscribe(MQTT_TOPIC)

    def on_disconnect(self,mqtt,obj,rc):
        if rc !=0:
            logger.debug(
                "disconnected from MQTT broker %s",(MqttAddress)
            )

    def on_message(self,mqtt,obj,msg):
        logger.debug("Received message from topic %r: %r", msg.topic, msg.payload)
        device_name = re.search(Dev_name, msg.topic).group(1)   # get device_id
        handleMSG = cmdhandler.CMDHandler(msg.payload.decode('utf-8'),device_name)  # sand payload , cmdval, device_id to cmd handler
        call_handler = handleMSG.cmd_handler()   # run handler



    def start(self):
        self.mqtt.connect(
            MQTT_ADDRESS, 1883, 60
        )
        rc = 0
        while rc == 0:
            rc = self.mqtt.loop_forever()
        return rc