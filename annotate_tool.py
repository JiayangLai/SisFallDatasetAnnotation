# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:55:46 2019

@author: KYDNN
"""
#import sys
import pandas as pd

#pathi = sys.argv[1]
pathi ='SisFall_dataset_csv/D05_SA02_R02.csv'

pd.read_csv(pathi).iloc[:,1:4].plot(figsize=[22,5])