# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:55:46 2019

@author: KYDNN
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt

pathi = sys.argv[1]

pd.read_csv(pathi).iloc[:,1:4].plot(figsize=[22,5])
plt.show()