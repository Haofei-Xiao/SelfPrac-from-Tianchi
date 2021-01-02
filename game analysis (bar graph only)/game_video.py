import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc("font",family='KaiTi')

df = pd.read_csv('bilibili_honor_top.csv')
popular = df.groupby("up主")

sortdata = popular.size().sort_values(ascending=False).head(10)
plt.figure(figsize=(15,10))
sortdata.plot.bar()
plt.xticks(rotation=50, fontsize = 20)
plt.yticks(fontsize = 20)
plt.ylabel("单位：万", fontsize = 18)
plt.title("王者荣耀播放量最高的10up主", fontsize = 40)
plt.savefig("gameana.png")
plt.show()

