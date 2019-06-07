import numpy as np 
x = np.zeros((8,8))
#print(x)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)