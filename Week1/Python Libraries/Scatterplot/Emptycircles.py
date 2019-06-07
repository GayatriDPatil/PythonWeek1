import matplotlib.pyplot as plt
#from pylab import randn
import numpy as np 

#x = randn(50)
#y = randn(50)
x = np.random.randn(50)
y = np.random.randn(50)
plt.scatter(x,y, facecolor='none',edgecolors='g')
plt.show()