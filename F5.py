# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 13:44:24 2021

@author: sunny

Function assumes inputs of the dataset as a numpy array
    dataset parameter only has one column of a sample of an underlying distribution
And mass bounds parameter 
    as a real number between 0.01 and 99.99
Function returns two variables
    the first is the lower bound of the sample distribution
    the second is the upper bound of the sample distribution
    both returned variables are unrounded
"""

import numpy as np

def empericalSmapleBounds(data_input, mass_bounds):

    data = np.sort(data_input)

    length = data.size

    entry_per_percentile = 0.01 * length

    tail_mass = (100 - mass_bounds) / 2
    upper_tail = 100 - tail_mass
    lower_tail = tail_mass
    
    upper_index = int(entry_per_percentile * upper_tail - 1)
    lower_index = int(entry_per_percentile * lower_tail - 1)
    
    return data[lower_index], data[upper_index]

''' # for testing purposes:
print(empericalSmapleBounds(np.genfromtxt('sampleInput1.csv'), 95))
print(empericalSmapleBounds(np.genfromtxt('sampleInput1.csv'), 99))
print(empericalSmapleBounds(np.genfromtxt('sampleInput1.csv'), 50))

print(empericalSmapleBounds(np.genfromtxt('sampleInput2.csv'), 95))
print(empericalSmapleBounds(np.genfromtxt('sampleInput2.csv'), 99))
print(empericalSmapleBounds(np.genfromtxt('sampleInput2.csv'), 50))
'''