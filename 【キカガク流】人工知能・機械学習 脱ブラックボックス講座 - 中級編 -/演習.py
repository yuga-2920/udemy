import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("\\Users\\karon\\OneDrive\\ドキュメント\\practice\\udemy\\【キカガク流】人工知能・機械学習 脱ブラックボックス講座 - 中級編 -\\housing.csv")

#sns.distplot(df['x5'],bins=10)
#sns.pairplot(df)

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

model = LinearRegression()

"""
model.fit(X,y)
model.score(X,y)
"""

X_train ,X_test ,y_train ,y_test = train_test_split(X,y,test_size=0.4,random_state=1)

model.fit(X_train,y_train)

"""
score = model.score(X_test,y_test)
print(score)
print(model.score(X_train,y_train))
"""

x = X.iloc[0,:]
y_pred = model.predict([x])[0]

"""
joblib.dump(model,"model.pkl")
"""

model_new = joblib.load("\\Users\\karon\\OneDrive\\ドキュメント\\practice\\udemy\\【キカガク流】人工知能・機械学習 脱ブラックボックス講座 - 中級編 -\\model.pkl")

#print(model_new.predict([x]))

np.set_printoptions(precision=3,suppress=True)
print(model.coef_)