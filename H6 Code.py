# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:18:50 2021

@author: sunny
"""

import numpy as np
## import pandas as pd
## import sys
from sklearn.linear_model import LinearRegression


## np.set_printoptions(threshold=np.inf)


## kepler = pd.read_csv("kepler.csv", names = ["Caste (1 to 5)", "Intelligence (AIQ)", "Brain mass (g)", "Hours worked per week", "Annual Income (credits)"])

data = np.genfromtxt('kepler.csv',delimiter=',')

#%% Question 1
## Correlation between caste and IQ
## corr_matrix = kepler.corr()

## pd.set_option("display.max_rows", None, "display.max_columns", None)
## print(corr_matrix)
## 0.672687

data = data.transpose()
r1 = np.corrcoef(data)
print(r1[0,1]) # 0.6726866924078111 correct

data = data.transpose()

#%% Question 2
# Regressing caste and brain mass
x1 = data[:,2].reshape(len(data),1)
y1 = data[:,0]

model1 = LinearRegression().fit(x1, y1)

slope = model1.coef_
intercept = model1.intercept_
yHat = slope * x1 + intercept
residuals1 = y1 - yHat.flatten()

# Regressing IQ and brain mass
x2 = data[:,2].reshape(len(data),1)
y2 = data[:,1]

model2 = LinearRegression().fit(x2, y2)

slope = model2.coef_
intercept = model2.intercept_
yHat = slope * x2 + intercept
residuals2 = y2 - yHat.flatten()

# print(residuals2)
# now correlating residuals

partial_corr = np.corrcoef(residuals1,residuals2)
print(partial_corr) # -0.03401872 correct: 0

#%% Question 3
# need to calculate r^2 = SSE / SSE + SSR

x = data[:,2].reshape(len(data),1)
y = data[:,1]

model = LinearRegression().fit(x, y)

slope = model.coef_ # Same goes for B1 (slope)
intercept = model.intercept_ # And B0 (intercept)
yHat = slope * x + intercept
residuals = y - yHat.flatten()

# predict = model.predict(x)
# residuals = y - predict
# intercept = model.intercept_

corr_m = np.corrcoef(x.reshape(1, len(x)), y)
corr_xy = corr_m[0,1]
r_sq = corr_xy ** 2

'''
explained = [entry - intercept for entry in predict] 

# SSR = sum(map(lambda x: x*x, residuals3))
SSR = np.sum(np.square(residuals))
# SSE = sum(map(lambda x: x*x, explained3))
SSE = np.sum(np.square(explained))

COD = SSE/(SSR + SSE)
'''

# print(COD) # 0.9339264360889333 ????
print(r_sq) # 0.6843730168538517 correct
#%% Question 4
x = data[:,2].reshape(len(data),1)
y = data[:,1]

model = LinearRegression().fit(x, y)
predict = model.predict([[3000]])

print(predict) # 125.02207053 # 124 correct

#%% Question 5
income = data[:,4]
caste = data[:,0]

income_caste_corr = np.corrcoef(income, caste)

print(income_caste_corr) # 0.38769367 correct

#%% Question 6
x = data[:,1].reshape(len(data),1)
y = data[:,0]

model = LinearRegression().fit(x, y)
predict = model.predict(x)
residuals1 = y - predict

x = data[:,1].reshape(len(data),1)
y = data[:,4]

model = LinearRegression().fit(x, y)
predict = model.predict(x)
residuals2 = y - predict

corr1 = np.corrcoef(residuals1, residuals2)

x = data[:,3].reshape(len(data),1)
y = data[:,0]

model = LinearRegression().fit(x, y)
predict = model.predict(x)
residuals1 = y - predict

x = data[:,3].reshape(len(data),1)
y = data[:,4]

model = LinearRegression().fit(x, y)
predict = model.predict(x)
residuals2 = y - predict

corr2 = np.corrcoef(residuals1, residuals2)
print(corr1 + corr2) # 0.43409707 correct: 0
#%% Question 6a
x = data[:,[1,3]].reshape(len(data),2)
y = data[:,0]

model1 = LinearRegression().fit(x,y)
predict1 = model1.predict(x)
residuals1 = y - predict1

x = data[:,[1,3]].reshape(len(data),2)
y = data[:,4]

model2 = LinearRegression().fit(x,y)
predict2 = model2.predict(x)
residuals2 = y - predict2

corr_m = np.corrcoef(residuals1, residuals2)
print(corr_m) # -0.01462991
#%% Question 7
x = data[:,1].reshape(len(data),1)
y = data[:,4]

model = LinearRegression().fit(x, y)
predict = model.predict(x)
intercept = model.intercept_

corr_m = np.corrcoef(x.reshape(1, len(x)), y)
corr_xy = corr_m[0,1]
r_sq1 = corr_xy ** 2

'''
residuals = y - predict
explained = [entry - intercept for entry in predict]

SS_r = np.sum(np.square(residuals))
SS_e = np.sum(np.square(explained))

COD7 = SS_e / (SS_r + SS_e) # 0.7480556995855387
'''
# print(COD7)
print(r_sq1) # 0.16151791873588173 correct
#%% Question 8
x = data[:,3].reshape(len(data),1)
y = data[:,4]

model = LinearRegression().fit(x, y)
predict = model.predict(x)
intercept = model.intercept_

corr_m = np.corrcoef(x.reshape(1, len(x)), y)
corr_xy = corr_m[0,1]
r_sq2 = corr_xy ** 2
'''
residuals = y - predict
explained = [entry - intercept for entry in predict]

SS_r = np.sum(np.square(residuals))
SS_e = np.sum(np.square(explained))

COD8 = SS_e / (SS_r + SS_e)
'''
# print(COD8) # 0.9255694821624909
print(r_sq2) # 0.67209454030374 correct

#%% Question 9
# COD9 = COD7 + COD8

# print(COD9)
# print(r_sq1) # 0.8336124590396218 correct
# print(r_sq2) 

# print(r_sq1 + r_sq2)

x = data[:,[1,3]].reshape(len(data),2)
y = data[:,4]

model = LinearRegression().fit(x, y)
predict = model.predict(x)
intercept = model.intercept_
score = model.score(x,y)

print(score)
#%% Question 10
x = np.array(data[:,[1,3]]).reshape(len(data),2)
y = data[:,4]

model = LinearRegression().fit(x, y)
predict = model.predict([[120, 50]])

print(predict) # 702.45856022 ???? correct: 884