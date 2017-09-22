def ngramanalysis(n):
    import os
    import string
    from collections import Counter
    from cleanfile import cleanfile
    from genngram import genngram
    import csv
    splitwords=['ellis']
    splitwords=set(splitwords)
    #reading interviewees' ID's and hence lastnames from  keys.xls to a distionary
    from xlrd import open_workbook
    workbook = open_workbook('keys.xls')
    sheet=workbook.sheets()[0]
    number_of_rows = sheet.nrows
    keys={}
    for i in range (0, number_of_rows):
        keys[i+1]=sheet.cell(i,1).value.lower()
    cleanedtext=''
    alltext=''
    beforetext=''
    aftertext=''
    #reading all file names in folder "Transcript"
    files=os.listdir('Transcript')
    for i in range (1,len(files)):
        #try except to print out any error 
        #this step is crucial in identifying broken transcripts (more details in readme.md)
        try:
            #reading transcripts and converting to lower case words
            text=open('Transcript/'+files[i], 'r').read().lower()
            textsplit=text.split(" ")
            interviewer=text.strip().split(":")[0]
            textsplit=[i for i in textsplit if i]
            index=[i for i, e in enumerate(textsplit) if e in splitwords]
            beforewords=''
            afterwords=''
            #interviewee lastname from distionary
            interviewee=keys[int(files[i].split('.')[0])]
            if index:
                index=[i for i in index if i>=0.1*len(textsplit) and i<=0.65*len(textsplit)]
                if index:
                    split=min(index)
                    beforetemp=" ".join(textsplit[:split+1])
                    aftertemp=" ".join(textsplit[split+2:])
                    beforetemp=beforetemp.strip()
                    aftertemp=aftertemp.strip()
                    beforetemp=interviewer+": "+beforetemp
                    aftertemp=interviewer+": "+aftertemp
                    beforewords=cleanfile(beforetemp,interviewee)
                    afterwords=cleanfile(aftertemp,interviewee)

            #calling generic function cleanfile to filter out content other than interviewee's
            #also taking out stop words, punctuations, digits, and extra white spaces
            #expanding contractions
            words=cleanfile(text,interviewee)
            
            #alltext contains the original content of all cleaned transcripts
            alltext=alltext+words+" "
            beforetext=beforetext+beforewords+" "
            aftertext=aftertext+afterwords+" "
            #cleanedtext on the other hand, only allow a word to appear once in one transcript
            wordslist=set(words.split())
            words=' '.join(wordslist)
            cleanedtext=cleanedtext+words+" "
        except Exception:
            #print out file names of broken transcripts
            print(files[i].split('.')[0])
            continue
    cleanedtext=cleanedtext.strip()
    #finding top 1000 most common n-gram in terms of number of people who mention it
    ##This list is generated by counting a bigram one time even if it appears in a transcript several times
    ##(i.e. multiple appearances in one transcript is counted as one time)
    cleanedlist=Counter(genngram(cleanedtext, n)).most_common()[:1000]
    #writing results to a .txt file
    f=open("results/ellis/1000 "+str(n)+"grams by population.txt", "w+")
    #cleaning original content in case file not empty
    f.seek(0)
    f.truncate()
    f.write('\n'.join('{} {}'.format(x[0],x[1]) for x in cleanedlist))
    f.close()
    alltext=alltext.strip()
    #finding top 1000 most common n-gram in terms of frequency that it appears in all transcripts
    ##This list is generated by counting a bigram multiple times if it appears in a transcript several times
    ##(i.e. multiple appearances in one transcript is counted as multiple times)
    alltextlist=Counter(genngram(alltext, n)).most_common()[:1000]
    #writing results into a .txt file
    f=open("results/ellis/1000 "+str(n)+"grams by frequency.txt", "w+")
    f.seek(0)
    f.truncate()
    f.write('\n'.join('{} {}'.format(x[0],x[1]) for x in alltextlist))
    f.close()
    
    #story before arrival
    beforetext=beforetext.strip()
    beforetextlist=Counter(genngram(beforetext, n)).most_common()[:1000]
    #writing results into a .txt file
    f=open("results/ellis/1000 "+str(n)+"grams pre-arrival.txt", "w+")
    f.seek(0)
    f.truncate()
    f.write('\n'.join('{} {}'.format(x[0],x[1]) for x in beforetextlist))
    f.close()
    
    #story after arrival
    aftertext=aftertext.strip()
    aftertextlist=Counter(genngram(aftertext, n)).most_common()[:1000]
    #writing results into a .txt file
    f=open("results/ellis/1000 "+str(n)+"grams post-arrival.txt", "w+")
    f.seek(0)
    f.truncate()
    f.write('\n'.join('{} {}'.format(x[0],x[1]) for x in aftertextlist))
    f.close()
    
    return None
