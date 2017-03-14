def genngram(words, n):
    li=[]
    temp=words.split(' ')
    word=''
    #generating n-grams
    for i in range (len(temp)-n+1):
        for j in range (n):
            word=word+" "+temp[i+j]
        #taking out extra white spaces
        word=word.strip()
        li.append(word)
        #reset word to an empty string
        word=''
    return li

