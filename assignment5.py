#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:34:29 2020

@author: MD ZAHID HASAN,3814489
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


src = 'C:/Users/zahid/Desktop/'
df = pd.read_csv(src + 'wind_data.csv', sep=";" , header = 0, parse_dates= [0], index_col=0, na_values= -999)

df = df.rename(columns={'u (m/s)': 'u', 'v (m/s)':'v', 'w (m/s)': 'w'})
U_mean = df['u'].mean()
V_mean = df['v'].mean()
W_mean = df['w'].mean()

#velocity fluctuations (u,v,w)

u = df['u']-U_mean
v = df['v'] -V_mean
w = df['w'] -W_mean

#square of flactuations or turbulence
u2 = np.multiply(u,u)
v2 = np.multiply(v,v)
w2 = np.multiply(w,w)

u2Mean = np.mean(u2)
v2Mean = np.mean(v2)
w2Mean = np.mean(w2)

e_avrge = 0.5*(u2Mean+v2Mean+w2Mean)

#hourly TKE

dfh = df.resample('H').mean()
dfh = dfh.dropna()

Ufmean = dfh['u'].mean()
Vfmean = dfh['v'].mean()
Wfmean = dfh['w'].mean()

dfh['u2'] = np.multiply(dfh['u']-Ufmean,dfh['u']-Ufmean)
dfh['v2'] = np.multiply(dfh['v'] -Vfmean, dfh['v'] -Vfmean)
dfh['w2'] = np.multiply(dfh['w'] -Wfmean, dfh['w'] -Wfmean)
dfh['e'] = 0.5*(dfh['u2']+dfh['v2']+dfh['w2'])

dfh.e.mean()

dfh = dfh.drop(columns=['u', 'v', 'w','u2', 'v2', 'w2'])
dfh['hours'] = pd.DatetimeIndex(dfh.index).hour

dfH = dfh.reset_index()
fig, (e)=plt.subplots(figsize=(6,4))

e.bar(dfH.index, dfH.e, color='blue')
e.set_title('TKE Hourly')
e.xaxis.set_ticks(dfH.index)
e.xaxis.set_ticks(np.arange(min(dfH.index), max(dfH.index)+1, 12.0))


#Reynolds Stress Tensor

uv = np.multiply(u,v)
uw = np.multiply(u,w)
vw = np.multiply(v,w)

uvmean = np.mean(uv)
uwmean = np.mean(uw)
vwmean = np.mean(vw)

ReynoldsStress = [
    [u2Mean, uvmean, uwmean],
    [uvmean, v2Mean, vwmean],
    [uwmean, vwmean, w2Mean]
    ]

print("Reynolds Stress Tensor=", ReynoldsStress)

#Correlation

dfh = dfh.drop(columns=('hours'), axis=1)
r = dfh.corr()

#Correlation Plotting 

a, b = np.polyfit(dfh['ustar (m/s)'], dfh['e'], 1)

fig,scat = plt.subplots(figsize=(6,4))
scat.plot(dfh['ustar (m/s)'], dfh['e'], 'or')
scat.plot(dfh['ustar (m/s)'], a*dfh['ustar (m/s)']+b, color='green')
scat.text(0, 8, 'r = 0.88' ,fontsize=15)

print(uvmean)