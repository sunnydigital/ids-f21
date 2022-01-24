# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:53:16 2021

@author: sunny
v1.0.0

Program to find the emperical discrete random variable
Function assumes input of the location (name included) of a csv file composed of 
    real numbers separated by newlines
Returns two objects, the first being an numpy.ndarray (2D array) of numpy.float64 objects
    while the second object is the first moment, or EV of the entered list of numbers in numpy.float64 format

Q: What kind of output data type do we need?
A: Needs to output as numpy array
"""

import numpy as np

writtenBy = "Sunny Son"

def empiricalRV(locationName):
    # Opens csv file and loads into array
    with open(locationName) as csvfile:
        dataset = list(np.loadtxt(csvfile))
    
    # Creates a dictionary of value : occurrences
    valOccur = {}
    for entry in dataset:
        if entry in valOccur.keys():
            valOccur[entry] += 1
        else:
            valOccur[entry] = 1
    
    # Finds the sum of occurrences
    totalOccur = sum(valOccur.values())
    
    # Creates a new dictionary with value : frequency
    valProb = {}
    for key in valOccur:
        valProb[key] = valOccur[key]/totalOccur
    
    # Sorts the value : frequency dictionary by order of value
    # TODO look up why this works, sorted arguments and lambda implementation
    sortedValProb = sorted(valProb.items(), key = lambda kv: kv[0])
    sortedValProb = np.array(sortedValProb)

    # Finds expected value from the key, value pairs
    expectedVal = 0
    for key, value in valProb.items():
        expectedVal += key * value
    
    return sortedValProb, expectedVal

# For testing purposes
### Please give me a 10 Sara! Haha jk.. Unless..?

"""
output1, output2 = empiricalRV("testData.csv")
output3 = output1[25][0] + output1[34][1]
print(type(output1[0][0]))
print(output1)
print(output2)
print(output3)
"""