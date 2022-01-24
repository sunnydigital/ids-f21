# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 10:20:23 2021

@author: sunny
"""

import numpy as np
# from statsmodels import robust
# from numpy import nanmean, absolute
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data = pd.read_csv('movieReplicationSet.csv')
data = data.iloc[:,:400]
# print(data['Star Wars: Episode 1 - The Phantom Menace (1999)'])

S1_S2 = []
S1_T = []
S1_S2_T = []

for col, row in data.iterrows():
    if not pd.isna(row['Star Wars: Episode 1 - The Phantom Menace (1999)']) and not pd.isna(row['Star Wars: Episode II - Attack of the Clones (2002)']):
        S1_S2.append([row['Star Wars: Episode 1 - The Phantom Menace (1999)'], row['Star Wars: Episode II - Attack of the Clones (2002)']])
        
for col, row in data.iterrows():
    if not pd.isna(row['Star Wars: Episode 1 - The Phantom Menace (1999)']) and not pd.isna(row['Titanic (1997)']):
        S1_T.append([row['Star Wars: Episode 1 - The Phantom Menace (1999)'], row['Titanic (1997)']])

for col, row in data.iterrows():
    if not pd.isna(row['Star Wars: Episode 1 - The Phantom Menace (1999)']) and not pd.isna(row['Titanic (1997)']) and not pd.isna(row['Star Wars: Episode II - Attack of the Clones (2002)']):
        S1_S2_T.append([row['Star Wars: Episode 1 - The Phantom Menace (1999)'], row['Star Wars: Episode II - Attack of the Clones (2002)'], row['Titanic (1997)']])

S1_S2 = np.array(S1_S2)
S1_T = np.array(S1_T)
S1_S2_T = np.array(S1_S2_T)
# print(S1_S2)
# print(S1_T)

#%% Star Wars II --> Star Wars I

x = S1_S2[:,1].reshape(len(S1_S2), 1)
y = S1_S2[:,0]

model = LinearRegression().fit(x, y)
intercept = model.intercept_
predict = model.predict(x)
slope = model.coef_
score = model.score(x, y)
'''
SSR = np.sum(np.square(predict - y))
SSE = np.sum(np.square(predict - intercept * np.ones([len(predict), 1])))
COD = SSE / (SSR + SSE)
'''
corr_m = np.corrcoef(x.reshape(1, len(S1_S2)), y)
corr_xy = corr_m[0,1]
r_sq = corr_xy ** 2

RMSE = np.sqrt(metrics.mean_squared_error(y, predict))

print(x.size)
print(slope)
# print(COD)
print(r_sq)
print(RMSE)

''' 
How many users have jointly rated Star Wars I and Star Wars II? 420
What is the beta (not intercept) for predicting Star Wars I ratings from Star Wars II ratings? [0.75475108]
What is the R^2 of the model predicting Star Wars I ratings from Star Wars II ratings? 0.48908573963312224
What is the RMSE of the model predicting Star Wars I ratings from Star Wars II ratings? 0.7981444938340251
'''

#%% Star Wars I --> Titanic

x = S1_T[:,0].reshape(len(S1_T), 1)
y = S1_T[:,1]

model = LinearRegression().fit(x, y)
intercept = model.intercept_
predict = model.predict(x)
slope = model.coef_
score = model.score(x, y)
'''
SSR = np.sum(np.square(predict - y))
SSE = np.sum(np.square(predict - intercept * np.ones([len(predict), 1])))
COD = SSE / (SSR + SSE)
'''
corr_m = np.corrcoef(x.reshape(1, len(S1_T)), y)
corr_xy = corr_m[0,1]
r_sq = corr_xy ** 2

RMSE = np.sqrt(metrics.mean_squared_error(y, predict))

print(x.size)
print(slope)
# print(COD)
print(r_sq)
print(RMSE)

'''
How many users have jointly rated Star Wars I and Titanic? 383
What is the beta (not intercept) for predicting Titanic ratings from Star Wars I ratings? [0.19594435]
What is the R^2 of the model predicting Titanic ratings from Star Wars I ratings? 0.055072460552405764 SUS
What is the RMSE of the model predicting Titanic ratings from Star Wars I ratings? 0.883203731416332
'''

#%% Star Wars I & Star Wars II --> Titanic

x = S1_S2_T[:,:2].reshape(len(S1_S2_T), 2)
y = S1_S2_T[:,2]

model = LinearRegression().fit(x, y)
intercept = model.intercept_
predict = model.predict(x)
slope = model.coef_
score = model.score(x,y)

# print(S1_S2_T.shape[0])
print(score)
'''
How many users have jointly rated all 3 movies - Star Wars I Star Wars II and Titanic? 355
What is the R^2 of the model predicting Titanic ratings from Star Wars I and Star Wars II ratings at the same time? 0.05915478611202318
'''