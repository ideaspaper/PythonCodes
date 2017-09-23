import os, cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

_projectDirectory = os.path.dirname(__file__)
_fileName = os.path.join(_projectDirectory, "images/input/Lenna512x512.jpg")

_img = cv2.imread(_fileName, cv2.IMREAD_UNCHANGED)
_fig = plt.figure("Color Spaces")
_gs = GridSpec(3, 3)

_fig1 = plt.subplot(_gs[0:3, 0:2])
_fig1.set_title("RGB Space")
_img1Show = cv2.cvtColor(_img, cv2.COLOR_BGR2RGB) #for displaying purpose
plt.imshow(_img1Show)

_fig2 = plt.subplot(_gs[0, 2])
_fig2.set_title("GRAYSCALE Space")
_img2 = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)
plt.imshow(_img2, cmap = "gray")

_fig3 = plt.subplot(_gs[1, 2])
_fig3.set_title("YCrCb Space")
_img3 = cv2.cvtColor(_img, cv2.COLOR_BGR2YCrCb)
_img3Show = cv2.cvtColor(_img3, cv2.COLOR_BGR2RGB) #for displaying purpose
plt.imshow(_img3Show)

_fig4 = plt.subplot(_gs[2, 2])
_fig4.set_title("HSV Space")
_img4 = cv2.cvtColor(_img, cv2.COLOR_BGR2HSV)
_img4Show = cv2.cvtColor(_img4, cv2.COLOR_BGR2RGB) #for displaying purpose
plt.imshow(_img4Show)

plt.tight_layout()
plt.show()