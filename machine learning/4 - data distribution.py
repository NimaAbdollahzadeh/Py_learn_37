
import numpy
import matplotlib.pyplot as plt

data_distribution = numpy.random.uniform(0.0, 10.0, 1000)

plt.hist(data_distribution, 10)
plt.show()
