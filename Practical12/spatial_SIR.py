#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:42:31 2019

@author: jefft
"""
"""
Use where() to find infected points
    - return tuple with 2 lists (x axis and y axis)
1. for each infected point found:
    determine if its neighbour will be infected this time
    1.1 create length-8 list with 0/1
    1.2 map each value to point's neighbours
        relative position of infected points' neighbours stored in dictionary
        -1, 1  0, 1   1, 1
        -1, 0         1, 0
        -1,-1  0,-1   1,-1
    1.3 set value of infected points to 1
        three special situations:
            a) neighbour already recovered -> remain 0.5
            b) neighbour out of the population range -> pass (do nothing)
            c) negative coordinate(other side of the plot) -> pass (do nothing)
2. find infected points again
3. for each infected points found:
    determine if it will recover this time
        set value to 0.5 with possibility gamma
4. plot every time from t= 0 to 100
"""
import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100,100)) #construct the whole population (100*100)
outbreak = np.random.choice(range(100),2) #random choose an outbreak point
population[outbreak[0],outbreak[1]] = 1 #infected denoted as 1


beta = 0.3
gamma = 0.05
dict={0:(-1,1),1:(-1,0),2:(-1,-1),3:(0,-1),4:(1,-1),5:(1,0),6:(1,1),7:(0,1)}
for p in range(0,100):
    ift = np.where(population==1)
    for i in range(0,len(ift[0])):
        trn = np.random.choice(range(2),8,p=[1-beta,beta])
        rtrn = np.where(trn==1) #these points, if not recovered, will be infected
        for item in rtrn[0]:
            if ift[0][i]+dict[item][0]>=0 and ift[1][i]+dict[item][1]>=0: #negative nunbers can still be indexed to be other side of the matrix
                try:
                    if population[ift[0][i]+dict[item][0], ift[1][i]+dict[item][1]] ==0: # if not recovered
                        population[ift[0][i]+dict[item][0], ift[1][i]+dict[item][1]] = 1 #set infected to 1
                except:
                    pass
    ift = np.where(population==1) #find the infected points again
    rcv = np.random.choice(range(2),len(ift[0]),p=[gamma,1-gamma]) #make a list of possible value(0 for recover, 1 for stay infected)
    for j in range(0,len(ift[0])):
        if rcv[j]==0: #find points to be recovered
            population[ift[0][j],ift[1][j]]=0.5
    plt.figure(figsize=(6,4), dpi=150)
    plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
