#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:46:47 2019

@author: jefft
"""

words = input('give me a string of words:')
mylist = words.split(' ')

for i in range(len(mylist)):
    mylist[i] = mylist[i][::-1]
"""
why cannot use 
for string in mylist:
    string = string[::-1]
answer: string[::-1] create a new list, by giving a reference to the string, it won't change the object also called by string
"""
mylist.sort()
"""
.sort() output NONE,
therefore, sorted(list_name) == list_name.sort()
also, you cannot operate on it with function
for example, reversed(mylist.sort()) is no use
"""
mylist.reverse()

print(mylist)