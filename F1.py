# -*- coding: utf-8 -*-
import sys
"""
Created on Wed Sep 15 21:32:26 2021

@author: sunny
Function to calculate conditional probability given two inputs
    P(A and B) between 0 and 1 (inclusive) and less than probA as variable jointProb
    P(A) between 0 (exclusive) and 1 (inclusive) as variable probA
"""

writtenBy = "Sunny Son"

def condProbCalc(jointProb,probA):
    if jointProb > 1 or jointProb < 0:
        sys.exit("Probability does not work that way!")
        
    if probA > 1 or probA <=0 or probA < jointProb:
        sys.exit("Probability does not work that way!")
        
    condProb = jointProb / probA

    return round(condProb,2)