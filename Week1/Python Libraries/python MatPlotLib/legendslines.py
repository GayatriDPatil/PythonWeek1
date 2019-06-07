import matplotlib.pyplot as plit
import pandas as pd 
x1 = [10,20,30]
y1 = [20,40,10]
plit.plot(x1,y1, label="line1")

#line2 ponts
x2= [10,20,30]
y2= [40,10,30]
plit.plot(x2,y2, label='line2')
plit.legend()
plit.show()