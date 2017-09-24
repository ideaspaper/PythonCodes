import os
import numpy as np

_projectDirectory = os.path.dirname(__file__)
_fileName1 = os.path.join(_projectDirectory, "file1.txt")

_dataWrite = np.arange(25).reshape(5, 5)
print("Write to file:")
print(_dataWrite)
print()
np.savetxt(_fileName1, _dataWrite, delimiter = "; ")

_dataRead = np.loadtxt(_fileName1, delimiter = ";")
print("Read from file:")
print(_dataRead)
print()

print("Multiply the read data with 5:")
print(_dataRead * 5)