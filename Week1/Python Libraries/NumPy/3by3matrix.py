import numpy as np 
x = np.ones((5,5))
print('Original Array:', x)
print("1 in the border and 0 in the inside array")
x[1:-1,1:-1] = 0
print(x)