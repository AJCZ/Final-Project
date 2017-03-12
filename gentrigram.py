
# coding: utf-8

# In[ ]:

def gentrigram(words):
    li=[]
    temp=words.split(' ')
    for i in range (len(temp)-2):
        li.append(temp[i]+" "+temp[i+1]+" "+temp[i+2])
    return li



