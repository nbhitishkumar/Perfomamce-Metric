import log
import json
from argparse import Namespace
import influx
from influxdb import InfluxDBClient

logger = log.NewLogger(__name__)



class CMDHandler:
    def __init__(self, payload, device_name):
        self.payload = payload
        self.device_name = device_name

    # Cmd handler that auto call cmdVal function for conv. in INLINE Protocol
    def cmd_handler(self):
        result=process(self.payload, self.device_name)
        if result:
            save_output=influx.InfluxClient(result)
            save_output.influxclient()
            if save_output:
                logger.debug("Output with device_id %r has been saved",self.device_name)
            else:
                logger.debug("Error in connection to InfluDb")

def process(payload, device_name):
    result =[{}]
    tags = {}
    fields = {}
    res = json.loads(payload)
    fields=res
    result[0]["measurement"]="performance"
    result[0]["tags"]={"device_name":device_name}
    result[0]["fields"]=fields
    print(result)
    return result