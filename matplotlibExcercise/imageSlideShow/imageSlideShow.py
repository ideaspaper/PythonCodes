import os, cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

_projectDirectory = os.path.dirname(__file__)
_imagesDirectory = os.path.join(_projectDirectory, "images")

#record all the images inside _imageDirectory folder into a list
_images = []
for _root, _dirs, _files in os.walk(_imagesDirectory):
	for _file in _files:
		if _file.endswith(".jpg"):
			_images.append(_imagesDirectory + "\\" + _file)

#prepare the figure
#mpl.rcParams['toolbar'] = 'None' #disable matplotlib toolbar
_fig = plt.figure("Image Slideshow")
_gs = GridSpec(3, 3)
_fig1 = plt.subplot(_gs[0:3, 0:3])

#initialize the figure with first image in the list
_imageIndex = 0
_imageTotal = len(_images)
_img = cv2.imread(_images[_imageIndex], cv2.IMREAD_UNCHANGED)
_imgShow = cv2.cvtColor(_img, cv2.COLOR_BGR2RGB) #for displaying purpose
_imgShowIt = plt.imshow(_imgShow)

def _changeImage(event):
	global _imageIndex #global is needed if we want to assign a value to the global variable
	_imageIndex += 1
	if _imageIndex == _imageTotal: #no global needed if we just want to read the value of global variable (declared on line 23)
		_imageIndex = 0
	_img = cv2.imread(_images[_imageIndex], cv2.IMREAD_UNCHANGED) #this syntax doesn't refer to variable declared on line 24
	_imgShow = cv2.cvtColor(_img, cv2.COLOR_BGR2RGB) #for displaying purpose, also this syntax doesn't refer to variable declared on line 25
	_imgShowIt.set_array(_imgShow) #modify the data inside global object declared on line 26, no global needed since we use the object's method
	plt.draw()
	
_cid = _fig.canvas.mpl_connect('button_press_event', _changeImage) #record the connection id, so we can disconnect the callback later

plt.xticks([]), plt.yticks([]) #hide tick values on X and Y axis
plt.tight_layout()
plt.show()
