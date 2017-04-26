import numpy as np

weight = np.array([[-4.6813, -8.1879, 3.6102],
                   [-8.3406, 0.0894, -6.0748]])

bias = np.array([[2.2380],
                 [4.9967]])

dataSetInput = np.array([[0.850,
                          0.800,
                          0.900,
                          0.100,
                          0.000,
                          0.100,
                          0.100,
                          0.100,
                          0.150,
                          0.100],
                         [0.750,
                          0.750,
                          0.800,
                          0.950,
                          0.850,
                          0.500,
                          0.450,
                          0.000,
                          0.100,
                          0.100],
                         [0.100,
                          0.000,
                          0.150,
                          0.500,
                          0.500,
                          0.850,
                          0.900,
                          0.100,
                          0.000,
                          0.150]])

ones = np.ones((1, 10))

n1 = np.matmul(weight, dataSetInput)
n2 = np.matmul(bias, ones)
n = np.add(n1, n2)

print("\nWeight:\n" + str(weight))
print("\nBias:\n" + str(bias))
print("\nData Set Input:\n" + str(dataSetInput))

# hardlim
for x in np.nditer(n, op_flags=['readwrite']):
    if x >= 0:
        x[...] = 1
    else:
        x[...] = 0

print("\nIdentifikasi Gas:\n" + str(n))
