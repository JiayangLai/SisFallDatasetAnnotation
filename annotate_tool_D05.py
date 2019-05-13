# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:55:46 2019

@author: KYDNN
"""
import pandas as pd
import sys
path = 'SisFall_dataset_csv/'
pathout = 'SisFall_dataset_csv_annotated/'
file = sys.argv[1]
upBeginIdx=int(sys.argv[2])
upEndIdx=int(sys.argv[3])

downBeginIdx=int(sys.argv[4])
downEndIdx=int(sys.argv[5])


tbl = pd.read_csv(path+file).iloc[:,1:]
tbl.columns = ['acc1_x','acc1_y','acc1_z','gyro_x','gyro_y','gyro_z','acc2_x','acc2_y','acc2_z']

tblUp = tbl.iloc[upBeginIdx:upEndIdx,:].copy()
tblUp.loc[:,'label']=5

tblDown = tbl.iloc[downBeginIdx:downEndIdx,:].copy()
tblDown.loc[:,'label']=6

tblUp.to_csv(pathout+file[:-4]+'_upstairs_annotated.csv',encoding='GBK')

tblDown.to_csv(pathout+file[:-4]+'_downstairs_annotated.csv',encoding='GBK')