#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:03:05 2019

@author: jefft
"""
import numpy as np
import matplotlib.pyplot as plt
import xml.dom.minidom
import os
os.chdir('/Users/jefft/Desktop/ZJE/IBI(local)/git_repository/IBI1_2018-19/Practical13')
def xml_to_cps():
    import os
    import xml.dom.minidom  
    os.system("/Applications/COPASI/CopasiSE -i predator-prey.xml -s predator-prey.cps")
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w")
    cpsTree.writexml(cpsFile)
    cpsFile.close()
#=============================Change Values====================================
pm = np.random.choice(range(100),4)/100
DOMTree = xml.dom.minidom.parse('predator-prey.xml')
collection = DOMTree.documentElement
model_it = collection.getElementsByTagName('parameter')
for i in range(0,4):
    model_it[i].setAttribute('value',str(pm[i]))
filexml = open('predator-prey.xml','w')
DOMTree.writexml(filexml)
filexml.close()

#============================Run COPASI in python==============================
xml_to_cps()
os.system("/Applications/COPASI/CopasiSE predator-prey.cps")

#===========================Read Data and Plot=================================
#read csv file
fl = open('modelResults.csv').readlines()
names = fl[0].split(',')
data=[]
for lines in fl[1:]:
    data.append(lines.split(','))
results = np.array(data)
results = results.astype(np.float)
# set labels with current values
s1 = 'Predator (b=' + str(pm[0]) + ', d=' + str(pm[1]) + ')'
s2 = 'Prey (b=' + str(pm[2]) + ', d=' + str(pm[3]) + ')'
# plot time against predator & prey populaiton
plt.plot(results[:,0],results[:,1], label=s1)
plt.plot(results[:,0],results[:,2], label=s2)
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time course')
plt.legend()
plt.show()
# plot predator populaiton against prey population
plt.plot(results[:,1],results[:,2])
plt.title('Limit cycle')
plt.xlabel('predator population')
plt.ylabel('prey populaition')
plt.show()







