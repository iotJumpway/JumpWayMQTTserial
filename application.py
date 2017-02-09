
import json
import time
from iot_jumpway_mqtt_serial.device import MQTTSerialClient

class IoTJumpWayMQTTSerialDemo():
    
    def __init__(self):
        
        self.configs = {}
        
        with open('config.json') as configs:
            self.configs = json.loads(configs.read())

	    self.MQTTSerialClient = MQTTSerialClient({
            "SystemLocation": self.configs["IoTJumpWaySettings"]["SystemLocation"],
            "SystemZone": self.configs["IoTJumpWaySettings"]["SystemZone"],
            "SystemDeviceID": self.configs["IoTJumpWaySettings"]["SystemDeviceID"],
            "SystemDeviceName": self.configs["IoTJumpWaySettings"]["SystemDeviceName"],
            "SystemDeviceCom": self.configs["IoTJumpWaySettings"]["SystemDeviceCom"],
            "MQTTUsername": self.configs["IoTJumpWayMQTTSettings"]["MQTTUsername"],
            "MQTTPassword": self.configs["IoTJumpWayMQTTSettings"]["MQTTPassword"]
        })
        
        self.MQTTSerialClient.begin()

IoTJumpWayMQTTSerialDemo = IoTJumpWayMQTTSerialDemo()