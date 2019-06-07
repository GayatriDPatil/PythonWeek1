import pandas as pd
import  seaborn as sb
from matplotlib import  pyplot as plt
df = pd.read_csv("iris.csv.1")
#x= df["species"]
#y = df["sepal_length"]
sb.violinplot(x = "species", y = "sepal_length",  data = df)
plt.show()