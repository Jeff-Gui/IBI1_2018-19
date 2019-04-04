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
#------------------------------------------------------------------------------



def compute(x,y,op):
    if op=='+':return x+y
    elif op=='*':return x*y
    elif op=='-':return x-y
    else:
        return x/y if y else None
    #this is the same as
    # if y:
    #   return x/y
    #else:
    #   return None
"""
syntax: if y: with no more condition means y is 0 (for int) or not empty(for other classes), then it will go on
syntax: return [object1] if [condition] else [object2]
.isalnum: test if a string is only composed of number and letters (no white space or '()'-like)
.format: formalize a string
"""
def exp(p,ite=0):
    global count
    from itertools import permutations
    if len(p)==1:
        return [(p[0],str(p[0]))]
    operation = ['+','-','*','/']
    ret = []
    p = permutations(p) if ite==0 else [p] #permutation function will output any possible combinaitons of numbers with ORDER, combinations are saved as arrays
    for array_n in p:
        #print(array_n)
        for num in range(1,len(array_n)): #split the combination array into 2 parts, cover every possible combination
            ret1 = exp(array_n[:num],ite+1)
            ret2 = exp(array_n[num:],ite+1)
            for op in operation:
                for va1,expression in ret1:
                    if va1==None:continue
                    for va2,expression2 in ret2:
                        if va2==None:continue
                        combined_exp = '{}{}' if expression.isalnum() else '({}){}'
                        combined_exp += '{}' if expression2.isalnum() else '({})' #add brackets to the expression
                        new_val = compute(va1,va2,op)
                        ret.append((new_val,combined_exp.format(expression,op,expression2)))
                        if ite==0 and new_val==24:
                            return ''.join(e+'\n' for x,e in ret if x==24) #if x=24, e+'\n'will be joined
                        count += 1
    return ret

if y==True:
    exp(nm)
    print('Recursion times:', count)

count = 0

#-------------------------------------------------------------------------------
def compute(x,y,op):
    if op=='+':return x+y
    elif op=='*':return x*y
    elif op=='-':return x-y
    else:
        if y:
            return x/y
        else:
            None
count = 0
solve = False
def point24(t):
    global count
    global solve
    operation = ['+','-','*','/']
    from itertools import permutations
    if len(t)==1 and t[0]==24:
        solve = True
        return (count,solve)
    if len(t)==1 and t[0]!=24:
        return (count,solve)
    else:
        t = permutations(t)
        for array in t:
            array = list(array)
            for op in operation:
                new_val = compute(array[0], array[1], op)
                del(array[0])
                array[0] = new_val
                point24(array)
                count += 1
                t = point24(array)


point24([1,2,3,4])
#------------------------------------------------------------------------------
from fractions import Fraction
from itertools import permutations
count = 0
solution = 0
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

def dfs(n):
    global count
    global solution
    count += 1
    
    if n == 1:
        if (float(nm[0])==24):
            solution += 1
            return 1
        else:
            return 0
    nm = permutations(nm)
    for ay in nm:
        ay = list(ay)
        for i in range(0,n):
            for j in range(i+1,n): #cover every possible combination of 2 numbers in the list
                a = ay[i]
                b = ay[j]
                ay[j] = ay[n-1]
                
                ay[i] = a+b
                if(dfs(n-1)):
                    return 1
                
                ay[i] = b-a
                if(dfs(n-1)):
                    return 1
                
                ay[i] = a*b
                if (dfs(n-1)):
                    return 1
                
                if a:
                    ay[i] = Fraction(b,a)
                    if (dfs(n-1)):
                        return 1
                
                if b:
                    ay[i] = Fraction(a,b)
                    if (dfs(n-1)):
                        return 1
                
                ay[i] = a
                ay[j] = b
    return 0

if (dfs(len(nm))):
    print('Yes')
else:
    print('No')
print('Recursion times:',count,'Solution:',solution)