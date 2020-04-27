import paho.mqtt.client as mqtt
import log
import mqtt as mq

logger = log.NewLogger(__name__)


def main():
    mqttc = mq.MqClient()
    runClient = mqttc.start()
    if runClient:
        logger.debug('Service Started')
    else:
        logger("Error connecting to MQTT Broker")


if __name__ == '__main__':
    logger.debug('Service is starting')
    main()