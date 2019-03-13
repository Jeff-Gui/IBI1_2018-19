#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:04:56 2019

@author: jefft
"""

#input n
#input a string for output
#input t = 1
#find t such that 2**t < n
#assign n-2**ti to n, add the result to the output
#find another t such that 2**t2 < n < 2**t
#assign n-2**t2 to n, add the result to the output
#repeat, until n=0
#for the last item, no "+" is needed
#print the output

n = 1233
t = 1
output = str(n) + " is "
while (n != 0):
    while 2**t <= n:
        t = t + 1
    n = n - 2**(t-1)
    if n == 0:
        output = output + "2**" + str(t-1)
        break
    output = output + "2**" + str(t-1) + " + "
    t=1
print(output)
    