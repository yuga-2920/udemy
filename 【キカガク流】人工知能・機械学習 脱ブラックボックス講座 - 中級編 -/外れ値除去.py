import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("\\Users\\karon\\OneDrive\\ドキュメント\\practice\\udemy\\【キカガク流】人工知能・機械学習 脱ブラックボックス講座 - 中級編 -\\housing.csv")

sns.distplot(df['x6'])

col ='x6'
mean = df.mean()
sigma = df.std()

low = mean[col] - 3 * sigma[col]
high = mean[col] + 3 * sigma[col]

df2 = df[(df[col]>low) & (df[col]<high)]

#sns.distplot(df[col])
#sns.distplot(df2[col])

cols = df.columns

_df = df
for col in cols:
    low = mean[col] - 3 * sigma[col]
    high = mean[col] + 3 * sigma[col]

    _df = _df[(_df[col]>low) & (_df[col]<high)]

X = _df.iloc[:,:-1]
y = _df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)

model = LinearRegression()

"""
model.fit(X_train,y_train)
model.score(X_train,y_train)
model.score(X_test,y_test)
"""

scaler = StandardScaler()
scaler.fit(X_train)
X_train2 = scaler.transform(X_train)
X_test2 = scaler.transform(X_test)

model.fit(X_train2,y_train)
model.score(X_train2,y_train)
np.set_printoptions(precision=3,suppress=True)
print(model.coef_)