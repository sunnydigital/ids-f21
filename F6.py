# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 11:19:06 2021

@author: sunny

i. Assumes inputs of 1) a 1D or 2D numpy array 
    iA. If 2D will be of a "m by 2" array where 
         iii. variables are in the columns, and numbers/measures in the rows
    iB. Columns will be of equal length
ii. A flag for the parameter where:
    1. is the mean
    2. is the standard deviation
    3. is the correlation
iii. The window size is a subset of how many numbers of the dataset to calculate the parameter indicated in 'flag.' over
iv. Further assumes window size will always be smaller than array to calculate function on
    ivA. will also assume the input array will always be 2D if calculating correlation and
    ivB. 1D if calculating for mean or std
v. Outputs the calculated variables and returns a list containing values
Note: std function calculates sample standard deviation (without implementing degrees of freedom)
"""

import numpy as np
# For testing purposes
A = [1,3,5,7,9]# np.genfromtxt('outputArrayExample50.csv')
B = np.transpose([[1,3,5,7,9],[1,2,4,3,5]])
C = np.genfromtxt('inputArrayExample.csv', delimiter=',')
C50 = np.genfromtxt('outputArrayExample50.csv')
C100 = np.genfromtxt('outputArrayExample300.csv')

def slidWinDescStats(arr, flag, window):
    ''' # For testing purposes
    def mean(arr):
        summ = 0
        count = 0
        for entry in arr:
            if np.isnan(entry):
                continue
            summ += entry
            count += 1
        mean = summ / count
        return mean

    def std(arr):
        std_mean = mean(arr)
        summ = 0
        count = 0
        for entry in arr:
            if np.isnan(entry):
                continue
            summ += (entry - std_mean) ** 2
            count += 1
        return (summ / count) ** 0.5

    def corr(arr1, arr2):
        corr_mean_1 = mean(arr1)
        corr_mean_2 = mean(arr2)
        corr_std_1 = std(arr1)
        corr_std_2 = std(arr2)
        
        summ = 0
        for index in range(len(arr1)):
            if np.isnan(arr1[index]) or np.isnan(arr2[index]):
                continue
            summ += (arr1[index] - corr_mean_1) * (arr2[index] - corr_mean_2)
            
        return summ / (corr_std_1 * corr_std_2)
    '''
    if flag == 1: # Section for setting flag as mean
        length = len(arr) # Initializes length as array length
        ret_arr = np.array([]) # Creates empty array to return with added values
        
        start = 0 # Initializes counter
        while start + window <= length: # While end less than length of array
            subset = arr[start:start+window] # Creates subset of array to cycle through
            ret_arr = np.append(ret_arr, np.mean(subset)) # Adds calculated mean to return array
            start += 1 # Adds to counter
            
        return ret_arr

    if flag == 2: # Section for calculating flag as population standard deviation
        length = len(arr) # Initializes length as array length
        ret_arr = np.array([]) # Creates empty array to return with added values
        
        start = 0 # Initializes counter
        while start + window <= length: # While end less than length of array
            subset = arr[start:start+window] # Creates subset of array to cycle through
            ret_arr = np.append(ret_arr, np.std(subset)) # Adds calculated standard deviation to return array
            start += 1 # Adds to counter
            
        return ret_arr

    if flag == 3: # Section for calculating 
        length = len(arr) # Initializes counter
        ret_arr = np.array([]) # Creates subset of array to cycle through

        start = 0 # Initializes counter
        while start + window <= length: # While end less than length of array
            subset = arr[start:start+window] # Creates subset of array to cycle through
            ret_arr = np.append(ret_arr, np.corrcoef(np.transpose(subset))[0,1]) # Adds calculated correlation coefficient to return array
            start += 1 # Adds to counter
            
        return ret_arr
    
# For testing purposes
'''
print(slidWinDescStats(A, 2, 3))
print(slidWinDescStats(A, 2, 4))
print(slidWinDescStats(B, 3, 3))
print(slidWinDescStats(B, 3, 4))
'''

# print(len(B)) # For testing purposes
# print(np.corrcoef(np.transpose(B))[0,1])

# print(B)
# np.transpose(B)
# print(B)
# print(B[0:3])

# print(np.corrcoef(np.transpose(B))[0,1])

# slidWinDescStats(B, 3, 4)