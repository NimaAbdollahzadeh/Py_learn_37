import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340])

plt.title("Sports watch data")
plt.xlabel("Average Pulse")
plt.ylabel("Colorful Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()