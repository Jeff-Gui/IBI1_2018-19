#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:56:00 2019

@author: jefft
"""
#pick up 2 numbers and put them back
#divide whole string into group of 2 numbers
#------------------------------------------------------------------------------
from fractions import Fraction
count = 0
solution = 0
y = False
nm = input('Please input numbers to computer 24:(use \',\' to divide them)\n')
nm = nm.split(',')
#check if input numbers are valid
for i in range(0,len(nm)):
    try:
        if float(nm[i]) == int(nm[i]):
            nm[i] = int(nm[i])
            y = True
        if not 0 < nm[i] < 24:
            print('The input number must be integers from 1 to 23')
    except:
        print('The input number must be integers from 1 to 23')

def dfs(n):
    global count
    global solution
    
    if n == 1:
        if (float(nm[0])==24):
            solution += 1
            return 1    #if 1 is returned when n=1, than every step when it goes back, 1 will be constantly returned, 
        else:
            return 0        
    for i in range(0,n):
        count += 1
        for j in range(i+1,n): #cover every possible combination of 2 numbers in the list
            count += 1
            a = nm[i]
            b = nm[j]
            nm[j] = nm[n-1] 
                
            nm[i] = a+b
            if (dfs(n-1)): #dfs(n-1) return 0 -> not execute, dfs(n-1) return 1 -> execute. If a solution is found, then all recusion funcitons will keep returning 1
                return 1
                
            nm[i] = b-a
            if (dfs(n-1)):
                return 1
            
            nm[i] = a-b
            if (dfs(n-1)):
                return 1
                
            nm[i] = a*b
            if (dfs(n-1)):
                return 1
                
            if a:
                nm[i] = Fraction(b,a) #fraction function can avoid /0
                if (dfs(n-1)):
                    return 1
                
            if b:
                nm[i] = Fraction(a,b)
                if (dfs(n-1)):
                    return 1
                
            nm[i] = a
            nm[j] = b #restore the list
    return 0

if (dfs(len(nm))): #finally returns 0
    print('Yes')
else:               #finally returns 1
    print('No')
print('Recursion times:',count,'Solution:',solution)