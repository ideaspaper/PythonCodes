import numpy as np

_iterationReturn = 0
_vectorReturn = 0

def numpyCarelessIteration():
	_data = np.arange(25).reshape(5, 5)
	_rows, _cols = _data.shape
	for i in range(0, _rows):
		for j in range(0, _cols):
			_data[i, j] += 10
	return _data
	
def numpyVectorOperation():
	_data = np.arange(25).reshape(5, 5)
	_data += 10
	return _data
	
#print(numpyCarelessIteration())
#print(numpyVectorOperation())

if __name__ == '__main__':
	import timeit
	print("Careless iteration: " + str(timeit.timeit("numpyCarelessIteration()", setup = "from __main__ import numpyCarelessIteration")))
	print("Vector operation: " + str(timeit.timeit("numpyVectorOperation()", setup = "from __main__ import numpyVectorOperation")))

