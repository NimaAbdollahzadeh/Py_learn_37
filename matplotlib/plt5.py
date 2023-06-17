import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o--b', ms = 20, mec = "r", mfc = "green")
plt.show()