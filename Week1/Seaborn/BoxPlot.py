import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
#df = sb.load_dataset('iris')
#sb.boxplot(data = df, orient = "h")
df = pd.read_csv("tips.csv")
sb.boxplot(x="day", y="tip", data= df)
plt.show()