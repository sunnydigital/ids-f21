# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:52:01 2021

@author: sunny
"""
import pandas as pd
from scipy import stats
import numpy as np

'''
data = gft('movieReplicationSet.csv', delimiter = ',')
columns = data[0,:]
index = ["Subject " + str(s+1) for s in data.shape(0)]

df = pd.DataFrame(data = data[1:-1,:], index = index, columns = columns)

print(df.head())
'''

data = pd.read_csv('movieReplicationSet.csv')

# print(data.head(10))

means = data.iloc[:,:400].mean(axis=0)
# print(means.sort_values(ascending=False))
# print(means.idxmax())
# print(means.idxmin())

medians = data.iloc[:,:400].median(axis=0)
# print(medians.sort_values(ascending=False))

modes = data.iloc[:,:400].mode(axis=0)
# print(modes["Independence Day (1996)"])

# mean_of_means = means.mean(axis=0)
# print(mean_of_means)


data1 = np.genfromtxt('movieReplicationSet.csv',delimiter=',',skip_header=1)

mean_arr = np.nanmean(data1[:,:400],axis=0)
print(mean_arr)

median_arr = np.nanmedian(data1[:,:400],axis=0)
print(median_arr)

modal_arr = stats.mode(data1[:,:400],axis=0)
print(modal_arr)

mean_of_means = np.nanmean(mean_arr)
print(mean_of_means)