# -*- coding: utf-8 -*-
"""
Created on Tue May 26 03:33:47 2020

@author: zahidhasan3814489
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


# Exercise 04



os.chdir('E:\ROAD TO BLUE\SUMMER 2020\MicroClimate\exercise import file')
df = pd.read_csv('Ex04_data.csv', sep=";", header= 0, parse_dates=[0], index_col=0)
dfTem = df[['Tmax','Tmin']].resample('M').mean()
dfRain = df['RR'].resample('M').sum()

# Calculation of Monthly means

Mm_df=df.resample('M').mean()

dfwintr = df['1981':'2010']
dfm = df['1981':'2017'].resample('M').mean()
tab = dfm.reset_index()
tab['month']= tab['Date'].dt.month
dfmJJA = tab.query('month==10 or month==11 or month==12') 
dfmJJA = dfmJJA.set_index('Date')
dfmJJA.drop('month',axis=1, inplace=True)

#Anomalies calculation
rrano = dfmJJA.RR - dfwintr.RR.mean()
tano = dfmJJA[['Tmax', 'Tmin']] - dfwintr[['Tmax', 'Tmin']].mean()

month = ('Oct', 'Nov', 'Dec')
dfsrc=dfmJJA.iloc[:,0:3]
dfsrc2 = tano.iloc[:,0:2]


#Group formation

dfJmean = dfsrc.groupby([pd.DatetimeIndex(dfsrc.index).month]).mean().round(1)
rranomnth = rrano.groupby([pd.DatetimeIndex(rrano.index).month]).mean().round(1)
tanomnth = dfsrc2.groupby([pd.DatetimeIndex(dfsrc2.index).month]).mean().round(1)

ranomnth =rranomnth.to_frame()
mon = ['Oct', 'Nov', 'Dec']






