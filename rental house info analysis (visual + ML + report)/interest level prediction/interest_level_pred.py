import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

'''
https://stackoverflow.com/questions/51452031/how-to-use-the-test-data-against-the-trained-model

https://stackoverflow.com/questions/45681387/predict-test-data-using-model-based-on-training-data-set

https://www.kaggle.com/c/titanic/discussion/54683
'''

x_col = ["bathrooms", "bedrooms", "latitude", "longitude", "price"]

df1= pd.read_json('train.json')
xtrain = df1[x_col]

d = {'low':1,'medium':2,'high':3}
df1["interest_level"] = df1["interest_level"].map(d)
ytrain = df1[["interest_level"]]


df2 = pd.read_json('test.json')
xtest = df2[x_col]


model = DecisionTreeRegressor()
model.fit(xtrain, ytrain)
pred = model.predict(xtest)
df2['pred_level'] = pred
df2['pred_level'] = df2['pred_level'].astype(int)
d2 = {1:'low',2:'medium', 3:'high'}
df2['pred_level']  = df2['pred_level'] .map(d2)
df1["interest_level"] = df1["interest_level"].map(d2)

df1.to_csv("training_data.csv")
df2.to_csv("testing_data.csv")
