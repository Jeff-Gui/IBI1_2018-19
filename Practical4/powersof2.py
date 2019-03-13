#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:04:56 2019

@author: jefft
"""

#input n
#input i = 1
#find ti such that 2**ti < n < 2**(ti+1)
#assign n-2**ti to n
#find t(i+1) such that 2**t2 < n < 2**(t(i+1)+1)
#assign n-2**t2 to n
#until n=0
#print "n is " 2**t1 + 2**t2 +...+2**0

n = 2019
i = 1
s = 1
while n != 0:
    while 2**i < n:
        i = i + 1
    n = n - 2**(i-1)
    print(n)
    