import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv("tips.csv")
sb.swarmplot(x="total_bill", y="day", data= df)
plt.show()