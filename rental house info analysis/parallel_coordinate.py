import pandas as pd
from pandas.plotting import parallel_coordinates
import matplotlib.pyplot as plt
import plotly.express as px

#https://plotly.com/python/parallel-coordinates-plot/
#https://stackoverflow.com/questions/38103738/plotting-parallel-coordinates-in-pandas-python

df = pd.read_json("train.json")

fig = px.parallel_coordinates(df, color="price",
                             color_continuous_scale=px.colors.diverging.Tealrose,
                             color_continuous_midpoint=2)
fig.show()

'''

fig, ax = plt.subplots(figsize=(15,10))
parallel_coordinates(
    df[['bathrooms', 'bedrooms',
        'latitude', 'listing_id', 'longitude', 'price']],
    'price')

plt.savefig("para_corr.png")
plt.show()
plt.close()'''