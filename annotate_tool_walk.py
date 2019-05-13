# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:55:46 2019

@author: KYDNN
"""
import pandas as pd
import os
path = 'SisFall_dataset_csv/'
pathout = 'SisFall_dataset_csv_annotated/'
filesList = os.listdir(path)

for filei in filesList:
    if filei[:3]=='D02' or filei[:3]=='D01':
        tbl = pd.read_csv(path+filei).iloc[:,1:]
        tbl.columns = ['acc1_x','acc1_y','acc1_z','gyro_x','gyro_y','gyro_z','acc2_x','acc2_y','acc2_z']
        tbl['label']=2
        print(tbl)
        tbl.to_csv(pathout+filei[:-4]+'_annotated.csv',encoding='GBK')