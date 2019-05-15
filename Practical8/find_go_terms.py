#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:32:20 2019
    This script
@author: jefft
"""
#http://geneontology.org/docs/ontology-documentation/
#http://pandas.pydata.org/pandas-docs/stable/
"""
common pattern in go_obo.xml
<term>
    <id>GO:XXXXXXX</id>
    <name>xxx</name>
    <def>
        <defstr>some_terms</defstr>
        <is_a>GO:XXXXXXX</is_a>
        <is_a>GO:XXXXXXX</is_a> #may have multiple parents
    </def>
</term>

from GO homepage:
    "The structure of GO can be described in terms of a graph, where each GO term is a node, and the relationships between the terms are edges between the nodes. 
    GO is loosely hierarchical, with ‘child’ terms being more specialized than their ‘parent’ terms, 
    but unlike a strict hierarchy, a term may have more than one parent term (note that the parent/child model does not hold true for all types of relations, see the relations documentation). 
    For example, the biological process term hexose biosynthetic process has two parents, hexose metabolic process and monosaccharide biosynthetic process. 
    This reflect the fact that biosynthetic process is a subtype of metabolic process and a hexose is a subtype of monosaccharide."
    
    
"""

import os
os.chdir('/Users/jefft/Desktop/ZJE/IBI(local)/git_repository/IBI1_2018-19/Practical8') #change working directory

#----------------------------SETUP--------------------------------------------
import xml.dom.minidom
import pandas as pd
import re

#create DOM tree
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement

#tms = collection.getElementsByTagName('term')
defnd = collection.getElementsByTagName('defstr') 
is_a = collection.getElementsByTagName('is_a') 

"""
An alternative approach to count child nodes
def child(x): #x is a text string
    count = 0
    for tm in tms:
        is_a = tm.getElementsByTagName('is_a')
        for isa in is_a:
            if x == isa.childNodes[0].data:
                count += 1
                count += child(tm.getElementsByTagName('id')[0].childNodes[0].data)
            return count
"""
dic = {'id':[],'name':[],'definition':[],'childnodes':[]}

res = set('')
def child(x,res):
    """
    x: id number of parent terms
    res: empty set storing all id numbers of child terms
    """
    for j in range(0, is_a.length):
        if x == is_a[j].childNodes[0].data: #if parent node id (x) is equal to child node is_a item
            iden = is_a[j].parentNode.getElementsByTagName('id')[0].childNodes[0].data #get the id of chile node
            res.add(iden) #put child node id into it
            child(iden,res) #now, the child node has become parent node and iterate until if condiontion does not hold -> no child node


#---------------------------MAIN SCRIPT----------------------------------------    
for i in range(0, defnd.length):
    defelm = defnd[i].childNodes[0]
    if re.search('autophagosome', defelm.data):
        term = defelm.parentNode.parentNode.parentNode #parent of the defstr element is <defstr> node
        ide = term.getElementsByTagName('id')[0].childNodes[0].data
        defstr = defelm.data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        child(ide,res)
        children = len(res)
        res = set('')
        dic['id'].append(ide)
        dic['name'].append(name)
        dic['definition'].append(defstr)
        dic['childnodes'].append(children)



dt = pd.DataFrame(dic) #data frame can be created through a dictionary with coloum name = keys
dt.to_excel('autophagosome.xlsx', sheet_name='Sheet1')

