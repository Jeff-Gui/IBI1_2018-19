#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:17:58 2019

@author: jefft
"""
#simple math
a = 820
b = 820820
print(b % 7 == 0)
c = b/7
d = c/11
e = d/13

#Boolean variables
X = True
Y = False
Z = (X and not Y) or (Y and not X)
W = (X != Y)
print(Z == W)

X = True
Y = True
Z = (X and not Y) or (Y and not X)
W = (X != Y)
print(Z == W)

X = False
Y = False
Z = (X and not Y) or (Y and not X)
W = (X != Y)
print(Z == W)

X = False
Y = True
Z = (X and not Y) or (Y and not X)
W = (X != Y)
print(Z == W)

