import seaborn as sb
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('titanic.csv')
#x = df["sex"]
#y = df["survived"]
sb.barplot(x = "sex", y = "survived", hue = "class", data = df)
plt.show()