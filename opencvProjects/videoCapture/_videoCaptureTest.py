import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib.animation as anm

_cap = cv2.VideoCapture(0)
_fig = plt.figure("Camera")
_gs = GridSpec(3, 3)

def captureFrame(i):
	_ret, _frame = _cap.read()
	#plt.imshow(_frame)
	
	_fig1 = plt.subplot(_gs[0:3, 0:2])
	_fig1.set_title("RGB Space")
	_frame1Show = cv2.cvtColor(_frame, cv2.COLOR_BGR2RGB) #for displaying purpose
	plt.imshow(_frame1Show)
	
	'''_fig2 = plt.subplot(_gs[0, 2])
	_fig2.set_title("GRAYSCALE Space")
	_frame2 = cv2.cvtColor(_frame, cv2.COLOR_BGR2GRAY)
	plt.imshow(_frame2, cmap = "gray")

	_fig3 = plt.subplot(_gs[1, 2])
	_fig3.set_title("YCrCb Space")
	_frame3 = cv2.cvtColor(_frame, cv2.COLOR_BGR2YCrCb)
	_frame3Show = cv2.cvtColor(_frame3, cv2.COLOR_BGR2RGB) #for displaying purpose
	plt.imshow(_frame3Show)

	_fig4 = plt.subplot(_gs[2, 2])
	_fig4.set_title("HSV Space")
	_frame4 = cv2.cvtColor(_frame, cv2.COLOR_BGR2HSV)
	_frame4Show = cv2.cvtColor(_frame4, cv2.COLOR_BGR2RGB) #for displaying purpose
	plt.imshow(_frame4Show)
	plt.tight_layout()'''
	
	
ani = anm.FuncAnimation(_fig, captureFrame, interval = 0)
plt.show()