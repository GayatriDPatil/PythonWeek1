import matplotlib.pyplot as plt 
#line 1
x1 = [10,20,30]
y1 = [20,40,10]
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]

plt.plot(x1,y1, color='blue', linewidth=3, label='line1', linestyle='dotted', marker='o', markerfacecolor='green', markersize=10)
plt.plot(x2,y2, color='red', linewidth=5, label='line2', linestyle='dashed', marker='o', markerfacecolor='green', markersize=10)
plt.legend()
plt.show()