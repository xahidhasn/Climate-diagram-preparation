# -*- coding: utf-8 -*-
"""
Created on Fri May  1 02:51:52 2020

@author: Md Zahid Hasan
Matriculation Nr: 3814489
"""

import os
import numpy as np
import pandas as pd

#Exercise1
   #an array with the dimensions 3 x 5 with arbitrary values.

Array_3by5=np.array([[2,3,5,8,6],[2,3,7,8,0],[4,5,6,7,2]],dtype=float)
        

  #an empty data Frame
DF_empty = pd.DataFrame()


    #a data frame with 5 rows
DF_row5=pd.DataFrame(index=['row1','row2','row3','row4','row5'])

     #a data frame with 3 rows and 2 columns
DF_row3by2=pd.DataFrame(columns=['Item1','Item2'],index=['row1','row2','row3'])



#Exercise2

list=[45,26,6,7,9]
list.append('AA')
list.remove(26)
len(list)

#Exercise3

#Calculation of Mean Values

os.chdir('C:\climat')
table = pd.read_csv('climate.dat', sep=";")
Tmax=table.loc[:,"Tmax"].mean()
T=table.loc[:,'T'].mean()
Tmin=table.loc[:,'Tmin'].mean()
RR=table.loc[:,'RR'].mean()
Sun=table.loc[:,'Sun'].mean()
Meanlist=[Tmax,T,Tmin,RR,Sun]
Mean_Value=pd.DataFrame(data=Meanlist,index=['T','Tmax','Tmin','RR','Sun'])

# the end