#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:50:52 2019

@author: jefft
"""

#-----FIND LEGAL ADDRESS-------
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header

fl1 = open('address_information.csv')
adlist = []
nmlist = []
sblist = []
t = 0
for line in fl1:
    mylist = re.split(',', str(line))
    if re.search(r'@', mylist[1]) == None: #omit the first line where no mail data is incluced
        continue
    if re.match(r'.+@.+\.com', mylist[1]):
        print(mylist[1], ':Correct Adress!')
        adlist += [mylist[1]]
        nmlist += [mylist[0]]
        sblist += [mylist[2]]
    else:
        print(mylist[1],':Wrong Adress!')
    
#-----SEND EMAIL-------
        #login server

sender = input('sender address:')
sev_ad = 'smtp.' + re.findall('@(.+)', sender)[0]
pw = input('password:')
server = smtplib.SMTP(sev_ad,25)
server.login(sender, pw)
print('From:'+ sender)

body = open('body.txt')
text = ''
for line in body:
    text += line #read the body
body.close()
        #send email
for i in range(0,len(adlist)):
    correct_text = re.sub(r'User', nmlist[i], text)
    msg = MIMEText(correct_text, 'palin', 'utf-8')
    try:
        server.sendmail(sender, [adlist[i]], msg.as_string())
        print ("Mail sent successfully!")
    except smtplib.SMTPException:
        print ("Error")
server.quit()

#from 菜鸟教程

sender = input('sender address:')
mail_user = input('your name:')
mail_host = 'smtp.' + re.findall('@(.+)', sender)[0]
mail_pass = input('password:')    

for i in range(0, len(adlist)):
    receivers = [adlist[i]]
    
    body = 'Dear ' + nmlist[i]+ ':\n' + 'Please find the results of your gene set linkage analysis result in attached file.\nThis is an email sent by the server, please don\'t reply.\nThank you for using GSLA.' 
    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = Header(sblist[i], 'utf-8')
    message['To'] =  Header(sblist[i], 'utf-8')

    message['Subject'] = Header(sblist[i], 'utf-8')
     
     
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)   
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("Mail sent successfully!")
    except smtplib.SMTPException:
        print ("Error")
smtpObj.quit()