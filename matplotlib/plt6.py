import matplotlib.pyplot as plt
import numpy as np

x = xpoints = np.array([2, 6, 4, 9])
y = ypoints = np.array([1, 13, 15, 5])

plt.plot(x, ls = ':', lw = "3.5", c = '#4CAF50')
plt.plot(y)
plt.show()