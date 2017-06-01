import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from numberRecognition import Ui_MainWindow
import numpy as np
import time

class numRec(Ui_MainWindow):
	
	checkBoxList = []
	numberPixel0 = [0, 1, 1, 1, 0,
					1, 0, 0, 0, 1,
					1, 0, 0, 0, 1,
					1, 0, 0, 0, 1,
					1, 0, 0, 0, 1,
					1, 0, 0, 0, 1,
					0, 1, 1, 1, 0]
	
	numberPixel1 = [0, 0, 1, 0, 0,
					0, 1, 1, 0, 0,
					0, 0, 1, 0, 0,
					0, 0, 1, 0, 0,
					0, 0, 1, 0, 0,
					0, 0, 1, 0, 0,
					0, 1, 1, 1, 0]
	
	numberPixel2 = [0, 1, 1, 1, 0,
					1, 0, 0, 0, 1,
					0, 0, 0, 0, 1,
					0, 0, 0, 1, 0,
					0, 0, 1, 0, 0,
					0, 1, 0, 0, 0,
					1, 1, 1, 1, 1]
	
	numberPixel3 = [1, 1, 1, 1, 1,
					0, 0, 0, 1, 0,
					0, 0, 1, 0, 0,
					0, 0, 0, 1, 0,
					0, 0, 0, 0, 1,
					1, 0, 0, 0, 1,
					0, 1, 1, 1, 0]
	
	numberPixel4 = [0, 0, 0, 1, 0,
					0, 0, 1, 1, 0,
					0, 1, 0, 1, 0,
					1, 0, 0, 1, 0,
					1, 1, 1, 1, 1,
					0, 0, 0, 1, 0,
					0, 0, 0, 1, 0]
	
	numberPixel5 = [1, 1, 1, 1, 1,
					1, 0, 0, 0, 0,
					1, 1, 1, 1, 0,
					0, 0, 0, 0, 1,
					0, 0, 0, 0, 1,
					1, 0, 0, 0, 1,
					0, 1, 1, 1, 0]
	
	numberPixel6 = [0, 0, 1, 1, 0,
					0, 1, 0, 0, 0,
					1, 0, 0, 0, 0,
					1, 1, 1, 1, 0,
					1, 0, 0, 0, 1,
					1, 0, 0, 0, 1,
					0, 1, 1, 1, 0]
	
	numberPixel7 = [1, 1, 1, 1, 1,
					0, 0, 0, 0, 1,
					0, 0, 0, 1, 0,
					0, 0, 1, 0, 0,
					0, 1, 0, 0, 0,
					0, 1, 0, 0, 0,
					0, 1, 0, 0, 0]
	
	numberPixel8 = [0, 1, 1, 1, 0,
					1, 0, 0, 0, 1,
					1, 0, 0, 0, 1,
					0, 1, 1, 1, 0,
					1, 0, 0, 0, 1,
					1, 0, 0, 0, 1,
					0, 1, 1, 1, 0]
	
	numberPixel9 = [0, 1, 1, 1, 0,
					1, 0, 0, 0, 1,
					1, 0, 0, 0, 1,
					0, 1, 1, 1, 1,
					0, 0, 0, 0, 1,
					0, 0, 0, 1, 0,
					0, 1, 1, 0, 0]
	
	numberToLoad = np.array([numberPixel0, numberPixel1, numberPixel2, numberPixel3, numberPixel4, numberPixel5, numberPixel6, numberPixel7, numberPixel8, numberPixel9]).T
	weightRes1 = 0; biasRes1 = 0; weightRes2 = 0; biasRes2 = 0;
	
	def __init__(self, dialog):
		Ui_MainWindow.__init__(self)
		self.setupUi(dialog)
		
		self.checkBoxList.append(self.checkBox_1); self.checkBoxList.append(self.checkBox_2); self.checkBoxList.append(self.checkBox_3); self.checkBoxList.append(self.checkBox_4); self.checkBoxList.append(self.checkBox_5);
		self.checkBoxList.append(self.checkBox_6); self.checkBoxList.append(self.checkBox_7); self.checkBoxList.append(self.checkBox_8); self.checkBoxList.append(self.checkBox_9); self.checkBoxList.append(self.checkBox_10);
		self.checkBoxList.append(self.checkBox_11); self.checkBoxList.append(self.checkBox_12); self.checkBoxList.append(self.checkBox_13); self.checkBoxList.append(self.checkBox_14); self.checkBoxList.append(self.checkBox_15);
		self.checkBoxList.append(self.checkBox_16); self.checkBoxList.append(self.checkBox_17); self.checkBoxList.append(self.checkBox_18); self.checkBoxList.append(self.checkBox_19); self.checkBoxList.append(self.checkBox_20);
		self.checkBoxList.append(self.checkBox_21); self.checkBoxList.append(self.checkBox_22); self.checkBoxList.append(self.checkBox_23); self.checkBoxList.append(self.checkBox_24); self.checkBoxList.append(self.checkBox_25);
		self.checkBoxList.append(self.checkBox_26); self.checkBoxList.append(self.checkBox_27); self.checkBoxList.append(self.checkBox_28); self.checkBoxList.append(self.checkBox_29); self.checkBoxList.append(self.checkBox_30);
		self.checkBoxList.append(self.checkBox_31); self.checkBoxList.append(self.checkBox_32); self.checkBoxList.append(self.checkBox_33); self.checkBoxList.append(self.checkBox_34); self.checkBoxList.append(self.checkBox_35);
		
		#signal and slot
		self.pushButtonLoad1.clicked.connect(lambda: self.loadNumber(1)); self.pushButtonLoad2.clicked.connect(lambda: self.loadNumber(2));
		self.pushButtonLoad3.clicked.connect(lambda: self.loadNumber(3)); self.pushButtonLoad4.clicked.connect(lambda: self.loadNumber(4));
		self.pushButtonLoad5.clicked.connect(lambda: self.loadNumber(5)); self.pushButtonLoad6.clicked.connect(lambda: self.loadNumber(6));
		self.pushButtonLoad7.clicked.connect(lambda: self.loadNumber(7)); self.pushButtonLoad8.clicked.connect(lambda: self.loadNumber(8));
		self.pushButtonLoad9.clicked.connect(lambda: self.loadNumber(9)); self.pushButtonLoad0.clicked.connect(lambda: self.loadNumber(0));
		
		self.pushButtonTrain.clicked.connect(self.train)
		
		self.pushButtonPredict.clicked.connect(self.predict)
		#signal and slot
	
	def loadNumber(self, number):
		size = self.numberToLoad.shape[0]
		for x in range (0, size):
			if(self.numberToLoad[x][number] == 1): self.checkBoxList[x].setChecked(True)
			else: self.checkBoxList[x].setChecked(False)
			
	def predict(self):
		size = self.numberToLoad.shape[0]
		pixel = np.zeros([35, 1])
		
		for x in range (0, size):
			if(self.checkBoxList[x].isChecked()): pixel[x][0] = 1
			else: pixel[x][0] = 0
		
		a0 = self.normf(pixel, 0, 1)
		a1 = self.fpnet(a0, self.weightRes1, self.biasRes1, 1)
		a2 = self.fpnet(a1, self.weightRes2, self.biasRes2, 0)
		output = self.denormf(a2, 0, 1)
		output = int(output * 10)
		if(output > 9): output = 9
		
		self.labelOutput.setText(str(output))
	
	#DENORMF - denormalization function
	def denormf(self, nx, xmin, xmax):
		x = 0.5 * (nx + 1) * (xmax - xmin) + xmin
		return x
	
	#NORMF - normalization function
	def normf(self, x, xmin, xmax):
		nx = 2 * (x - xmin) / (xmax - xmin) - 1
		return nx
	
	#DTF - Derivative of transfer function
	def dtf(self, a, tftype):
		if(tftype == 0):
			dv = np.diag(np.ones(a.size))		#linear transfer function
		elif(tftype == 1):
			dv = np.diag((a * (1 - a))[:, 0])	#logsig transfer function
		elif(tftype == 2):
			dv = np.diag(((1 - a) *  a)[:, 0])	#tansig transfer function
		return dv
	
	#HARDLIM function
	def hardlim(self, x):
		for x in np.nditer(n, op_flags=['readwrite']):
			if x >= 0:
				x[...] = 1
			else:
				x[...] = 0
	
	#FPNET - forward propagation of neural network
	def fpnet(self, p, w, b, tftype):
		col = p.shape[1]
		o = np.ones([1, col])
		n = np.matmul(w, p) + np.matmul(b, o)
		if tftype == 0:
			a = n
		elif tftype == 1:
			a = 1 / (1 + np.exp(-n))
		elif tftype == 2:
			a = (np.exp(n) - np.exp(-n)) / (np.exp(n) + np.exp(-n))
		elif tftype == 3:
			a = hardlim(n)
		return a
	
	#SLAYER - Layer sensitifity
	def slayer(self, a, w, s, tftype):
		s1 = np.matmul(self.dtf(a, tftype), np.matmul((w.T), s))
		return s1
	
	#SOUT - Output sensitifity
	def sout(self, a, t, tftype):
		so = -2 * np.matmul(self.dtf(a, tftype), (t - a))
		return so
	
	def train(self):
		#p1 = [0, 0]; p2 = [0, 5]; p3 = [5, 0]; p4 = [5, 5];
		#t1 = [0]; t2 = [5]; t3 = [5]; t4 = [0];
		p0 = self.numberPixel0; p1 = self.numberPixel1; p2 = self.numberPixel2;
		p3 = self.numberPixel3; p4 = self.numberPixel4; p5 = self.numberPixel5;
		p6 = self.numberPixel6; p7 = self.numberPixel7; p8 = self.numberPixel8;
		p9 = self.numberPixel9;
		#t0 = [0, 0, 0, 0]; t1 = [0, 0, 0, 1]; t2 = [0, 0, 1, 0]; t3 = [0, 0, 1, 1]; t4 = [0, 1, 0, 0];
		#t5 = [0, 1, 0, 1]; t6 = [0, 1, 1, 0]; t7 = [0, 1, 1, 1]; t8 = [1, 0, 0, 0]; t9 = [1, 0, 0, 1];
		t0 = [0]; t1 = [1]; t2 = [2]; t3 = [3]; t4 = [4];
		t5 = [5]; t6 = [6]; t7 = [7]; t8 = [8]; t9 = [9];
		po = np.array([p0, p1, p2, p3, p4, p5, p6, p7, p8, p9]).T
		to = np.array([t0, t1, t2, t3, t4, t5, t6, t7, t8, t9]).T
		#po = np.array([p1, p2, p3, p4]).T
		#to = np.array([t1, t2, t3, t4]).T
		
		rowp = po.shape[0]
		colp = po.shape[1]
		rowt = to.shape[0]
		
		ni = rowp		#number of input
		nt = rowt		#number of target
		nls = colp		#number of learning set
		nnum = 18		#number of layer's hidden node
		
		w1 = 2 * np.random.rand(nnum, ni) - 1
		b1 = 2 * np.random.rand(nnum, 1) - 1
		w2 = 2 * np.random.rand(nt, nnum) - 1
		b2 = 2 * np.random.rand(nt, 1) - 1
		o = np.ones([1, nls])
		
		pmin = np.min(po); pmax = np.max(po)
		tmin = np.min(to); tmax = np.max(to)
		p = self.normf(po, pmin, pmax)
		t = self.normf(to, tmin, tmax)
		
		lr = 0.3				#learning rate
		momOriginal = 0.2		#original value of momentum
		theta = 0.05			#error threshold
		increase = 1.1			#decrease factor
		decrease = 0.6			#increase factor
		deltaError = 0			#error difference between interation
		
		dw1 = 0; db1 = 0; dw2 = 0; db2 = 0;
		errtol = 1; errtolmax = 1e-6; epoch = 0; epochmax = 2000;
		oldError = 0; mom = momOriginal;
		
		while(errtol > errtolmax and epoch < epochmax):
			epoch = epoch + 1
			errtol = 0
			
			for i in range (0, nls):
				a0 = p[:, i][np.newaxis].T
				a1 = self.fpnet(a0, w1, b1, 1)
				a2 = self.fpnet(a1, w2, b2, 0)
				a = a2
				e = t[:, i] - a
				J = np.sum(e ** 2)
				if(J > errtolmax / nls):
					s2 = self.sout(a2, t[:, i][np.newaxis].T, 0)
					s1 = self.slayer(a1, w2, s2, 1)
					
					dw2 = mom * dw2 - (1 - mom) * lr * s2 * a1.T
					db2 = mom * db2 - (1 - mom) * lr * s2
					dw1 = mom * dw1 - (1 - mom) * lr * s1 * a0.T
					db1 = mom * db1 - (1 - mom) * lr * s1
					
					temp_w2 = w2
					temp_b2 = b2
					temp_w1 = w1
					temp_b1 = b1
					
					w2 = w2 + dw2
					b2 = b2 + db2
					w1 = w1 + dw1
					b1 = b1 + db1
				
				errtol = errtol + J
			
			deltaError = errtol - oldError
			deltaError = deltaError / errtol
			oldError = errtol
			self.labelEpoch.setText(str(epoch))
			self.labelError.setText(str(errtol))
			
			if(deltaError > 0 and deltaError > theta):
				w2 = temp_w2
				b2 = temp_b2
				w1 = temp_w1
				b1 = temp_b1
				lr = lr * decrease
				mom = 0
			elif(deltaError > 0 and deltaError <= theta):
				mom = momOriginal
			elif(deltaError <= 0):
				lr = lr * increase
				mom = momOriginal
		
		self.weightRes1 = w1
		self.biasRes1 = b1
		self.weightRes2 = w2
		self.biasRes2 = b2
		
		self.pushButtonPredict.setEnabled(True)
	
	def fileQuit(self):
		sys.exit()
		
		
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	prog = numRec(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())