# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:08:48 2021

@author: sunny
"""

import pandas as pd
import numpy as np
from numpy import mean, absolute

data = np.genfromtxt('corporateSales.csv',delimiter=',')

median_violations = np.nanmedian(data[:,2])
print(median_violations)

corr_IQ_custComplaint = np.corrcoef(data[:,0],data[:,1])
print(corr_IQ_custComplaint)

std_ethical_violations = np.nanstd(data[:,2])
print(std_ethical_violations)

median_IQ = np.nanmedian(data[:,0])
print(median_IQ)

median_complaints = np.nanmedian(data[:,1])
print(median_complaints)

corr_IQ_violation = np.corrcoef(data[:,0],data[:,2])
print(corr_IQ_violation)

def mad(data,axis=None):
    return mean(absolute(data - mean(data, axis)), axis)

mad_customer_complaint = mad(data[:,1])
print(mad_customer_complaint)

mean_IQ = np.nanmean(data[:,0])
print(mean_IQ)

std_IQ = np.nanstd(data[:,0])
print(std_IQ)

corr_custCompl_ethicalVio = np.corrcoef(data[:,1],data[:,2])
print(corr_custCompl_ethicalVio)