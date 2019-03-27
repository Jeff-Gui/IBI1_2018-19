#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:59:06 2019

@author: jefft
"""

"""
counting DNA nucleotides
"""
dna = str(input('input a DNA sequence:\n'))
dic = {}
dic['A'] = 0
dic['T'] = 0
dic['C'] = 0
dic['G'] = 0
for char in dna:
    if char == 'A':
        dic['A'] += 1
    if char == 'T':
        dic['T'] += 1
    if char == 'C':
        dic['C'] += 1
    if char == 'G':
        dic['G'] += 1
#PIE PLOT
import matplotlib.pyplot as plt
labels = ['A', 'T', 'C', 'G']
sizes = [dic['A'], dic['T'], dic['C'], dic['G']]
    #autopct will translate data in to pct and sizes value is not needed
#to set the title of the pie chart, use plt.title
plt.title('pie of the four DNA nucleotides')
colors = ['mistyrose', 'powderblue', 'mintcream', 'thistle']
explode= [0, 0.1, 0, 0]
plt.pie(sizes, labels = labels, autopct = '%1.1f%%', colors = colors, explode = explode, startangle = 30) 

plt.show()
print(dna)
print(dic)
