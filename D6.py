# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:06:08 2021

@author: sunny
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
from sklearn.decomposition import PCA

data = pd.read_csv('movieReplicationSet.csv')
print(data.shape)