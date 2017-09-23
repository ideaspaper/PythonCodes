import cv2
import numpy as np

_cap = cv2.VideoCapture(0)

def _BGRtoGRAY(_img):
	_imgB, _imgG, _imgR = cv2.split(_img)
	return (_imgB * 0.114 + _imgG * 0.587 + _imgR * 0.299).astype(np.uint8)
	
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
	return cv2.merge((_imgH, _imgS,_imgV))

while(True):
	_ret, _frame = _cap.read()
	_gray = _BGRtoGRAY(_frame)
	cv2.imshow('Normal', _gray)
	_gray = np.rot90(_gray, 1)
	cv2.imshow('Rotation 1', _gray)
	_gray = np.rot90(_gray, 2)
	cv2.imshow('Rotation 2', _gray)
	_gray = np.rot90(_gray, 3)
	cv2.imshow('Rotation 3', _gray)
	_gray = np.fliplr(_gray)
	_gray = np.flipud(_gray)
	cv2.imshow('Flip', _gray)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
_cap.release()
cv2.destroyAllWindows()