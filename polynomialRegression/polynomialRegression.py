import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

xData = np.array([30, 50, 80, 100])
yData = np.array([300, 250, 190, 150])
z = np.polyfit(xData, yData, 2)

print(z)
plt.plot(xData, yData, 'o')
xp = np.linspace(0, 500, 100)
plt.plot(xp, np.polyval(z, xp), 'r')

plt.show()