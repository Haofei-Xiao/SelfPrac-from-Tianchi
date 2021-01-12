import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
https://stackoverflow.com/questions/39922986/pandas-group-by-and-sum
https://stackoverflow.com/questions/27842613/pandas-groupby-sort-within-groups
https://www.kite.com/python/answers/how-to-display-the-value-of-each-bar-in-a-bar-chart-using-matplotlib-in-python

'''

df = pd.read_csv("h1b_kaggle.csv")

fig, ax = plt.subplots(figsize=(15,7))
graph = df.groupby(['EMPLOYER_NAME'])['PREVAILING_WAGE'].sum().nlargest(10)
graph = graph.to_frame().reset_index()  # convert series to df for graph

sns.barplot(x=graph["PREVAILING_WAGE"], y=graph["EMPLOYER_NAME"])
plot = sns.barplot(x=graph["PREVAILING_WAGE"], y=graph["EMPLOYER_NAME"])

# adjusing visual effect
plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.25, bottom=0.1, right=0.96, top=0.9)
ax.set_ylabel('companies')
ax.set_xlabel('wages (10^8)')
ax.set_title('tot wage of top 10 companies applying h1b')

# put value in bar graph
for index, value in enumerate(graph["PREVAILING_WAGE"]):
    plt.text(value, index, s=round(value, 2))

plt.savefig("top 10 h1b comp wage.png")
plt.show()