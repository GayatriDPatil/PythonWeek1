import numpy
x = [[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]]
y = 4
z = []
z = [j * y for i in x for j in i]
print(z)
#print("\n") 
#print(numpy.transpose(z)) 