# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mqttDemo.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(721, 461)
        Form.setMinimumSize(QtCore.QSize(721, 461))
        Form.setMaximumSize(QtCore.QSize(721, 461))
        self.groupBoxLCDMessage = QtWidgets.QGroupBox(Form)
        self.groupBoxLCDMessage.setGeometry(QtCore.QRect(10, 370, 351, 81))
        self.groupBoxLCDMessage.setObjectName("groupBoxLCDMessage")
        self.lineEditLCDMessage = QtWidgets.QLineEdit(self.groupBoxLCDMessage)
        self.lineEditLCDMessage.setGeometry(QtCore.QRect(10, 20, 331, 20))
        self.lineEditLCDMessage.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditLCDMessage.setMaxLength(16)
        self.lineEditLCDMessage.setObjectName("lineEditLCDMessage")
        self.pushButtonSendLCD = QtWidgets.QPushButton(self.groupBoxLCDMessage)
        self.pushButtonSendLCD.setGeometry(QtCore.QRect(10, 50, 331, 23))
        self.pushButtonSendLCD.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButtonSendLCD.setObjectName("pushButtonSendLCD")
        self.groupBoxRelay = QtWidgets.QGroupBox(Form)
        self.groupBoxRelay.setGeometry(QtCore.QRect(370, 370, 341, 80))
        self.groupBoxRelay.setObjectName("groupBoxRelay")
        self.pushButtonRelayOn = QtWidgets.QPushButton(self.groupBoxRelay)
        self.pushButtonRelayOn.setGeometry(QtCore.QRect(10, 20, 321, 23))
        self.pushButtonRelayOn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButtonRelayOn.setObjectName("pushButtonRelayOn")
        self.pushButtonRelayOff = QtWidgets.QPushButton(self.groupBoxRelay)
        self.pushButtonRelayOff.setGeometry(QtCore.QRect(10, 50, 321, 23))
        self.pushButtonRelayOff.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButtonRelayOff.setObjectName("pushButtonRelayOff")
        self.groupBoxButtonStatus = QtWidgets.QGroupBox(Form)
        self.groupBoxButtonStatus.setGeometry(QtCore.QRect(370, 10, 341, 171))
        self.groupBoxButtonStatus.setObjectName("groupBoxButtonStatus")
        self.labelButtonStatus = QtWidgets.QLabel(self.groupBoxButtonStatus)
        self.labelButtonStatus.setGeometry(QtCore.QRect(10, 20, 321, 141))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(40)
        self.labelButtonStatus.setFont(font)
        self.labelButtonStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelButtonStatus.setObjectName("labelButtonStatus")
        self.groupBoxPIRStatus = QtWidgets.QGroupBox(Form)
        self.groupBoxPIRStatus.setGeometry(QtCore.QRect(370, 190, 341, 171))
        self.groupBoxPIRStatus.setObjectName("groupBoxPIRStatus")
        self.labelPIRStatus = QtWidgets.QLabel(self.groupBoxPIRStatus)
        self.labelPIRStatus.setGeometry(QtCore.QRect(10, 20, 321, 141))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(40)
        self.labelPIRStatus.setFont(font)
        self.labelPIRStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPIRStatus.setObjectName("labelPIRStatus")
        self.groupBoxBrokerSetting = QtWidgets.QGroupBox(Form)
        self.groupBoxBrokerSetting.setGeometry(QtCore.QRect(10, 10, 351, 351))
        self.groupBoxBrokerSetting.setObjectName("groupBoxBrokerSetting")
        self.lineEditURLBroker = QtWidgets.QLineEdit(self.groupBoxBrokerSetting)
        self.lineEditURLBroker.setGeometry(QtCore.QRect(130, 20, 211, 20))
        self.lineEditURLBroker.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditURLBroker.setObjectName("lineEditURLBroker")
        self.lineEditPortBroker = QtWidgets.QLineEdit(self.groupBoxBrokerSetting)
        self.lineEditPortBroker.setGeometry(QtCore.QRect(130, 50, 211, 20))
        self.lineEditPortBroker.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditPortBroker.setObjectName("lineEditPortBroker")
        self.lineEditSubscribeTopicBroker = QtWidgets.QLineEdit(self.groupBoxBrokerSetting)
        self.lineEditSubscribeTopicBroker.setGeometry(QtCore.QRect(130, 260, 211, 20))
        self.lineEditSubscribeTopicBroker.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditSubscribeTopicBroker.setObjectName("lineEditSubscribeTopicBroker")
        self.lineEditAPIKeyBroker = QtWidgets.QLineEdit(self.groupBoxBrokerSetting)
        self.lineEditAPIKeyBroker.setGeometry(QtCore.QRect(130, 170, 211, 20))
        self.lineEditAPIKeyBroker.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditAPIKeyBroker.setObjectName("lineEditAPIKeyBroker")
        self.lineEditAuthenticationTokenBroker = QtWidgets.QLineEdit(self.groupBoxBrokerSetting)
        self.lineEditAuthenticationTokenBroker.setGeometry(QtCore.QRect(130, 200, 211, 20))
        self.lineEditAuthenticationTokenBroker.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditAuthenticationTokenBroker.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditAuthenticationTokenBroker.setObjectName("lineEditAuthenticationTokenBroker")
        self.pushButtonConnectBroker = QtWidgets.QPushButton(self.groupBoxBrokerSetting)
        self.pushButtonConnectBroker.setGeometry(QtCore.QRect(10, 290, 331, 23))
        self.pushButtonConnectBroker.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButtonConnectBroker.setObjectName("pushButtonConnectBroker")
        self.labelStatusBroker = QtWidgets.QLabel(self.groupBoxBrokerSetting)
        self.labelStatusBroker.setGeometry(QtCore.QRect(10, 320, 171, 16))
        self.labelStatusBroker.setObjectName("labelStatusBroker")
        self.lineEditOrganizationBroker = QtWidgets.QLineEdit(self.groupBoxBrokerSetting)
        self.lineEditOrganizationBroker.setGeometry(QtCore.QRect(130, 80, 211, 20))
        self.lineEditOrganizationBroker.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditOrganizationBroker.setObjectName("lineEditOrganizationBroker")
        self.lineEditDeviceTypeBroker = QtWidgets.QLineEdit(self.groupBoxBrokerSetting)
        self.lineEditDeviceTypeBroker.setGeometry(QtCore.QRect(130, 110, 211, 20))
        self.lineEditDeviceTypeBroker.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditDeviceTypeBroker.setObjectName("lineEditDeviceTypeBroker")
        self.lineEditDeviceIDBroker = QtWidgets.QLineEdit(self.groupBoxBrokerSetting)
        self.lineEditDeviceIDBroker.setGeometry(QtCore.QRect(130, 140, 211, 20))
        self.lineEditDeviceIDBroker.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditDeviceIDBroker.setObjectName("lineEditDeviceIDBroker")
        self.lineEditPublishTopicBroker = QtWidgets.QLineEdit(self.groupBoxBrokerSetting)
        self.lineEditPublishTopicBroker.setGeometry(QtCore.QRect(130, 230, 211, 20))
        self.lineEditPublishTopicBroker.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditPublishTopicBroker.setObjectName("lineEditPublishTopicBroker")
        self.labelBroker = QtWidgets.QLabel(self.groupBoxBrokerSetting)
        self.labelBroker.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.labelBroker.setObjectName("labelBroker")
        self.labelPort = QtWidgets.QLabel(self.groupBoxBrokerSetting)
        self.labelPort.setGeometry(QtCore.QRect(10, 50, 111, 16))
        self.labelPort.setObjectName("labelPort")
        self.labelPublishTopic = QtWidgets.QLabel(self.groupBoxBrokerSetting)
        self.labelPublishTopic.setGeometry(QtCore.QRect(10, 230, 111, 16))
        self.labelPublishTopic.setObjectName("labelPublishTopic")
        self.labelOrganization = QtWidgets.QLabel(self.groupBoxBrokerSetting)
        self.labelOrganization.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.labelOrganization.setObjectName("labelOrganization")
        self.labelDeviceType = QtWidgets.QLabel(self.groupBoxBrokerSetting)
        self.labelDeviceType.setGeometry(QtCore.QRect(10, 110, 111, 16))
        self.labelDeviceType.setObjectName("labelDeviceType")
        self.labelDeviceID = QtWidgets.QLabel(self.groupBoxBrokerSetting)
        self.labelDeviceID.setGeometry(QtCore.QRect(10, 140, 111, 16))
        self.labelDeviceID.setObjectName("labelDeviceID")
        self.labelAPIKey = QtWidgets.QLabel(self.groupBoxBrokerSetting)
        self.labelAPIKey.setGeometry(QtCore.QRect(10, 170, 111, 16))
        self.labelAPIKey.setObjectName("labelAPIKey")
        self.labelAuthenticationToken = QtWidgets.QLabel(self.groupBoxBrokerSetting)
        self.labelAuthenticationToken.setGeometry(QtCore.QRect(10, 200, 111, 16))
        self.labelAuthenticationToken.setObjectName("labelAuthenticationToken")
        self.labelSubscribeTopic = QtWidgets.QLabel(self.groupBoxBrokerSetting)
        self.labelSubscribeTopic.setGeometry(QtCore.QRect(10, 260, 111, 16))
        self.labelSubscribeTopic.setObjectName("labelSubscribeTopic")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MQTT Demo"))
        self.groupBoxLCDMessage.setTitle(_translate("Form", "LCD Message"))
        self.lineEditLCDMessage.setText(_translate("Form", "Message..."))
        self.pushButtonSendLCD.setText(_translate("Form", "Send"))
        self.groupBoxRelay.setTitle(_translate("Form", "Relay"))
        self.pushButtonRelayOn.setText(_translate("Form", "ON"))
        self.pushButtonRelayOff.setText(_translate("Form", "OFF"))
        self.groupBoxButtonStatus.setTitle(_translate("Form", "Button Status"))
        self.labelButtonStatus.setText(_translate("Form", "---"))
        self.groupBoxPIRStatus.setTitle(_translate("Form", "PIR Status"))
        self.labelPIRStatus.setText(_translate("Form", "---"))
        self.groupBoxBrokerSetting.setTitle(_translate("Form", "Broker Setting"))
        self.lineEditURLBroker.setText(_translate("Form", "messaging.internetofthings.ibmcloud.com"))
        self.lineEditPortBroker.setText(_translate("Form", "1883"))
        self.lineEditSubscribeTopicBroker.setText(_translate("Form", "status"))
        self.lineEditAPIKeyBroker.setText(_translate("Form", "a-5ehvj5-n7pwbbpsk2"))
        self.lineEditAuthenticationTokenBroker.setText(_translate("Form", "gyN9xpnZ?fs1U0c*wy"))
        self.pushButtonConnectBroker.setText(_translate("Form", "Connect"))
        self.labelStatusBroker.setText(_translate("Form", "Status: -"))
        self.lineEditOrganizationBroker.setText(_translate("Form", "5ehvj5"))
        self.lineEditDeviceTypeBroker.setText(_translate("Form", "IoTDevice"))
        self.lineEditDeviceIDBroker.setText(_translate("Form", "device-01"))
        self.lineEditPublishTopicBroker.setText(_translate("Form", "status"))
        self.labelBroker.setText(_translate("Form", "Broker:"))
        self.labelPort.setText(_translate("Form", "Port:"))
        self.labelPublishTopic.setText(_translate("Form", "Publish topic:"))
        self.labelOrganization.setText(_translate("Form", "Organization:"))
        self.labelDeviceType.setText(_translate("Form", "Device type:"))
        self.labelDeviceID.setText(_translate("Form", "Device ID:"))
        self.labelAPIKey.setText(_translate("Form", "API Key:"))
        self.labelAuthenticationToken.setText(_translate("Form", "Authentication token:"))
        self.labelSubscribeTopic.setText(_translate("Form", "Subscribe topic:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

