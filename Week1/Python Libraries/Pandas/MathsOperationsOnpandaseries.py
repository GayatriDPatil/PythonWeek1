import pandas as pd 
x = pd.Series([2, 4, 6, 8, 10])
y = pd.Series([1, 3, 5, 7, 9])
add = x + y
print("Addition :",add)
subtract = x-y
print("Substraction :", subtract)
multiple = x*y
print("Multiplication :", multiple)
divide = x/y
print("Division :", divide)