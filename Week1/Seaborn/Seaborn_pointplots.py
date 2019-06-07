import pandas as pd
import seaborn as sb
from matplotlib import  pyplot as plt
df = pd.read_csv("titanic.csv")
sb.pointplot(x="sex", y="survived", hue = "class", data=df)
plt.show()
