#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:56:00 2019

@author: jefft
"""


count = 0
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
    except:
        print('The input number must be integers from 1 to 23')
    

#pick up 2 numbers and put them back
#divide whole string into group of 2 numbers
"""
import math
def dvd2(L):
  if len(L) < 2:
      return L[:]
  else:
        middle = len(L)//2
        left = dvd2(L[:middle])
        right = dvd2(L[middle:])
        return [right, left]
L = [1,2,3,4,6,7,8,10]
#left and right should be int
def operation(left, right):
    for i in range(1,math.ceil(len(L)/2)):
        left = left + right
        left = left - right
        left = left * right
        left = left / right
"""        
#------------------------------------------------------------------------------



def compute(x,y,op):
    if op=='+':return x+y
    elif op=='*':return x*y
    elif op=='-':return x-y
    else:return x/y if y else None

def exp(p,iter=0):
    global count
    from itertools import permutations
    if len(p)==1:
        return [(p[0],str(p[0]))]
    operation = ['+','-','*','/']
    ret = []
    p = permutations(p) if iter==0 else [p] #permutation function will output any possible combinaitons of numbers with ORDER, combinations are saved as arrays
    for array_n in p:
        #print(array_n)
        for num in range(1,len(array_n)): #split the combination array into 2 parts, cover every part
            ret1 = exp(array_n[:num],iter+1)
            ret2 = exp(array_n[num:],iter+1)
            for op in operation:
                for va1,expression in ret1:
                    if va1==None:continue
                    for va2,expression2 in ret2:
                        if va2==None:continue
                        combined_exp = '{}{}' if expression.isalnum() else '({}){}'
                        combined_exp += '{}' if expression2.isalnum() else '({})'
                        new_val = compute(va1,va2,op)
                        ret.append((new_val,combined_exp.format(expression,op,expression2)))
                        if iter==0 and new_val==24:
                            return ''.join(e+'\n' for x,e in ret if x==24)
                        count += 1
    return ret

if y:
    print(exp(nm))
    
    print('Recursion times:', count)

count = 0

"""
from itertools import permutations
p = permutations([1,2,3])
ret1 = exp()
"""