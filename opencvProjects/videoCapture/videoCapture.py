import cv2
import numpy as np

_cap = cv2.VideoCapture(0)

while(True):
    _ret, _frame = _cap.read()
    cv2.imshow('frame', _frame)
	
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

_cap.release()
cv2.destroyAllWindows()