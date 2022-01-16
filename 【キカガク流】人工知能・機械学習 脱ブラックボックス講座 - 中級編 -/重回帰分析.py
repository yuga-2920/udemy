import numpy as np
import pandas as pd

x = np.array([[1],[2],[3]])
X = np.array([[1,2],[3,4]])
Xt =  X.T
X_inv = np.linalg.inv(X)
XX_inv = np.dot(X,X_inv)

X = np.array([
    [1,2,3],
    [1,2,5],
    [1,3,4],
    [1,5,9]
])

y = np.array([
    [1],
    [5],
    [6],
    [8]
])
XtX = np.dot(X.T,X)
XtX_inv = np.linalg.inv(XtX)
Xty = np.dot(X.T,y)
w = np.dot(XtX_inv,Xty)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X,y)
model.score(X,y)


print(model.coef_)
print(model.intercept_)