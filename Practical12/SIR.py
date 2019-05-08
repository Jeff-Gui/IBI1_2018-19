#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:03:35 2019

@author: jefft
"""

import numpy as np
import matplotlib.pyplot as plt

N = 10000 #total populaiton
sp = []
ift = []
rcv = []
beta = 0.3
gamma = 0.05
count1 = 0
count2 = 0
sp.append(N-1)
ift.append(1)
rcv.append(0)
for t in range(1,1000):
    for item in np.random.choice(range(2),sp[t-1],p=[1-beta*ift[t-1]/N, beta*ift[t-1]/N]): #yield infected people
        if item==1:
          count1 += 1
    sp.append(sp[t-1]-count1)
    for item in np.random.choice(range(2),ift[t-1],p=[1-gamma, gamma]): #yield recovered people
        if item==1:
            count2 += 1
    rcv.append(rcv[t-1]+count2)
    ift.append(ift[t-1]+count1-count2)
    count1, count2 = 0, 0 #reset

#========================plot==================================================
plt.figure(figsize=(6,4),dpi=150)
x = [y for y in range(1,1001)]
plt.plot(x,sp,label='susceptible')
plt.plot(x,ift,label='infected')   
plt.plot(x,rcv,label='recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend() 
plt.savefig("simple SIR", type="png")
