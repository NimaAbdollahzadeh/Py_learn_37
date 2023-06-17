import numpy
from scipy import stats


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = numpy.mean(speed)
print(mean)

median = speed.sort()
median = numpy.median(speed)
print(median)

mode = stats.mode(speed)
print(mode)