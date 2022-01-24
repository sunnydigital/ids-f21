# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 00:06:09 2021

@author: sunny

v1.0.0

Assumes an input of a **2D Numpy Array ONLY**
Calculates the Normalized Error to the given power and root
    Assuming two input parameters:
        One being a m (row) by 2 (column) numpy array
            this array has a first column being the yHat predicted values and the decond being the y values being predicted
        The other being an integer to calculate the nth power/root of the Normalized Error
    Returns the Nth Normalized Error as a float/integer
"""
import numpy as np # imports numpy to use

# used for testing
A = np.array([np.array([1,2,3,4,5]), np.array([2,4,1,6,2])])
A = np.transpose(A)

B = np.array([np.array([0,10,5]),np.array([50,5,10])])
B = np.transpose(B)



def normalizedError(array, power): # defines function
    
    sum = 0 # initializes sum variable
    n = array.shape[0] # initializes n to divide by later as m (rows)
    
    for entry in array: # starts iterator as each entry in array
        
        sum += np.absolute(entry[0] - entry[1]) ** power # adds to sum the square of the absolute value of the first column of entered array minus the second column
    
    average_sum = sum / n # calculates the average of the sum of values
    
    root_average_sum = average_sum ** (1 / power) # calculates for the nth root of the average sum
    
    return root_average_sum # returns value

print(normalizedError(B,3))