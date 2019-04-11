#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:51:30 2019

@author: yangjiaolei
"""
import xml.dom.minidom
import re
import pandas as pd

filePath=r'...';#Your file path
fileName='go_obo.xml';
resName='autophagosome.xlsx'
file=filePath+'/'+fileName
res=filePath+'/'+resName

re_immu = re.compile(r'autophagosome')
#Function to find childnodes 
def Child(id, resultSet):
    for t in go:
        parents = t.getElementsByTagName('is_a')
        geneid = t.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultSet.add(geneid)
#                don't use resultSet = resultSet | set([geneid])
#                otherwise you will create a new set instead of modifying the existing one
#                print (resultSet)
                Child(geneid, resultSet)
                
#create a pandas.Dataframe to store the output
df = pd.DataFrame(columns=['id','name','definition','childnodes'])

#create the DOM tree    
DOMTree = xml.dom.minidom.parse(file) 
obo = DOMTree.documentElement
go = obo.getElementsByTagName('term')
for term in go:
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    #find terms that contain the word 'autophagosome'
    if re_immu.search(defstr):
        id = term.getElementsByTagName('id')[0].childNodes[0].data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        resultSet = set()
        Child(id, resultSet)
        df = df.append(pd.DataFrame({'id':[id],'name':[name],'definition':[defstr],'childnodes':[len(resultSet)]})) 
        print(id, len(resultSet))
#save to excel
df.to_excel(res,index=False)
