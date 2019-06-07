import numpy as np
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[0,0,0],
    [0,0,0],
    [0,0,0]]
# inverse using library
inverse = np.linalg.inv(X)
print(inverse)
# transpose using library
ConvertMaytrix = np.matrix(X) 
Result = ConvertMaytrix.transpose() 
print(Result)
# by loop transpose
for i in range(0,len(X)):
    for j in range(0,len(X)):
        Y[i][j] = X[j][i]
print(Y)