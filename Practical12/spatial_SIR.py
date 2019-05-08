#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:42:31 2019

@author: jefft
"""
"""
-1,1   0,1    1,1
-1,0          1,0
-1,-1  0,-1   1,-1
"""
import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100,100))
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1


beta = 0.3
gamma = 0.05
dict={0:(-1,1),1:(-1,0),2:(-1,-1),3:(0,-1),4:(1,-1),5:(1,0),6:(1,1),7:(0,1)}
for p in range(0,100):
    ift = np.where(population==1) #find the infected points
    rcv = np.random.choice(range(2),len(ift[0]),p=[gamma,1-gamma])
    for j in range(0,len(ift[0])):
        if rcv[j]==0: #these guys will be recovered
            population[ift[0][j],ift[1][j]]=0.5
    ift = np.where(population==1)
    for i in range(0,len(ift[0])):
        trn = np.random.choice(range(2),8,p=[1-beta,beta])
        rtrn = np.where(trn==1)#these guys, if not recovered, will be infected
        for item in rtrn[0]:
            if ift[0][i]+dict[item][0]>=0 and ift[1][i]+dict[item][1]>=0: #minus nunbers can still be indexed to be other side of the matrix
                try:
                    if population[ift[0][i]+dict[item][0], ift[1][i]+dict[item][1]] ==0: # if not recovered
                        population[ift[0][i]+dict[item][0], ift[1][i]+dict[item][1]] = 1
                except:
                    pass
    plt.figure(figsize=(6,4), dpi=150)
    plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
