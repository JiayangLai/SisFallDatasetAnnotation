# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:01:24 2019

@author: KYDNN
"""
import os
import pandas as pd

filePath = "SisFall_dataset/"

#print(os.listdir(filePath))
for i,j,k in os.walk(filePath):
    if j == []:
        os.mkdir(i.replace('/','_csv/'))
        print(i.replace('/','_csv/'))
        for filesk in k:
            if 'txt' == filesk[-3:]:
                newfilename = i.replace('/','_csv/')+'/'+filesk.replace('txt','csv')
                print(newfilename)
                csvTbl = pd.read_csv(i+'/'+filesk,header=None)
                csvTbl.iloc[:,8] = csvTbl.iloc[:,8].str.replace(';','')
                csvTbl = csvTbl.astype('float')
                csvTbl.to_csv(newfilename,encoding='GBK')
