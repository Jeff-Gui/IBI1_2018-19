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

body = open('body.txt')
text = ''
for line in body:
    text += line #read the body
body.close()
        #send email
server = smtplib.SMTP(sev_ad,25)
server.login(sender, pw)
print('From:'+ sender)

for i in range(0,len(adlist)):
    correct_text = re.sub(r'User', nmlist[i], text)
    msg = MIMEText(correct_text, 'plain', 'utf-8')
    msg['Subject'] = Header(sblist[i], 'utf-8')
    msg['From'] = Header(sender, 'utf-8')
    msg['To'] =  Header(adlist[i], 'utf-8')
    try:
        server.sendmail(sender, [adlist[i]], str(msg))
        print ("Mail sent successfully!")
    except smtplib.SMTPException:
        print ("Error")
    
server.quit()