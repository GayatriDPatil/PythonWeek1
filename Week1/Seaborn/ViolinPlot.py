import pandas as pd
import  seaborn as sb
from matplotlib import  pyplot as plt
df = pd.read_csv("tips.csv")
sb.violinplot(x = "sex", y = "total_bill",  data = df)
plt.show()