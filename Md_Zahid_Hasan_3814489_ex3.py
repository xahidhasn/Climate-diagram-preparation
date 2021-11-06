# -*- coding: utf-8 -*-
"""
Created on Tue May 26 01:03:21 2020

@author: zahid
3814489
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

#Exercise1

DataFrame1=pd.DataFrame({"categorical":('A','B','C','D'),"Metric_data":(3,4,5,6)})
DataFrame2=pd.DataFrame({"categorical":('A','B','C','D'),"Metric_data":(3,7,5,8)})
DataFrame3=pd.DataFrame({"categorical":('A','B','C','D'),"Metric_data":(3,5,5,8)})
DataFrame4=pd.DataFrame({"categorical":('A','B','C','D'),"Metric_data":(2,4,8,8)})

#Exercise2
os.chdir('C:/climat')
df = pd.read_csv('rcp85climate.csv', sep=";", header= 0, parse_dates=[0], index_col=0)

#monthly mean
df_m = df.resample('M').mean()

dfmm= df_m['1960':'2005'].mean()
dfmm1= df_m['2043':'2100'].mean()

df_y=df.resample('Y').mean()

#Annual mean
dfyy= df_y['1960':'2005'].mean()
dfyy1= df_y['2043':'2100'].mean()

#plotting
fix,ax=plt.subplots(3,1,figsize=(16,10))
plt.style.use("seaborn")

plt.subplot()





