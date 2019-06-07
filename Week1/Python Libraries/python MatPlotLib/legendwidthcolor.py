import  matplotlib.pyplot as plt
x1 = [10,20,30]
y1 = [20,40,10]
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]

plt.plot(x1,y1, color='blue', linewidth = 3, label = 'line-width-3')
plt.plot(x2,y2, Color='red', linewidth = 7, label = 'line-width-7')
plt.legend()
plt.show()