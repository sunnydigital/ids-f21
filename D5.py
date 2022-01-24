# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:30:38 2021

@author: sunny
"""
import numpy as np
from scipy import stats as st
import pandas as pd

data = pd.read_csv('movieReplicationSet.csv', delimiter=',')
data = data.iloc[:,:400]

means = data.mean(axis=0, skipna=1)
means_asc = means.sort_values

sem = data.sem(axis=0, skipna=1)

CI_sorted = []
for label, value in means.iteritems():
    CI = st.norm.interval(0.95, loc=means[label], scale=sem[label])
    absol = np.absolute(CI)[0]
    CI_sorted.append([label, CI, absol])

CI_sorted = pd.DataFrame(CI_sorted)
CI_sorted.columns = ['Title', 'Confidence Interval', 'Absolute CI']
CI_sorted = CI_sorted.sort_values(by=['Absolute CI'])

df_mean = means.mean()
# print(df_mean)

df_list = []
for col, row in data.iterrows():
    for index, entry in row.iteritems():
        df_list.append(entry)

df_arr = np.array(df_list)
df_arr = df_arr[~np.isnan(df_arr)]

all_sem = st.sem(df_arr)
all_mean = np.mean(df_arr)

# print(df_mean)
# print(CI_sorted)
# print(all_sem)
#%% What is the 95% CI for the mean rating of "The Life of David Gale (2003)"?

name = 'The Life of David Gale (2003)'
CI = st.norm.interval(0.95, loc=means[name], scale=sem[name])
print(means[name])
print(CI-np.ones(2)*means[name])

'''
2.151315789473684
[-0.26219944  0.26219944]
'''

#%% What is the 99% CI for the mean rating of "Cocktail (1988)"?

name = 'Cocktail (1988)'
CI = st.norm.interval(0.99, loc=means[name], scale=sem[name])
print(means[name])
print(CI-np.ones(2)*means[name])

'''
2.125
[-0.34987556  0.34987556]
'''

#%% What is the 99% CI for the mean rating of "Saving Private Ryan (1998)"?

name = 'Saving Private Ryan (1998)'
CI = st.norm.interval(0.99, loc=means[name], scale=sem[name])
print(means[name])
print(CI-np.ones(2)*means[name])

'''
3.140877598152425
[-0.11204062  0.11204062]
'''

#%% "Memento (2000)" is a significantly better movie than average (at 99% confidence)

name = 'Memento (2000)'
CI = st.norm.interval(0.99, loc=means[name], scale=sem[name])
print(CI)
print(df_mean)
'''
(2.96994009092893, 3.292990943553829)
2.634619386670867
'''

#%% What is the 95% CI for the mean rating of "Anger Management (2002)"?

name = 'Anger Management (2002)'
CI = st.norm.interval(0.95, loc=means[name], scale=sem[name])
print(means[name])
print(CI-np.ones(2)*means[name])
'''
2.5024271844660193
[-0.13927746  0.13927746]
'''

#%% "Traffic (2000)" is a significantly worse movie than average (at 99% confidence)

name = 'Traffic (2000)'
CI = st.norm.interval(0.99, loc=means[name], scale=sem[name])
print(CI)
print(df_mean)

'''
(2.0064020871607444, 2.6759508540157264)
2.634619386670867
'''

#%% What is the 99% CI for the mean rating of "Billy Madison (1995)"?

name = 'Billy Madison (1995)'
CI = st.norm.interval(0.99, loc=means[name], scale=sem[name])
print(means[name])
print(CI-np.ones(2)*means[name])

'''
2.4927536231884058
[-0.1814138  0.1814138]
'''

#%% "From Hell (2001)" is a significantly worse movie than average (at 95% confidence)

name = 'From Hell (2001)'
CI = st.norm.interval(0.95, loc=means[name], scale=sem[name])
print(CI)
print(df_mean)
'''
(1.8501762860030182, 2.3202782594515274)
2.634619386670867
'''

#%% What is the 95% CI for the mean rating of "Stir Crazy (1980)"?

name = 'Stir Crazy (1980)'
CI = st.norm.interval(0.95, loc=means[name], scale=sem[name])
print(means[name])
print(CI-np.ones(2)*means[name])

'''
2.194915254237288
[-0.30433883  0.30433883]
'''

#%% What is the 95% CI for the mean rating of "McArthur (1977)"?

name = 'MacArthur (1977)'
CI = st.norm.interval(0.95, loc=means[name], scale=sem[name])
print(means[name])
print(CI-np.ones(2)*means[name])

'''
2.1147540983606556
[-0.28279758  0.28279758]
'''