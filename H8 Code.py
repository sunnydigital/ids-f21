# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 08:33:16 2021

@author: sunny
"""
import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_csv('Sadex1.csv', names=('BDI', 'placebo'))
treated = []
not_treated = []


for col, row in data.iterrows():
    if row['placebo'] == 0:
        not_treated.append(row['BDI'])
    else:
        treated.append(row['BDI'])

treated = pd.DataFrame(treated)
not_treated = pd.DataFrame(not_treated)
#%% Question 1 What is the difference in the sample means of the two groups?
mean_dif = treated.mean() - not_treated.mean()
print(mean_dif)

#%% Question 2 How many degrees of freedom does the t-distribution of the suitable significance test have in this case?
# 30 + 30 - 2

#%% Question 13 How many people are in *each* treatment group of this experiment?
# 30

#%% Question 14 What is the p-value resulting from doing a suitable significance test in this case?
t, p = stats.ttest_ind(treated, not_treated)
print(t, p) # [-1.27376269] [0.20782839]

#%% Question 15 With these results, we conclude that
# We have no evidence to believe that the drug works because p > 0.05

#%% Question 16 We are concerned that large differences in the depression scores of the individuals within the two groups might have obscured the potential effectiveness of the drug. To alleviate this, we ran another small study where we measure the depression scores of people before (Column 1) or after (Column 2) they received Sadex. The results are reported in "Sadex2.csv".
# How many participants are part of this new study in total?
data2 = pd.read_csv('Sadex2.csv', names=('control', 'treatment'))
print(data2.shape)

#%% Question 17 What is the difference in the sample means of the two groups?
control_m = data2.iloc[:,0].mean()
treatment_m = data2.iloc[:,1].mean()

print(control_m - treatment_m)

#%% Question 18 With the results from this study, we conclude that (pick the strongest statement you can justifiably make, given the data)

t, p = stats.ttest_rel(data2.iloc[:,0], data2.iloc[:,1])
print(t, p)

#%% Question 19 Just to be sure, you run another test with a larger sample. You are confident that the drug works and that you have enough people in the study to show this, so you again run a design where people who are depressed are randomly assigned to conditions, either receiving (1 in Column 2) or not receiving (0 in Column 2) Sadex. Depression scores are in V1. This data is reported in "Sadex3.csv"
# With the results from this study, we conclude that
data3 = pd.read_csv('Sadex3.csv', names=('BDI', 'placebo'))
treated = []
not_treated = []

for col, row in data3.iterrows():
    if row['placebo'] == 0:
        not_treated.append(row['BDI'])
    else:
        treated.append(row['BDI'])

treated = pd.DataFrame(treated)
not_treated = pd.DataFrame(not_treated)

t, p = stats.ttest_ind(not_treated, treated)
print(t, p) # [-2.23852148] [0.02642623]

#%% Question 20 Finally, you want to harness the power of a repeated measures design, so you run it with a new sample of depressed people, before (Column 1) or after (Column 2) giving them Sadex. This data is reported in "Sadex4.csv"
# Note: Clinical significance means that there is a reduction of at least 5 points in the depression score of depressed individuals after receiving the drug.
# What do you conclude about the drug?

data4 = pd.read_csv('Sadex4.csv', names=('before', 'after'))

control_m = data4.iloc[:,0].mean()
treatment_m = data4.iloc[:,1].mean()

print(control_m - treatment_m)

t,p = stats.ttest_rel(data4['before'], data4['after'])
print(t, p)