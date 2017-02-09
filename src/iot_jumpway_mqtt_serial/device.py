# *****************************************************************************
# Copyright (c) 2016 TechBubble Technologies and other Contributors.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html 
#
# Contributors:
#   Adam Milton-Barker - TechBubble Technologies Limited
# *****************************************************************************

import os
import sys
import time
import json
import serial
import base64

from techbubbleiotjumpwaymqtt.device import JumpWayPythonMQTTDeviceConnection

class MQTTSerialClient():
    
    def __init__(self, configs):
		
		self._configs = configs

		if self._configs['SystemLocation'] is None:
			raise ConfigurationException("SystemLocation property is required")
		elif self._configs['SystemZone'] is None:
			raise ConfigurationException("SystemZone property is required")
		elif self._configs['SystemDeviceID'] is None:
			raise ConfigurationException("SystemDeviceID property is required")
		elif self._configs['SystemDeviceName'] is None:
			raise ConfigurationException("SystemDeviceName property is required")
		elif self._configs['SystemDeviceCom'] is None:
			raise ConfigurationException("SystemDeviceCom property is required")
		elif self._configs['MQTTUsername'] is None:
			raise ConfigurationException("MQTTUsername property is required")
		elif self._configs['MQTTPassword'] is None:
			raise ConfigurationException("MQTTPassword property is required")

		self.JumpWayMQTTClient = ""
		self.startMQTT()

		self.serialClient = serial.Serial(self._configs['SystemDeviceCom'], 9600)  
		time.sleep(5)
		print("CONNECTED TO COM PORT: "+self._configs['SystemDeviceCom'])
        
    def deviceCommandsCallback(self,topic,payload):
		
		print("Received command data: %s" % (payload))

		self.serialClient.write(payload+'\n')
		self.serialClient.flush()
            
    def startMQTT(self):
		
		try:
			
			self.JumpWayMQTTClient = JumpWayPythonMQTTDeviceConnection({
				"locationID": self._configs['SystemLocation'],  
				"zoneID": self._configs['SystemZone'], 
				"deviceId": self._configs['SystemDeviceID'], 
				"deviceName": self._configs['SystemDeviceName'], 
				"username": self._configs['MQTTUsername'], 
				"password": self._configs['MQTTPassword']
			})
			
			self.JumpWayMQTTClient.connectToDevice()
			self.JumpWayMQTTClient.subscribeToDeviceChannel("Commands")
			self.JumpWayMQTTClient.deviceCommandsCallback = self.deviceCommandsCallback
			
		except Exception as e:
			print(str(e))
			sys.exit()
            
    def begin(self):
		
		print("SYSTEM INITIATED")

		while True:

			receivedData = 	self.serialClient.readline()

			print(receivedData) 
			
			if(receivedData):

				self.JumpWayMQTTClient.publishToDeviceChannel(
					"Sensors",
					receivedData
				)

			time.sleep(5)