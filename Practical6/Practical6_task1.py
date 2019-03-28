#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:50:52 2019

@author: jefft
"""

import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#-----FIND LEGAL ADDRESSES-------
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
fl1.close()
    
#-----SEND EMAILS-------
    
    #collect information
sender = input('sender address: \n')
sev_ad = 'smtp.' + re.findall('@(.+)', sender)[0] #deduce server name
import getpass
pw = getpass.getpass('password: ') #collect password while not showing in the console *QtConsole does not support the feature
    
    #read email body from body.txt
body = open('body.txt')
text = ''
for line in body:
    text += line #read body line by line
body.close()
    
    #send email
server = smtplib.SMTP(sev_ad,25) #setup SMTP object, port for server is 25
server.login(sender, pw) #connect and login can be done at the same time, or use server.connect() to connect first
print('From:'+ sender)

for i in range(0,len(adlist)):
    correct_text = re.sub(r'User', nmlist[i], text) #replace 'User' with correct name
        #setup message, plain means no-format, utf-8 ensures Chinese character can be read
    msg = MIMEText(correct_text, 'plain', 'utf-8') #decoding
    msg['Subject'] = Header(sblist[i], 'utf-8')
    msg['From'] = Header(sender, 'utf-8')
    msg['To'] =  Header(adlist[i], 'ascii')
        #actually send the email
    try:
        server.sendmail(sender, [adlist[i]], str(msg))
        print ("Mail sent successfully!")
    except smtplib.SMTPException:
        print ("Error")

server.quit()
