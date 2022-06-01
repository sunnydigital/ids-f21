# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:44:10 2021

@author: sunny
"""
import numpy as np
# from statsmodels import robust
from numpy import nanmean, absolute
import pandas as pd

data1 = np.genfromtxt('movieReplicationSet.csv',delimiter=',',skip_header=1)

mean_arr = np.nanmean(data1[:,:400],axis=0)
# print(mean_arr)

median_arr = np.nanmedian(data1[:,:400],axis=0)
# print(median_arr)

# modal_arr = stats.mode(data1[:,:400],axis=0)
# print(modal_arr)

mean_of_means = np.nanmean(mean_arr)
# print(mean_of_means)

std_all = np.nanstd(data1,axis=0)
# print(std_all)

mean_std_all = np.nanmean(std_all)
# print(mean_std_all)
# 1.0555420434356373

median_std_all = np.nanmedian(std_all)
# print(median_std_all)
# 1.0687823330600204

def mad(data, axis=None):
    return nanmean(absolute(data[~np.isnan(data).any()] - nanmean(data,axis)), axis)

mean_mad_all = []

for array in data1[:][:400]:
    np.append(mean_mad_all, np.nanmean(mad(array,0)))
print(mean_mad_all)

corr_avg_all = np.corrcoef(data1[:,:400],data1[:,:400])
# print(corr_avg_all)

'''
def mead(data,axis=None):
    return nanmean(absolute(data - nanmedian(data,axis)), axis)
'''

median_mad_all = np.nanmedian(mad(data1,axis=0))
# print(median_mad_all)

# median of MAD is 0.858
# mean of MAD is 0.852
# correlation 0.39

data = pd.read_csv('movieReplicationSet.csv')

# print(data.head(10))

data = data.iloc[:,:400]

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

mad = data.iloc[:,:400].mad(axis=0)

mean_mad_all_pd = mad.mean()
# print(mean_mad_all_pd)
# 0.8519316014154186

median_mad_all_pd = mad.median()
# print(median_mad_all_pd)
# 0.8576626878081213

corr_matrix = data.corr()
# print(corr_matrix)

# print(corr_matrix.mean(axis=0).mean())
# 0.39028621339553043