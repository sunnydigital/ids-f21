# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:14:27 2021

@author: sunny
"""

import numpy as np
import random as rd
import pandas as pd

data = pd.read_csv('movieRatingsDeidentified.csv')

pulp_fiction = data['Pulp Fiction (1994)']
magnolia = data['Magnolia (1999)']

reservoir_dogs = data['Reservoir Dogs (1992)']
good_will_hunting = data['Good Will Hunting (1997)']

saving_private_ryan = data['Saving Private Ryan (1998)']

zoolander = data['Zoolander (2001)']

unforgiven = data['Unforgiven (1992)']
big_fish = data['Big Fish (2003)']

mulholland_dr = data['Mulholland Dr. (2001)']

def row_removal(df1, df2):
    removed = []
    for col, row in pd.concat([df1, df2], axis=1).iterrows():
        if not pd.isna(row[0]) and not pd.isna(row[1]):
            removed.append([row[0], row[1]])
    return pd.DataFrame(removed, columns=[df1.name, df2.name])

def element_removal(df):
    removed = []
    for index, item in df.iteritems():
        if not pd.isna(item):
            removed.append(item)
    return pd.DataFrame(removed, columns=[df.name])

def permutation_test(df1, df2, num_reps):
    comb_df = row_removal(df1, df2)
    
    comb_df1 = comb_df.iloc[:,0]
    comb_df2 = comb_df.iloc[:,1]
    
    test_stat = comb_df1.mean() - comb_df2.mean()
    
    joint_data = pd.concat((comb_df1, comb_df2))
    
    n1 = comb_df1.size
    n2 = joint_data.size

    shuffled_stats = np.empty([num_reps,1])
    shuffled_stats[:] = np.NaN
    
    for i in range(num_reps):
        shuffled_indices = np.random.permutation(n2)
        shuffled_group1 = joint_data.iloc[shuffled_indices[:n1]]
        shuffled_group2 = joint_data.iloc[shuffled_indices[n1:]]
        shuffled_stats[i,0] = np.mean(shuffled_group1) - np.mean(shuffled_group2)
    
    temp1 = np.argwhere(shuffled_stats > test_stat)
    temp2 = len(temp1)
    
    exact_p = temp2/len(shuffled_stats)
    
    return exact_p

def bootstrapping(df, test_stat, confidence, num_reps):
    sample_means = df.mean()
    
    values_list = df.values.tolist()
    
    
    '''
    n = df.size
    
    tych_means = np.empty([num_reps, 1])
    tych_means[:] = np.NaN
    
    tych_indices = np.random.randint(0,n,[num_reps,num_reps])
    
    for i in range(num_reps): # loop through each repeat
        temp_indices = tych_indices[:,i] # indices for this iteration
        tych_means[i] = np.mean(df[temp_indices]) # compute the mean
    '''

#%% Weekly salary question
weekly_earn = [200, 400, 600, 800, 1000]

salaries = [np.sum(rd.choices(weekly_earn, k=26)) for i in range(100000)]

print(np.mean(salaries))
print(np.percentile(salaries, 22))

#%%

M1 = np.array(mulholland_dr).transpose()

temp = np.array([np.isnan(M1)],dtype=bool)
temp2 = temp*1 # convert boolean to int
temp2 = sum(temp2) # take sum of each participant
missingData = np.where(temp2>0) # find participants with missing data
combinedData = np.delete(M1,missingData) # delete missing data from array

sampleMeans = np.mean(combinedData,axis=0) 
# These are the real means. We get that straight up from the sample itself.
# So what we do we get from the resampling?

numRepeats = int(1e4) # How many times do we want to resample the 1 empirical
# sample we have?
nSample = len(combinedData) # Number of data points in the sample

# Preallocate what will contain the bootstrapped sample means:
tychenicMeans = np.empty([numRepeats,1])
tychenicMeans[:] = np.NaN

# Draw integers - which we'll use as indices, num_repeats times:
tychenicIndices = np.random.randint(0,nSample,[numRepeats,numRepeats])
# Draw random numbers from 0 to n_sample (not inclusive), to yield an array
# with dimensions that are num_repeats x num_repeats (10000 x 10000)

# Estimate the stability of the sample mean for which movie?:
for i in range(numRepeats): # loop through each repeat
    tempIndices = tychenicIndices[:,i] # indices for this iteration
    tychenicMeans[i] = np.mean(combinedData[tempIndices]) # compute the mean

# How good is our estimate of the empirical sample mean as the mean of the
# resampled tychenic means? 
estimateOffset = np.mean(tychenicMeans) - np.mean(combinedData)

# How do the tychenic sample means distribute? How tight is this distribution? 
# Could the estimate reasonably have been +/- 0.1 from the real sample mean?
import matplotlib.pyplot as plt
numBins = 101
plt.hist(tychenicMeans,numBins)
plt.xlabel('Tychenic sample means')
plt.ylabel('Count')

# Add the sample mean:
plt.plot([np.mean(combinedData),np.mean(combinedData)],[0,400],color='black',linewidth=0.5)

confidenceLevel = 95 # What confidence level (probability of containing 
# the empirical mean) is desired? Also try 99%
lowerBoundPercent = (100 - confidenceLevel)/2 # lower bound
upperBoundPercent = 100 - lowerBoundPercent # upper bound
lowerBoundIndex = round(numRepeats/100*lowerBoundPercent)-1 # what index?
upperBoundIndex = round(numRepeats/100*upperBoundPercent)-1 # what index?
sortedSamples = np.sort(tychenicMeans,axis=0)
lowerBound = sortedSamples[lowerBoundIndex] # What tychenic value consistutes the lower bound?
upperBound = sortedSamples[upperBoundIndex] # What tychenic value consistutes the upper bound?

# Add it to the plot:
numBins = 101
plt.hist(tychenicMeans,numBins)
plt.xlabel('Tychenic sample means')
plt.ylabel('Count')
plt.plot([np.mean(combinedData),np.mean(combinedData)],[0,400],color='black',linewidth=0.5)
plt.plot([lowerBound,lowerBound],[0,400],color='red',linewidth=0.5) 
plt.plot([upperBound,upperBound],[0,400],color='red',linewidth=0.5) 

#%% Question 13 You work for a movie studio and want to know whether viewers perceive "Pulp Fiction" (1994) as a significantly better movie than "Magnolia" (1999). To determine this, you use a permutation test, utilizing row-wise removal of missing data and as a test statistic, you define "Tyche's C" as the average difference in ratings (Pulp Fiction rating minus Magnolia rating). Given this approach, the statement that is best supported by the data is that

# print(row_removal(pulp_fiction, magnolia))
# print(element_removal(saving_private_ryan))
# permutation_test(reservoir_dogs, good_will_hunting)
print(permutation_test(pulp_fiction, magnolia, 10000))
print(permutation_test(unforgiven, big_fish, 10000))
print(permutation_test(reservoir_dogs, good_will_hunting, 10000))

#%% 
import random
random.seed()

#%%
money = [100, 200, 300, 400, 500]
rent_count = 0
iterations = int(100000)

#%%
for idx in range(iterations):
    temp = []
    for i in range(52):
        temp.append(money[random.randint(0,4)])
    if (sum(temp) >= 14400):
        rent_count += 1
        
print(rent_count/iterations)