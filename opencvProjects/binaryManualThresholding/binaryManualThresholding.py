import os, cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.widgets import Slider, Button

def _binary(_img):
	_imgHeight, _imgWidth = _img.shape
	_imgBin = np.empty((_imgHeight, _imgWidth))
	_indexThreshold1 = _img >= _threshold
	_imgBin[_indexThreshold1] = 255
	_indexThreshold2 = _img < _threshold
	_imgBin[_indexThreshold2] = 0
	return _imgBin

def _changeThreshold(val):
	global _percentThreshold
	global _threshold
	_percentThreshold = _slider.val
	_threshold = _percentThreshold / 100 * 255
	_changeImage(None)

def _changeImage(event):
	if event != None:
		global _imageIndex
		_imageIndex += 1
		if _imageIndex == _imageTotal:
			_imageIndex = 0
	
	_img = cv2.imread(_images[_imageIndex], cv2.IMREAD_UNCHANGED)
	_img = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)
	_fig1ShowIt.set_array(_img)
	
	_imgBin = _binary(_img)
	_fig2ShowIt.set_array(_imgBin)
	plt.draw()

_projectDirectory = os.path.dirname(__file__)
_imagesDirectory = os.path.join(_projectDirectory, "images")

_images = []
for _root, _dirs, _files in os.walk(_imagesDirectory):
	for _file in _files:
		if _file.endswith(".jpg"):
			_images.append(_imagesDirectory + "\\" + _file)

_imageIndex = 0
_imageTotal = len(_images)

_img = cv2.imread(_images[_imageIndex], cv2.IMREAD_UNCHANGED)
_img = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)

_sliderInitVal = 50
_percentThreshold = _sliderInitVal
_threshold = _percentThreshold / 100 * 255

_fig = plt.figure("Binary Image with Manual Thresholding")
_gs = GridSpec(15, 2)
_fig1 = plt.subplot(_gs[0:13, 0])
plt.xticks([]), plt.yticks([]) #hide tick values on X and Y axis
_fig1.set_title("Original")
_fig1ShowIt = plt.imshow(_img, cmap = "gray")

_imgBin = _binary(_img)
_fig2 = plt.subplot(_gs[0:13, 1])
plt.xticks([]), plt.yticks([]) #hide tick values on X and Y axis
_fig2.set_title("Binary")
_fig2ShowIt = plt.imshow(_imgBin, cmap = "gray")

_sliderAx = _fig.add_axes([0.2, 0.1, 0.4, 0.05])
_slider = Slider(_sliderAx, "Threshold (%)", 0, 100, valinit = _sliderInitVal)
_sliderCid = _slider.on_changed(_changeThreshold)
_ChangeAx = _fig.add_axes([0.7, 0.1, 0.1, 0.05])
_changeButton = Button(_ChangeAx, "Change")
_changeButtonCid = _changeButton.on_clicked(_changeImage)

plt.show()
