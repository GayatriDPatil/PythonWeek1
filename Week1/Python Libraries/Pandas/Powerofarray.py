#import pandas as pd 
#x = pd.DataFrame({'X':[0 ,1, 2, 3, 4, 5, 6]})
#print(x)

import numpy as np
x = np.arange(7)
print("Original array", x)
print("First array elements raised to powers from second array, element-wise:")
print(np.power(x, 3))