import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('\\Users\\karon\\OneDrive\\ドキュメント\\practice\\udemy\\【キカガク流】人工知能・機械学習 脱ブラックボックス講座 - 初級編 -\\sample.csv')
x = df['x']
y = df['y']
df_c = df - df.mean()

x = df_c['x']
y = df_c['y']

xx = x * x
xy = x * y

a = xy.sum() / xx.sum()

"""
plt.scatter(x,y,label='y')
plt.plot(x,a*x,label='y_hat',color='red')
plt.legend()
plt.show()
"""
x_new = 40
mean = df.mean()
mean_x = df['x']
mean_y = df['y']
xc = x_new - mean_x
yc = a * xc