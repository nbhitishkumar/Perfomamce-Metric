from influxdb import InfluxDBClient
import log

logger = log.NewLogger(__name__)
IN_DB = 'design'
IN_PORT = 8086
IN_ADDRESS = 'localhost'
IN_USER = 'admin'
IN_PASS = 'admin'


class InfluxClient:
    def __init__(self,payload):
        self.payload = payload
    # create influxdbClient and save payload to db
    
    def influxclient(self):
        client=InfluxDBClient(host = IN_ADDRESS,port = IN_PORT,username = IN_USER,password = IN_PASS,database = IN_DB)
        if client:
            logger.debug("connected to InFluxDb")
        else:
            logger.debug("Cannot connect to InFluxDb")
        print(type(self.payload))
        client.write_points(self.payload)
        client.close()
        return logger.debug("saved")