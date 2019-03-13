#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:27:54 2019

@author: jefft
"""

#input and print n(integer)
#check if n=1, if so, end loop; else, go on
#check if n is a even number
#if n is a even number, divide n by 2, and asign the result to n
#if n is an odd number, multiply n by 3 and add 1, then asign the result to n
#print n
#repeat the above 4 steps until the loop ends

n = 123
print(n)
while n != 1:
    if n%2 == 0:
        n = n/2
    else:
        n = 3*n + 1
    print(n)
    