# from numpy import random

# x=random.randint(100, size=(5))

# print(x)



#TRAIN AND TEST

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 10)
y = numpy.random.normal(150, 40, 10) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]


print(train_x,train_y)
# plt.scatter(train_x, train_y)
# plt.show()