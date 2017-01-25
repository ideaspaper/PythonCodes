import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mqttDemo import Ui_Form
import paho.mqtt.client as mqtt
import json

class mqttDemoGuiProgram(Ui_Form):
	#misc variables
	connectionState = 0
	connectingState = 0
	
	#broker credentials
	broker = 0
	port = 0
	organization = 0
	deviceType = 0
	deviceID = 0
	APIKey = 0
	authenticationToken = 0
	publishTopic = 0
	subscribeTopic = 0
	client = 0

	def __init__(self, dialog):
		Ui_Form.__init__(self)
		self.setupUi(dialog)
		
		#signal and slot
		self.lineEditURLBroker.selectionChanged.connect(self.lineEditURLBroker.clear)									#broker setting group box
		self.lineEditPortBroker.selectionChanged.connect(self.lineEditPortBroker.clear)									#broker setting group box
		self.lineEditOrganizationBroker.selectionChanged.connect(self.lineEditOrganizationBroker.clear)					#broker setting group box
		self.lineEditDeviceTypeBroker.selectionChanged.connect(self.lineEditDeviceTypeBroker.clear)						#broker setting group box
		self.lineEditDeviceIDBroker.selectionChanged.connect(self.lineEditDeviceIDBroker.clear)							#broker setting group box
		self.lineEditPublishTopicBroker.selectionChanged.connect(self.lineEditPublishTopicBroker.clear)					#broker setting group box
		self.lineEditSubscribeTopicBroker.selectionChanged.connect(self.lineEditSubscribeTopicBroker.clear)				#broker setting group box
		self.lineEditAPIKeyBroker.selectionChanged.connect(self.lineEditAPIKeyBroker.clear)								#broker setting group box
		self.lineEditAuthenticationTokenBroker.selectionChanged.connect(self.lineEditAuthenticationTokenBroker.clear)	#broker setting group box
		self.pushButtonConnectBroker.clicked.connect(self.connectBroker)												#broker setting group box
		self.lineEditLCDMessage.selectionChanged.connect(self.lineEditLCDMessage.clear)									#lcd message group box
		self.pushButtonSendLCD.clicked.connect(self.publishMessage)
		self.pushButtonRelayOn.clicked.connect(self.publishRelayOn)
		self.pushButtonRelayOff.clicked.connect(self.publishRelayOff)
		#signal and slot
		
	def connectBroker(self):
		#put codes here
		if self.connectionState == 0 and self.connectingState == 0:
			self.connectingState = 1
			self.pushButtonConnectBroker.setText("Disconnect")
			self.labelStatusBroker.setText("Status: Connecting...")
			self.broker = self.lineEditURLBroker.text()
			self.port = self.lineEditPortBroker.text()
			self.organization = self.lineEditOrganizationBroker.text()
			self.deviceType = self.lineEditDeviceTypeBroker.text()
			self.deviceID = self.lineEditDeviceIDBroker.text()
			self.APIKey = self.lineEditAPIKeyBroker.text()
			self.authenticationToken = self.lineEditAuthenticationTokenBroker.text()
			self.publishTopic = self.lineEditPublishTopicBroker.text()
			self.subscribeTopic = self.lineEditSubscribeTopicBroker.text()
				
			self.broker = self.organization + "." + self.broker
			self.publishTopic = "iot-2/type/" + self.deviceType + "/id/" + self.deviceID + "/cmd/" + self.publishTopic + "/fmt/json"
			self.subscribeTopic = "iot-2/type/" + self.deviceType + "/id/" + self.deviceID + "/evt/" + self.subscribeTopic + "/fmt/json"
			clientID = "a:" + self.organization + ":" + self.APIKey
			
			self.client = mqtt.Client(client_id = clientID)
			self.client.on_connect    = self.on_connect					#set the callback function for on_connect event
			self.client.on_message    = self.on_message					#set the callback function for on_message event
			self.client.on_disconnect = self.on_disconnect				#set the callback function for on_disconnect event
			self.client.username_pw_set(self.APIKey, password = self.authenticationToken)
			self.client.connect(host = self.broker, port = int(self.port), keepalive = 60)
			self.client.loop_start()
		elif self.connectionState == 1 and self.connectingState == 0:
			self.connectingState = 1
			self.pushButtonConnectBroker.setText("Connect")
			self.labelStatusBroker.setText("Status: Disconnecting...")
			self.client.disconnect()
			self.client.loop_stop()
	
	def on_connect(self, client, userdata, flags, rc):
		self.connectionState = 1
		self.connectingState = 0
		self.labelStatusBroker.setText("Status: Connected")
		#print("Connected with result code " + str(rc))
		self.client.subscribe(self.subscribeTopic)
		
	def on_message(self, client, userdata, msg):
		data = str(msg.payload)
		mylist = data.split(" ")
		if mylist[0] == 'b\'{"d":{"PIR':
			if mylist[2].split("}")[0] == "0":
				self.labelPIRStatus.setText("LOW")
			elif mylist[2].split("}")[0] == "1":
				self.labelPIRStatus.setText("HIGH")
		elif mylist[0] == 'b\'{"d":{"Push':
			if mylist[3].split("}")[0] == "0":
				self.labelButtonStatus.setText("LOW")
			elif mylist[3].split("}")[0] == "1":
				self.labelButtonStatus.setText("HIGH")
		
	def on_disconnect(self, client, userdata, rc):
		self.connectionState = 0
		self.connectingState = 0
		self.labelStatusBroker.setText("Status: Disconnected")
		self.labelPIRStatus.setText("---")
		self.labelButtonStatus.setText("---")
		#print("Disconnect with result code " + str(rc))
	
	def publishMessage(self):
		msg = json.JSONEncoder().encode({"d":{"lcd":self.lineEditLCDMessage.text()}})
		self.client.publish(self.publishTopic, payload=msg, qos=0, retain=False)
		
	def publishRelayOn(self):
		msg = json.JSONEncoder().encode({"d":{"relay":"1"}})
		self.client.publish(self.publishTopic, payload=msg, qos=0, retain=False)
	
	def publishRelayOff(self):
		msg = json.JSONEncoder().encode({"d":{"relay":"0"}})
		self.client.publish(self.publishTopic, payload=msg, qos=0, retain=False)
		
	def myDebug(self):
		broker = self.lineEditURLBroker.text()
		port = self.lineEditPortBroker.text()
		publishTopic = self.lineEditPublishTopicBroker.text()
		subscribeTopic = self.lineEditSubscribeTopicBroker.text()
		apiKey = self.lineEditAPIKeyBroker.text()
		authenticationToken = self.lineEditAuthenticationTokenBroker.text()
		print(broker)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()
	prog = mqttDemoGuiProgram(dialog)
	dialog.show()
	sys.exit(app.exec_())