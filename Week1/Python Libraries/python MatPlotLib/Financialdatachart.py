import matplotlib.pyplot as plit
import pandas as pd 
df = pd.read_csv('fdata.csv',',',parse_dates=True,index_col=0)
df.plot()
plit.xlabel('x.axis')
plit.ylabel('y-axis')
plit.title("Financial chart")
plit.show()