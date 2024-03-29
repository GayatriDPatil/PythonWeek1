import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

plt.barh(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0), edgecolor='blue')
plt.xlabel('languages')
plt.ylabel("popularity")
plt.title("popularity of programming languages")
plt.xticks(x_pos,x)
plt.minorticks_on()
#plt.grid(which='major', linestyle='-', linewidth='0.5',color='red')
#plt.grid(which='minor', linestyle='-', linewidth='0.5',color='black')
plt.show()