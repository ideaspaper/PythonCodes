import os, cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def _BGRtoGRAY(_img):
	_imgB, _imgG, _imgR = cv2.split(_img)
	return (_imgB * 0.114 + _imgG * 0.587 + _imgR * 0.299).astype(np.uint8)
	
def _BGRtoCMYK(_img):
	_imgB, _imgG, _imgR = cv2.split(_img)
	_imgB = _imgB / 255.0
	_imgG = _imgG / 255.0
	_imgR = _imgR / 255.0
	
	_imgK = 1 - cv2.max(_imgB, cv2.max(_imgG, _imgR))
	_imgC = (1 - _imgR - _imgK) / (1 - _imgK)
	_imgM = (1 - _imgG - _imgK) / (1 - _imgK)
	_imgY = (1 - _imgB - _imgK) / (1 - _imgK)
	
	_imgK = _imgK * 255
	_imgC = _imgC * 255
	_imgM = _imgM * 255
	_imgY = _imgY * 255
	
	_imgK = _imgK.astype(np.uint8)
	_imgC = _imgC.astype(np.uint8)
	_imgM = _imgM.astype(np.uint8)
	_imgY = _imgY.astype(np.uint8)
	return _imgC, _imgM, _imgY, _imgK

def _BGRtoHSV(_img):
	_imgB, _imgG, _imgR = cv2.split(_img)
	_imgB = _imgB / 255.0
	_imgG = _imgG / 255.0
	_imgR = _imgR / 255.0
	
	_imgV = cv2.max(_imgB, cv2.max(_imgG, _imgR))
	_imgS = np.copy(_imgV)
	_imgH = np.copy(_imgV)
	_minRGB = cv2.min(_imgB, cv2.min(_imgG, _imgR))
	
	_indexVIsNotZero = _imgV != 0
	_imgS[_indexVIsNotZero] = (_imgV[_indexVIsNotZero] - _minRGB[_indexVIsNotZero]) / _imgV[_indexVIsNotZero]
	_indexVIsZero = _imgV == 0
	_imgS[_indexVIsZero] = 0
	
	_indexVIsR = _imgV == _imgR
	_imgH[_indexVIsR] = 60 * (_imgG[_indexVIsR] - _imgB[_indexVIsR]) / (_imgV[_indexVIsR] - _minRGB[_indexVIsR])
	_indexVIsG = _imgV == _imgG
	_imgH[_indexVIsG] = 120 + 60 * (_imgB[_indexVIsG] - _imgR[_indexVIsG]) / (_imgV[_indexVIsG] - _minRGB[_indexVIsG])
	_indexVIsB = _imgV == _imgB
	_imgH[_indexVIsB] = 240 + 60 * (_imgR[_indexVIsB] - _imgG[_indexVIsB]) / (_imgV[_indexVIsB] - _minRGB[_indexVIsB])
	
	_indexHIsSmallerThanZero = _imgH < 0
	_imgH[_indexHIsSmallerThanZero] += 360
	
	_imgH = _imgH / 360 * 180
	_imgS = _imgS * 255
	_imgV = _imgV * 255
	
	_imgH = _imgH.astype(np.uint8)
	_imgS = _imgS.astype(np.uint8)
	_imgV = _imgV.astype(np.uint8)
	return cv2.merge((_imgV, _imgS,_imgH))
	
_projectDirectory = os.path.dirname(__file__)
_fileName = os.path.join(_projectDirectory, "images/input/Lenna512x512.jpg")

_img = cv2.imread(_fileName,cv2.IMREAD_UNCHANGED)
_fig = plt.figure("Color Spaces")
_gs = GridSpec(4, 4)

_fig1 = plt.subplot(_gs[0:4, 0:2])
_fig1.set_title("RGB Space")
_img1Show = cv2.cvtColor(_img, cv2.COLOR_BGR2RGB) #for displaying purpose
plt.imshow(_img1Show)

_fig2 = plt.subplot(_gs[0, 2:4])
_fig2.set_title("GRAYSCALE Space")
_img2 = _BGRtoGRAY(_img)
plt.imshow(_img2, cmap = "gray")


_img3, _img4, _img5, _img6 = _BGRtoCMYK(_img)
_fig3 = plt.subplot(_gs[1, 2])
_fig3.set_title("Cyan space")
plt.imshow(_img3, cmap = "gray")
_fig4 = plt.subplot(_gs[1, 3])
_fig4.set_title("Magenta space")
plt.imshow(_img4, cmap = "gray")
_fig5 = plt.subplot(_gs[2, 2])
_fig5.set_title("Yellow space")
plt.imshow(_img5, cmap = "gray")
_fig6 = plt.subplot(_gs[2, 3])
_fig6.set_title("Black space")
plt.imshow(_img6, cmap = "gray")

_fig7 = plt.subplot(_gs[3, 2:4])
_fig7.set_title("HSV Space")
_img7 = _BGRtoHSV(_img)
plt.imshow(_img7)

plt.tight_layout()
plt.show()