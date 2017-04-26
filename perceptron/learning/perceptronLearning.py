import numpy as np

# initializing weight and bias with random samples from a uniform
# distribution over [-1, 1)
weight = 2 * np.random.rand(2, 3) - 1
bias = 2 * np.random.rand(2, 1) - 1

trainingSetInput = np.array([[0.800,
                              0.850,
                              0.900,
                              0.200,
                              0.100,
                              0.250,
                              0.150,
                              0.100,
                              0.150,
                              0.100,
                              0.050,
                              0.000],
                             [0.700,
                              0.750,
                              0.800,
                              0.900,
                              0.800,
                              0.800,
                              0.400,
                              0.450,
                              0.500,
                              0.050,
                              0.020,
                              0.000],
                             [0.100,
                              0.050,
                              0.150,
                              0.400,
                              0.500,
                              0.400,
                              0.800,
                              0.850,
                              0.900,
                              0.050,
                              0.000,
                              0.000]])

trainingSetOutput = np.array([[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                              [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]])

ones = np.ones([1, trainingSetOutput.shape[1]])

for iteration in range(0, 2000):
    n1 = np.matmul(weight, trainingSetInput)
    n2 = np.matmul(bias, ones)
    n = np.add(n1, n2)

    for x in np.nditer(n, op_flags=['readwrite']):
        if x >= 0:
            x[...] = 1
        else:
            x[...] = 0

    e = np.subtract(trainingSetOutput, n)
    w1 = np.matmul(e, trainingSetInput.transpose())
    weight = np.add(weight, w1)
    b1 = np.matmul(e, ones.transpose())
    bias = np.add(bias, b1)

    ssqe = np.sum(e**2)
    print("Iteration " + str(iteration) + " sum squared error: " + str(ssqe))
    if ssqe == 0:
        break

print("\nWeight:\n" + str(weight))
print("\nBias:\n" + str(bias))
