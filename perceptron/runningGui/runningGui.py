#Jawaban Nomor 2 (GUI)
#Daniel Kristianto - 2216204002
#KODE FORM PROGRAM GUI PERCEPTRON DENGAN PENERAPAN NILAI WEIGHT DAN BIAS YANG TELAH DIDAPATKAN SEBELUMNYA

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runningGui.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(561, 321)
        Form.setMinimumSize(QtCore.QSize(561, 321))
        Form.setMaximumSize(QtCore.QSize(561, 321))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(320, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelGasIdentificationResult = QtWidgets.QLabel(Form)
        self.labelGasIdentificationResult.setGeometry(QtCore.QRect(320, 60, 231, 211))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelGasIdentificationResult.setFont(font)
        self.labelGasIdentificationResult.setFrameShape(QtWidgets.QFrame.Box)
        self.labelGasIdentificationResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelGasIdentificationResult.setObjectName("labelGasIdentificationResult")
        self.lineEditSensor1 = QtWidgets.QLineEdit(Form)
        self.lineEditSensor1.setGeometry(QtCore.QRect(10, 60, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lineEditSensor1.setFont(font)
        self.lineEditSensor1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditSensor1.setObjectName("lineEditSensor1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEditSensor2 = QtWidgets.QLineEdit(Form)
        self.lineEditSensor2.setGeometry(QtCore.QRect(10, 140, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lineEditSensor2.setFont(font)
        self.lineEditSensor2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditSensor2.setObjectName("lineEditSensor2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEditSensor3 = QtWidgets.QLineEdit(Form)
        self.lineEditSensor3.setGeometry(QtCore.QRect(10, 220, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lineEditSensor3.setFont(font)
        self.lineEditSensor3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditSensor3.setObjectName("lineEditSensor3")
        self.pushButtonProcess = QtWidgets.QPushButton(Form)
        self.pushButtonProcess.setGeometry(QtCore.QRect(200, 140, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButtonProcess.setFont(font)
        self.pushButtonProcess.setObjectName("pushButtonProcess")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Perceptron running"))
        self.label.setText(_translate("Form", "Gas Identification"))
        self.labelGasIdentificationResult.setText(_translate("Form", "---"))
        self.lineEditSensor1.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "Input Sensor 1"))
        self.lineEditSensor2.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "Input Sensor 2"))
        self.label_5.setText(_translate("Form", "Input Sensor 3"))
        self.lineEditSensor3.setText(_translate("Form", "0"))
        self.pushButtonProcess.setText(_translate("Form", "Process"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
