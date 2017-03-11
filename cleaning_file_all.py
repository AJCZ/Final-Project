
# coding: utf-8

# In[62]:

import os
from cleanfile import *

#read in interviewees' ID's and lastnames
from xlrd import open_workbook
workbook = open_workbook('keys.xls')
sheet=workbook.sheets()[0]
number_of_rows = sheet.nrows
keys={}
for i in range (0, number_of_rows):
    keys[i+1]=sheet.cell(i,1).value.lower()
#cleanedtext is a string containing all cleaned text
cleanedtext=''
#clean all transcripts and save in cleanedtext
files=os.listdir('Transcript')
for i in range (1,len(files))
    text=open('Transcript/'+files[i], 'r').read().lower()
    interviewee=keys[int(files[i].split('.')[0])]
    cleanedtext[int(files[i].split('.')[0])]=cleanfile(text,interviewee)


# In[ ]:



