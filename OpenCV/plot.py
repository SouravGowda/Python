'''import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dirtydata.csv')
df1=df.dropna()


# df1.plot( kind='hist',x='Duration',y='Calories')
df["Duration"].plot(kind = 'hist')
plt.show()
'''

'''
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
'''


import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()



'''
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode=[0.2,0,0,0]

plt.pie(y, labels = mylabels)#explode=myexplode)
plt.legend(title = "Four Fruits:")
plt.show()


# SEABORN
# import seaborn as sns

# sns.distplot([0, 1, 2, 3, 4, 5])

