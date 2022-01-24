# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 00:32:45 2021

@author: sunny
v1.0.0

Program to find the median absolute deviation
Function assumes input of the location (name included) of a csv file composed of 
    real numbers separated by newlines which are consecutive and have no breaks in between
Returns the median absolute deviation of the input array of numbers

Q: What kind of output data type do we need?
A: Needs to output as numpy array
"""

writtenBy = 'Sunny Son'
# importing numpy, which will be used
import numpy as np
# Defining the function
def medAbsDev(locationName):
    # Input the data
    data = np.genfromtxt(locationName)
    # Generated the median of the data
    median = np.nanmedian(data)
    # Initializes an empty numpy array to store absolute values of value - median
    abs_dev = np.array([])
    for entry in data: # Loops through data input
        if np.isnan(entry): # Tests for emptiness; if so will skip
            continue
        abs_dev = np.append(abs_dev, np.absolute(entry - median)) # Appends the value (entry) - median to an array
        
    return np.nanmedian(abs_dev) # Returns the value of the median of the absolute median array