def genbigram(words):
    li=[]
    temp=words.split(' ')
    for i in range (len(temp)-1):
        li.append(temp[i]+" "+temp[i+1])
    return li

