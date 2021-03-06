# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numberRecognition.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 514)
        MainWindow.setMinimumSize(QtCore.QSize(798, 514))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxTraining = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxTraining.setFont(font)
        self.groupBoxTraining.setObjectName("groupBoxTraining")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxTraining)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxEpoch = QtWidgets.QGroupBox(self.groupBoxTraining)
        self.groupBoxEpoch.setObjectName("groupBoxEpoch")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBoxEpoch)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelEpoch = QtWidgets.QLabel(self.groupBoxEpoch)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.labelEpoch.setFont(font)
        self.labelEpoch.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEpoch.setObjectName("labelEpoch")
        self.verticalLayout_6.addWidget(self.labelEpoch)
        self.verticalLayout.addWidget(self.groupBoxEpoch)
        self.groupBoxError = QtWidgets.QGroupBox(self.groupBoxTraining)
        self.groupBoxError.setObjectName("groupBoxError")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBoxError)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelError = QtWidgets.QLabel(self.groupBoxError)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.labelError.setFont(font)
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)
        self.labelError.setObjectName("labelError")
        self.verticalLayout_7.addWidget(self.labelError)
        self.verticalLayout.addWidget(self.groupBoxError)
        self.pushButtonTrain = QtWidgets.QPushButton(self.groupBoxTraining)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonTrain.setFont(font)
        self.pushButtonTrain.setObjectName("pushButtonTrain")
        self.verticalLayout.addWidget(self.pushButtonTrain)
        self.horizontalLayout.addWidget(self.groupBoxTraining)
        self.verticalLayoutRunning = QtWidgets.QVBoxLayout()
        self.verticalLayoutRunning.setObjectName("verticalLayoutRunning")
        self.horizontalLayoutPixelPredictOutput = QtWidgets.QHBoxLayout()
        self.horizontalLayoutPixelPredictOutput.setObjectName("horizontalLayoutPixelPredictOutput")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBoxPixel = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxPixel.sizePolicy().hasHeightForWidth())
        self.groupBoxPixel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxPixel.setFont(font)
        self.groupBoxPixel.setObjectName("groupBoxPixel")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxPixel)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 0, 4, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 1, 1, 1, 1)
        self.checkBox_25 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_25.setText("")
        self.checkBox_25.setObjectName("checkBox_25")
        self.gridLayout.addWidget(self.checkBox_25, 4, 4, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 1, 2, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_14.setText("")
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout.addWidget(self.checkBox_14, 2, 3, 1, 1)
        self.checkBox_1 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_1.setText("")
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout.addWidget(self.checkBox_1, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_34 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_34.setText("")
        self.checkBox_34.setObjectName("checkBox_34")
        self.gridLayout.addWidget(self.checkBox_34, 6, 3, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_9.setText("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 1, 3, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.checkBox_31 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_31.setText("")
        self.checkBox_31.setObjectName("checkBox_31")
        self.gridLayout.addWidget(self.checkBox_31, 6, 0, 1, 1)
        self.checkBox_27 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_27.setText("")
        self.checkBox_27.setObjectName("checkBox_27")
        self.gridLayout.addWidget(self.checkBox_27, 5, 1, 1, 1)
        self.checkBox_32 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_32.setText("")
        self.checkBox_32.setObjectName("checkBox_32")
        self.gridLayout.addWidget(self.checkBox_32, 6, 1, 1, 1)
        self.checkBox_28 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_28.setText("")
        self.checkBox_28.setObjectName("checkBox_28")
        self.gridLayout.addWidget(self.checkBox_28, 5, 2, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_15.setText("")
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout.addWidget(self.checkBox_15, 2, 4, 1, 1)
        self.checkBox_26 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_26.setText("")
        self.checkBox_26.setObjectName("checkBox_26")
        self.gridLayout.addWidget(self.checkBox_26, 5, 0, 1, 1)
        self.checkBox_35 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_35.setText("")
        self.checkBox_35.setObjectName("checkBox_35")
        self.gridLayout.addWidget(self.checkBox_35, 6, 4, 1, 1)
        self.checkBox_30 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_30.setText("")
        self.checkBox_30.setObjectName("checkBox_30")
        self.gridLayout.addWidget(self.checkBox_30, 5, 4, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 0, 3, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_12.setText("")
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 2, 1, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_10.setText("")
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 1, 4, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_11.setText("")
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 2, 0, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_13.setText("")
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout.addWidget(self.checkBox_13, 2, 2, 1, 1)
        self.checkBox_33 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_33.setText("")
        self.checkBox_33.setObjectName("checkBox_33")
        self.gridLayout.addWidget(self.checkBox_33, 6, 2, 1, 1)
        self.checkBox_19 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_19.setText("")
        self.checkBox_19.setObjectName("checkBox_19")
        self.gridLayout.addWidget(self.checkBox_19, 3, 3, 1, 1)
        self.checkBox_23 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_23.setText("")
        self.checkBox_23.setObjectName("checkBox_23")
        self.gridLayout.addWidget(self.checkBox_23, 4, 2, 1, 1)
        self.checkBox_29 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_29.setText("")
        self.checkBox_29.setObjectName("checkBox_29")
        self.gridLayout.addWidget(self.checkBox_29, 5, 3, 1, 1)
        self.checkBox_21 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_21.setText("")
        self.checkBox_21.setObjectName("checkBox_21")
        self.gridLayout.addWidget(self.checkBox_21, 4, 0, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_16.setText("")
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout.addWidget(self.checkBox_16, 3, 0, 1, 1)
        self.checkBox_22 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_22.setText("")
        self.checkBox_22.setObjectName("checkBox_22")
        self.gridLayout.addWidget(self.checkBox_22, 4, 1, 1, 1)
        self.checkBox_20 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_20.setText("")
        self.checkBox_20.setObjectName("checkBox_20")
        self.gridLayout.addWidget(self.checkBox_20, 3, 4, 1, 1)
        self.checkBox_18 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_18.setText("")
        self.checkBox_18.setObjectName("checkBox_18")
        self.gridLayout.addWidget(self.checkBox_18, 3, 2, 1, 1)
        self.checkBox_17 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_17.setText("")
        self.checkBox_17.setObjectName("checkBox_17")
        self.gridLayout.addWidget(self.checkBox_17, 3, 1, 1, 1)
        self.checkBox_24 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_24.setText("")
        self.checkBox_24.setObjectName("checkBox_24")
        self.gridLayout.addWidget(self.checkBox_24, 4, 3, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBoxPixel)
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 1, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBoxPixel)
        self.pushButtonPredict = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPredict.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPredict.sizePolicy().hasHeightForWidth())
        self.pushButtonPredict.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonPredict.setFont(font)
        self.pushButtonPredict.setObjectName("pushButtonPredict")
        self.verticalLayout_5.addWidget(self.pushButtonPredict)
        self.horizontalLayoutPixelPredictOutput.addLayout(self.verticalLayout_5)
        self.groupBoxOutput = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxOutput.sizePolicy().hasHeightForWidth())
        self.groupBoxOutput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxOutput.setFont(font)
        self.groupBoxOutput.setObjectName("groupBoxOutput")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBoxOutput)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelOutput = QtWidgets.QLabel(self.groupBoxOutput)
        font = QtGui.QFont()
        font.setPointSize(120)
        font.setBold(False)
        font.setWeight(50)
        self.labelOutput.setFont(font)
        self.labelOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOutput.setObjectName("labelOutput")
        self.horizontalLayout_6.addWidget(self.labelOutput)
        self.horizontalLayoutPixelPredictOutput.addWidget(self.groupBoxOutput)
        self.verticalLayoutRunning.addLayout(self.horizontalLayoutPixelPredictOutput)
        self.groupBoxLoadTrainingSet = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxLoadTrainingSet.sizePolicy().hasHeightForWidth())
        self.groupBoxLoadTrainingSet.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxLoadTrainingSet.setFont(font)
        self.groupBoxLoadTrainingSet.setObjectName("groupBoxLoadTrainingSet")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxLoadTrainingSet)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout04 = QtWidgets.QHBoxLayout()
        self.horizontalLayout04.setObjectName("horizontalLayout04")
        self.pushButtonLoad0 = QtWidgets.QPushButton(self.groupBoxLoadTrainingSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonLoad0.setFont(font)
        self.pushButtonLoad0.setObjectName("pushButtonLoad0")
        self.horizontalLayout04.addWidget(self.pushButtonLoad0)
        self.pushButtonLoad1 = QtWidgets.QPushButton(self.groupBoxLoadTrainingSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonLoad1.setFont(font)
        self.pushButtonLoad1.setObjectName("pushButtonLoad1")
        self.horizontalLayout04.addWidget(self.pushButtonLoad1)
        self.pushButtonLoad2 = QtWidgets.QPushButton(self.groupBoxLoadTrainingSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonLoad2.setFont(font)
        self.pushButtonLoad2.setObjectName("pushButtonLoad2")
        self.horizontalLayout04.addWidget(self.pushButtonLoad2)
        self.pushButtonLoad3 = QtWidgets.QPushButton(self.groupBoxLoadTrainingSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonLoad3.setFont(font)
        self.pushButtonLoad3.setObjectName("pushButtonLoad3")
        self.horizontalLayout04.addWidget(self.pushButtonLoad3)
        self.pushButtonLoad4 = QtWidgets.QPushButton(self.groupBoxLoadTrainingSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonLoad4.setFont(font)
        self.pushButtonLoad4.setObjectName("pushButtonLoad4")
        self.horizontalLayout04.addWidget(self.pushButtonLoad4)
        self.verticalLayout_2.addLayout(self.horizontalLayout04)
        self.horizontalLayout59 = QtWidgets.QHBoxLayout()
        self.horizontalLayout59.setObjectName("horizontalLayout59")
        self.pushButtonLoad5 = QtWidgets.QPushButton(self.groupBoxLoadTrainingSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonLoad5.setFont(font)
        self.pushButtonLoad5.setObjectName("pushButtonLoad5")
        self.horizontalLayout59.addWidget(self.pushButtonLoad5)
        self.pushButtonLoad6 = QtWidgets.QPushButton(self.groupBoxLoadTrainingSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonLoad6.setFont(font)
        self.pushButtonLoad6.setObjectName("pushButtonLoad6")
        self.horizontalLayout59.addWidget(self.pushButtonLoad6)
        self.pushButtonLoad7 = QtWidgets.QPushButton(self.groupBoxLoadTrainingSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonLoad7.setFont(font)
        self.pushButtonLoad7.setObjectName("pushButtonLoad7")
        self.horizontalLayout59.addWidget(self.pushButtonLoad7)
        self.pushButtonLoad8 = QtWidgets.QPushButton(self.groupBoxLoadTrainingSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonLoad8.setFont(font)
        self.pushButtonLoad8.setObjectName("pushButtonLoad8")
        self.horizontalLayout59.addWidget(self.pushButtonLoad8)
        self.pushButtonLoad9 = QtWidgets.QPushButton(self.groupBoxLoadTrainingSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonLoad9.setFont(font)
        self.pushButtonLoad9.setObjectName("pushButtonLoad9")
        self.horizontalLayout59.addWidget(self.pushButtonLoad9)
        self.verticalLayout_2.addLayout(self.horizontalLayout59)
        self.verticalLayoutRunning.addWidget(self.groupBoxLoadTrainingSet)
        self.horizontalLayout.addLayout(self.verticalLayoutRunning)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Number Prediction"))
        self.groupBoxTraining.setTitle(_translate("MainWindow", "Training"))
        self.groupBoxEpoch.setTitle(_translate("MainWindow", "Epoch"))
        self.labelEpoch.setText(_translate("MainWindow", "-"))
        self.groupBoxError.setTitle(_translate("MainWindow", "Error"))
        self.labelError.setText(_translate("MainWindow", "-"))
        self.pushButtonTrain.setText(_translate("MainWindow", "Train"))
        self.groupBoxPixel.setTitle(_translate("MainWindow", "Pixel"))
        self.pushButtonPredict.setText(_translate("MainWindow", "Predict"))
        self.groupBoxOutput.setTitle(_translate("MainWindow", "Output"))
        self.labelOutput.setText(_translate("MainWindow", "-"))
        self.groupBoxLoadTrainingSet.setTitle(_translate("MainWindow", "Load Training Set"))
        self.pushButtonLoad0.setText(_translate("MainWindow", "Load 0"))
        self.pushButtonLoad1.setText(_translate("MainWindow", "Load 1"))
        self.pushButtonLoad2.setText(_translate("MainWindow", "Load 2"))
        self.pushButtonLoad3.setText(_translate("MainWindow", "Load 3"))
        self.pushButtonLoad4.setText(_translate("MainWindow", "Load 4"))
        self.pushButtonLoad5.setText(_translate("MainWindow", "Load 5"))
        self.pushButtonLoad6.setText(_translate("MainWindow", "Load 6"))
        self.pushButtonLoad7.setText(_translate("MainWindow", "Load 7"))
        self.pushButtonLoad8.setText(_translate("MainWindow", "Load 8"))
        self.pushButtonLoad9.setText(_translate("MainWindow", "Load 9"))
        self.actionClose.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

