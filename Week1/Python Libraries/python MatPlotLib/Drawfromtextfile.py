import matplotlib.pyplot as plit
with open('test.txt') as f:
    data = f.read()
data = data.split('\n')
x= [row.split(' ')[0] for row in data]
y= [row.split(' ')[1] for row in data]
plit.plot(x,y)
plit.show()