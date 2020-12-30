import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#https://stackoverflow.com/questions/23232989/boxplot-stratified-by-column-in-python-pandas
#https://stackoverflow.com/questions/38927459/pandas-boxplot-with-ranges-in-x-axis
df = pd.read_json("train.json")


df['log'] = pd.qcut(df['longitude'],5)
df['lat'] = pd.qcut(df['latitude'],5)

fig, ax =plt.subplots(1,2, figsize=(18, 10))
sns.boxplot(x=df["log"], y=df["price"], data=df, ax=ax[0])
sns.boxplot(x=df["lat"], y=df["price"], data=df, ax=ax[1])
ax[0].set_ylim(0,7000)
ax[1].set_ylim(0,7000)

plt.savefig("lat&logprice_boxplot.png")
plt.show()
plt.close()

