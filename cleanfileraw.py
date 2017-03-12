
# coding: utf-8

# In[ ]:

def cleanfileraw(text, interviewee):
    from nltk import PorterStemmer
    from nltk.tokenize import sent_tokenize, word_tokenize
    import string
    
    punct=set(string.punctuation)
    words = text.split(":")
    interviewer=words[0]
    wordsclean=[]
    for i in range(len(words)-1):
        if words[i].split(" ")[-1]==interviewee:
            wordsclean.append(words[i+1]) 
    if len(wordsclean)!=0:
        words=[]
        for i in range(len(wordsclean)-1):
            temp=wordsclean[i].split(" ")
            del temp[-1]
            words.append(" ".join(temp))
        words.append(wordsclean[-1])
        for i in range(len(words)):
            words[i]=words[i].strip() 
        text = " ".join(words)

        text=text.replace("'","97401")
        textclean=''.join(x for x in text if x not in punct)
        text=textclean.strip()

        text=text.replace("97401","'")
        text=text.replace(interviewer, "")
        
        text=''.join([x for x in text if not x.isdigit()])

        wordsnew=[]
        words=text.split(" ")
        for i in range (len(words)):
            if words[i]!='':
                wordsnew.append(words[i])

        text=' '.join(wordsnew)
        textclean=''.join(x for x in text if x not in punct)
        text=textclean.strip()
        saveforlater=text
        
        text=text.split(" ")
        text=[x for x in text if x!=""]
        
        textclean=' '.join(text)
        return textclean
    else:
        return ''


