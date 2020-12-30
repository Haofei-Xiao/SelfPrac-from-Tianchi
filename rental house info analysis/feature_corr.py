import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#https://medium.com/@szabo.bibor/how-to-create-a-seaborn-correlation-heatmap-in-python-834c0686b88e

df = pd.read_json("train.json")
fig, ax = plt.subplots(figsize=(15,10))
sns.heatmap(df.corr())
plt.savefig("feature_corr.png")
plt.show()
plt.close()