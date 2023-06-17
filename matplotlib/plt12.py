import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]


plt.bar(x, y, color = "#4CAF50")

plt.show()