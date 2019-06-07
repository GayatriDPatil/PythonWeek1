import seaborn as sb
import  pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("tips.csv")
sb.swarmplot(x="total_bill", y="size", data= df)
plt.show()