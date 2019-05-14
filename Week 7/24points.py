#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:56:00 2019

@author: jefft
"""
from fractions import Fraction
count = 0
s = 0
y = False
nm = input('Please input numbers to computer 24:(use \',\' to divide them)\n')
nm = nm.split(',')
for i in range(0,len(nm)):
    try:
        if float(nm[i]) == int(nm[i]):
            nm[i] = int(nm[i])
            y = True
        if not 0 < nm[i] < 24:
            print('The input number must be integers from 1 to 23')
            s = 1
            break
    except:
        print('The input number must be integers from 1 to 23')
        s = 1
        break

#pick up 2 numbers and put them back
#divide whole string into group of 2 numbers
#==============================================================================
def compute(x,y,op,t):
    if op=='+':return x+y
    elif op=='*':return x*y
    elif op=='-':return x-y
    elif op=='r-':return y-x 
    elif op=='/':
        if y:
            return Fraction(x,y)
        else:
            return nm[t]
    else:
        if x:
            return Fraction(y,x) #division is not precise, e.g. 1/3=0.333, 0.333*3=0.999!=1
        else:
            return nm[t]
#==============================================================================
def dfs(n):
    """
    n is the "calculating area" of a list. Shorten by one once every calculation
    (merge two numbers at the first and second position of the list by maths operaition
    put the result to the first position
    put the last item to the second position
    in next recrusion, compute these two positions again)
    restore the list after recursion for next step in the loop
    """
    global count
    global nm
    count += 1    
    if n == 1:
        if nm[0]==None:
            return 0
        elif (float(nm[0])==24):
            return 1    #if 1 is returned when n=1, than every step when it goes back, 1 will be constantly returned, 
        else:
            return 0        
    for i in range(0,n):
        for j in range(i+1,n): #cover every possible combination of 2 numbers in the current "calculating area"
            a = nm[i]
            b = nm[j]
            #print(nm,n)
            nm[j] = nm[n-1] #put the last item into the place to be operated next time
            for char in ['+','-','r-','*','/','r/']: #'r-' is reverse minus (y-x),'r/' is reverse divide (y/x)
                nm[i] = compute(a,b,char,i)
                if (dfs(n-1)): # if find a solution, than return 1 -> not executed
                    return 1
            # if cannot find a solution, than not executed (already return)
            nm[i] = a
            nm[j] = b #restore the list
    return 0

if s==0:
    if (dfs(len(nm))): #finally returns 0
        print('Yes')
    else:               #finally returns 1
        print('No')
    print('Recursion times:',count)