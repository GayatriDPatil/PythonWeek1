x = [[5,1,3],[1,1,1],[1,2,1]]
y = [1,2,3]
z = 0
for i in range(0,len(x)):
    for j in range(0,len(y)):
        z = z + x[i][j] * y[j]
    print(z)
    z = 0
