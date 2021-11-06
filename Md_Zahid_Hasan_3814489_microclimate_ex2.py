# -*- coding: utf-8 -*-
"""
Created on Tue May 19 01:01:00 2020

@author: Md Zahid Hasan
3814489
"""


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Exercise1

os.chdir('C:/climat')
files = pd.read_csv('Ex02_data.csv', sep=";", header= 0, parse_dates=[0], index_col=0)

#Minimum Values
MinTmax = files.loc[:, 'Tmax'].max()
MinTmin = files.loc[:, 'Tmin'].min()
MinRR = files.loc[:, 'RR'].min()

#Maximum Values
MaxTmax= files.loc[:,'Tmax'].max()
MaxTmin=files.loc[:,'Tmin'].max()
MaxRR=files.loc[:,'RR'].max()

#Calculation of monthly anomalies
meandata= files.resample('M').mean()

AnomaliesTmax= files.Tmax-files.Tmax.mean()
AnomaliesTmin=files.Tmin - files.Tmin.mean()
AnomaliesRR=files.RR-files.RR.mean()





# Exercise2

fix,ax=plt.subplots(3,1,figsize=(16,10))
plt.style.use("seaborn")
ax[0].plot(meandata.index,meandata["Tmax"],label="MAX Temperature",color="r",linestyle="-")
ax[0].set_ylabel("Tmax")
ax[1].plot(meandata.index,meandata["Tmin"],label="Min Temperature",color="g",linestyle="-")
ax[1].set_ylabel("Tmin")
ax[2].plot(meandata.index,meandata["RR"],label="RR",linestyle="-")
ax[2].set_ylabel("RR")
plt.show()


Dataframe=pd.DataFrame({"categorical":('A','B','C','D'),"Metric_data":(3,4,5,6)})

