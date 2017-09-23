import os, cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

_projectDirectory = os.path.dirname(__file__)
_inputFolder = os.path.join(_projectDirectory, "images/input/")
_fileInputName = "handwriting3"
_fileFormat = ".jpg"

_percentThreshold = 52
_threshold = _percentThreshold / 100 * 255

_img = cv2.imread(_inputFolder + _fileInputName + _fileFormat, cv2.IMREAD_UNCHANGED)
_img = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)
_imgHeight, _imgWidth = _img.shape

_fig = plt.figure("Binary Image with Manual Thresholding")
_gs = GridSpec(1, 2)

_fig1 = plt.subplot(_gs[0, 0])
_fig1.set_title("Original")
plt.imshow(_img, cmap = "gray")

_imgBin = np.empty((_imgHeight, _imgWidth))
_indexThreshold1 = _img >= _threshold
_imgBin[_indexThreshold1] = 255
_indexThreshold2 = _img < _threshold
_imgBin[_indexThreshold2] = 0

_fig2 = plt.subplot(_gs[0, 1])
_fig2.set_title("Threshold: " + str(_percentThreshold) + "%")
plt.imshow(_imgBin, cmap = "gray")

plt.xticks([]), plt.yticks([]) #hide tick values on X and Y axis
plt.tight_layout()
plt.show()