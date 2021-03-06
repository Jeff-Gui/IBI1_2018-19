#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:06:14 2019

@author: jefft
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000 #total populaiton
sp = []
ift = []
rcv = []
list_inf=[]
beta = 0.3
gamma = 0.05
count1 = 0
count2 = 0
for i in range(0,110,10):
    vc =int(N*i/100)
    if N==vc:
        sp=[0]
        ift=[0] #if all people are vaccinated
    else:
        sp=[N-vc-1]
        ift=[1]
    rcv=[0]
    for t in range(1,1000):
        count1 = np.random.choice(range(2),sp[t-1],p=[1-beta*ift[t-1]/N, beta*ift[t-1]/N]).sum() #yield infected people
        count2 = np.random.choice(range(2),ift[t-1],p=[1-gamma, gamma]).sum() #yield recovered people
        sp.append(sp[t-1]-count1)
        rcv.append(rcv[t-1]+count2)
        ift.append(ift[t-1]+count1-count2)
        count1, count2 = 0, 0 #reset
    list_inf.append(ift)
#========================plot==================================================
plt.figure(figsize=(6,4),dpi=150)
x = [y for y in range(1,1001)]
for u in range(0,11):
    plt.plot(x,list_inf[u],label=str(u*10)+'%',color=cm.gnuplot2(u*20)) #plot graphs in one figure with loops
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.savefig("SIR model with different vaccination rates", type="png")