def genngram(words, n):
    li=[]
    temp=words.split(' ')
    word=''
    for i in range (len(temp)-n+1):
        for j in range (n):
            word=word+" "+temp[i+j]
        word=word.strip()
        li.append(word)
        word=''
    return li

