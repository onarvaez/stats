# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:14:51 2018

@author: Omar
"""
import numpy as np 
import pandas as pd
import scipy.stats as sst

data = pd.read_csv('/misc/torrey/onarvaez/estadistic/avf_manual_automatic.csv')


vector_automatic=[]
for i in range(100):
    vector_automatic.append(data.iloc[i,0])
vector_manual=[]
for i in range(100):
    vector_manual.append(data.iloc[i,1])    



vector_normality=[]
for i in range(100):
    vector_normality.append(data.iloc[i,0])
    vector_normality.append(data.iloc[i,1])

result_normality_intact = sst.normaltest(vector_normality)



test = sst.ttest_ind(vector_automatic,vector_manual)

vector_pvalues = np.array([test.pvalue])
 

avf_test_1=["avf_test"]

df = pd.DataFrame(vector_pvalues, columns=avf_test_1)
