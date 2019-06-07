import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv("gapminder-FiveYearData.csv")
#dt = sb.load_dataset("gapminder-FiveYearData.csv")
sb.boxplot(x="lifeExp", y="continent", data= df)
plt.show()