#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:46:47 2019

@author: jefft
"""

words = str(input('give me a string of words:'))
mylist = words.split(' ')
for i in range(len(mylist)):
    mylist[i] = mylist[i][::-1]
"""
why cannot use 
for string in mylist:
    string = string[::-1]
"""
mylist.sort()
mylist.reverse()

print(mylist)