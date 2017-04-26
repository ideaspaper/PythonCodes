# Jawaban Nomor 2 (Kode Proram Utama)
# Daniel Kristianto - 2216204002
# KODE UTAMA PROGRAM GUI PERCEPTRON DENGAN PENERAPAN NILAI WEIGHT DAN BIAS
# YANG TELAH DIDAPATKAN SEBELUMNYA

import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from runningGui import Ui_Form
from tempfile import TemporaryFile


class perceptronGui(Ui_Form):

    #sensorInput = np.zeros((3, 1))

    def __init__(self, dialog):
        Ui_Form.__init__(self)
        self.setupUi(dialog)

        #signal and slot
        self.lineEditSensor1.selectionChanged.connect(
            self.lineEditSensor1.clear)
        self.lineEditSensor2.selectionChanged.connect(
            self.lineEditSensor2.clear)
        self.lineEditSensor3.selectionChanged.connect(
            self.lineEditSensor3.clear)
        self.pushButtonProcess.clicked.connect(self.identificationProcess)

    def identificationProcess(self):
        '''Nilai weight dari hasil learning menggunakan Matlab'''
        weight = np.array([[-4.6813, -8.1879, 3.6102],
                           [-8.3406, 0.0894, -6.0748]])
        '''Nilai bias dari hasil learning menggunakan Matlab'''
        bias = np.array([[2.2380],
                         [4.9967]])

        ones = np.ones((1, 1))

        sensorInput = np.zeros((3, 1))
        sensorInput[(0, 0)] = float(self.lineEditSensor1.text())
        sensorInput[(1, 0)] = float(self.lineEditSensor2.text())
        sensorInput[(2, 0)] = float(self.lineEditSensor3.text())
        n1 = np.matmul(weight, sensorInput)
        n2 = np.matmul(bias, ones)
        n = np.add(n1, n2)

        # hardlim
        for x in np.nditer(n, op_flags=['readwrite']):
            if x >= 0:
                x[...] = 1
            else:
                x[...] = 0

        if n[(0, 0)] == 0 and n[(1, 0)] == 0:
            self.labelGasIdentificationResult.setText("Alkohol")
        elif n[(0, 0)] == 0 and n[(1, 0)] == 1:
            self.labelGasIdentificationResult.setText("Bensin")
        elif n[(0, 0)] == 1 and n[(1, 0)] == 0:
            self.labelGasIdentificationResult.setText("Spiritus")
        else:
            self.labelGasIdentificationResult.setText("---")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = perceptronGui(dialog)
    dialog.show()
    sys.exit(app.exec_())
