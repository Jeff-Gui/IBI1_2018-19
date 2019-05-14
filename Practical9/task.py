#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:00:34 2019

@author: jefft
"""
"""
sequence source

>SOD2_human (NP_000627.2) 
MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK

>SOD2_mouse (NP_038699.2) 
MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK

>RandomSeq 
WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL

seq_h = 'MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
seq_m = 'MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
seq_r = 'WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'
"""

import os
os.chdir('/Users/jefft/Desktop/ZJE/IBI(local)/git_repository/IBI1_2018-19/Practical9') #change working directory
#==========================Read sequence from .txt files=======================
import re
a1 = open('seq_h.txt')
a2 = a1.read()
a1.close()
seq_h = ''
for char in a2[a2.find('\n')+1:]: #The first line is information, not sequence, skip the first \n
    if re.match('\w',char): # If meet with alphanumeric characters(no numbers in the lines), add into string
        seq_h += char

a1 = open('seq_m.txt')
a2 = a1.read()
a1.close()
seq_m = ''
for char in a2[a2.find('\n')+1:]:
    if re.match('\w',char):
        seq_m += char
        
a1 = open('seq_r.txt')
a2 = a1.read()
a1.close()
seq_r = ''
for char in a2[a2.find('\n')+1:]:
    if re.match('\w',char):
        seq_r += char
        
#========================Construct the matrix dictionary=======================
bls62h = open('BLOSUM62.txt')
bls62 = {}
data = bls62h.readlines() # Read line by line
letterl = re.findall('[A-Z*]', data[0]) # The first line contains all the first letters of the index
for i in range(0, len(letterl)): # i is the location of the first letter
    for j in range(1,len(data)): # for the rest lines in the matrix
        bls62[(letterl[i],data[j][0])] = int(data[j][3*i+2 : 3*i+4]) #find the value(2-len string), make the dictionary(tuple:integer)
bls62h.close()

#===============================Comparing the sequences========================
score = 0
diff = 0
diffseq = ''
for i in range(0, len(seq_h)):
    if seq_h[i] != seq_m[i]:
        diff += 1
        diffseq += '*'
    else:
        diffseq += seq_h[i]
    score += bls62[(seq_h[i],seq_m[i])] #index blosum62 matrix
seqlen = len(seq_h)
print('\nSOD2_human (NP_000627.2)\n', seq_h ,'\n\n ~ \n', diffseq, '\n ~ \n', '\nSOD2_mouse (NP_038699.2)\n', seq_m, sep='')
print('\nBLOSUM62 score:', score, '\nIdentity:', '{:.2%}'.format(1-diff/len(seq_h)))

score = 0
diff = 0
diffseq = ''
for i in range(0, len(seq_h)):
    if seq_m[i] != seq_r[i]:
        diff += 1
        diffseq += '*'
    else:
        diffseq += seq_m[i]
    score += bls62[(seq_m[i],seq_r[i])]
seqlen = len(seq_h)
print('\nSOD2_mouse (NP_038699.2)\n', seq_m ,'\n\n ~ \n', diffseq, '\n ~ \n', '\nRandomSeq\n', seq_r, sep='')
print('\nBLOSUM62 score:', score, '\nIdentity:', '{:.2%}'.format(1-diff/len(seq_m))) #string formating: keep 2 digits of decimals

score = 0
diff = 0
diffseq = ''
for i in range(0, len(seq_h)):
    if seq_h[i] != seq_r[i]:
        diff += 1
        diffseq += '*'
    else:
        diffseq += seq_h[i]
    score += bls62[(seq_h[i],seq_r[i])]
seqlen = len(seq_h)
print('\nSOD2_human (NP_000627.2)\n', seq_h ,'\n\n ~ \n', diffseq, '\n ~ \n', '\nRandomSeq\n', seq_r, sep='')
print('\nBLOSUM62 score:', score, '\nIdentity:', '{:.2%}'.format(1-diff/len(seq_h)))


#========OTHER appraoches to convert txt file into panda dataframe=============
import pandas as pd
#http://pandas.pydata.org/pandas-docs/stable/
data = pd.read_csv('BLOSUM62.txt',sep=' +',engine='python')
dic = data.to_dict()
#to index the "dict in the dict"
dic['A']['P']

