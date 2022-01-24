# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 00:17:42 2021

@author: sunny
"""

import numpy as np
from scipy import stats
import pandas as pd

data = pd.read_csv('movieReplicationSet.csv')
data = data.iloc[:,:400]
# print(data['Star Wars: Episode 1 - The Phantom Menace (1999)'])

all_three = []

for col, row in data.iterrows():
    if not pd.isna(row['Kill Bill: Vol. 1 (2003)']) and not pd.isna(row['Kill Bill: Vol. 2 (2004)']) and not pd.isna(row['Pulp Fiction (1994)']):
        all_three.append([row['Kill Bill: Vol. 1 (2003)'], row['Kill Bill: Vol. 2 (2004)'], row['Pulp Fiction (1994)']])

all_three = np.array(all_three)
kill_bill_1 = all_three[:,0]
kill_bill_2 = all_three[:,1]
pulp_fiction = all_three[:,2]

#%% Question 1 How many users have rated all 3 of these movies?
print(all_three.shape) # (238, 3)
print(kill_bill_1.shape)

#%% Question 2 Doing a paired samples t-test between ratings from Kill Bill 2 and Pulp Fiction, what is the absolute t-value?
t1, p1 = stats.ttest_rel(pulp_fiction, kill_bill_2)

print(t1, p1) # 1.2364948550927515 0.2174986340345261

#%% Question 3 Doing a paired samples t-test between ratings from Kill Bill 1 and Kill Bill 2, what is the p-value and what should you decide re significance?

t2, p2 = stats.ttest_rel(kill_bill_1, kill_bill_2)
print(t2, p2) # 1.4739760809411913 0.14181503833524034

#%% Question 4 Doing an independent samples t-test between ratings from Kill Bill 2 and Pulp Fiction, what is the absolute t-value?

t3, p3 = stats.ttest_ind(pulp_fiction, kill_bill_2)
print(t3, p3) # 0.83201193765794 0.4058211698544758

#%% Question 5 What is the mean rating of Pulp Fiction in this population (of people who have rated all 3 movies)?

mean_pulp_fiction = pulp_fiction.mean()
print(mean_pulp_fiction) # 3.2752100840336134

#%% Question 6 Doing a paired samples t-test between ratings from Kill Bill 1 and Kill Bill 2, what is the absolute t-value?

t6, p6 = stats.ttest_rel(kill_bill_1, kill_bill_2)
print(t6, p6) # 1.4739760809411913 0.14181503833524034

#%% Question 7 Doing an independent samples t-test between ratings from Kill Bill 1 and Kill Bill 2, what is the absolute t-value?

t7, p7 = stats.ttest_ind(kill_bill_1, kill_bill_2)
print(t7, p7) # 0.6712552299230066 0.502384929498441

#%% Question 8 Doing an independent samples t-test between ratings from Kill Bill 1 and Kill Bill 2, what is the p-value and what should you decide re significance?

t7, p7 = stats.ttest_ind(kill_bill_1, kill_bill_2)
print(t7, p7) # 0.6712552299230066 0.502384929498441

#%% Question 9 What are the degrees of freedom for a *paired samples* t-test between Kill Bill 1 and Kill Bill 2 (using the same population of people who have rated all 3 movies)?

