import psutil
import os
import paho.mqtt.client as mqtt
import json

res={}
topic='result/device/'
Device_name="Dell_Laptop"

while True:
    cpu = psutil.cpu_percent(interval=1, percpu=False)
    mem = psutil.virtual_memory()
    res["cpu_usages"]=cpu
    res["memory_usages"]=mem.percent
    client = mqtt.Client(Device_name)
    client.connect("127.0.0.1")
    client.publish(topic+Device_name+"/performance", str(json.dumps(res)))
    client.disconnect()