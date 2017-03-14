def ngramanalysis(n):
    import os
    import string
    from collections import Counter
    from cleanfile import cleanfile
    from genngram import genngram
    import csv
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
    alltext=''
    #clean all transcripts and save in cleanedtext
    files=os.listdir('Transcript')
    for i in range (1,len(files)):
        try:
            text=open('Transcript/'+files[i], 'r').read().lower()
            interviewee=keys[int(files[i].split('.')[0])]
            words=cleanfile(text,interviewee)
            alltext=alltext+words+" "
            wordslist=set(words.split())
            words=' '.join(wordslist)
            cleanedtext=cleanedtext+words+" "
        except Exception:
            print(files[i].split('.')[0])
            continue
    cleanedtext=cleanedtext.strip()
    cleanedlist=Counter(genngram(cleanedtext, n)).most_common()[:1000]
    f=open("results/1000 "+str(n)+"grams by population.txt", "w+")
    f.seek(0)
    f.truncate()
    f.write('\n'.join('{} {}'.format(x[0],x[1]) for x in cleanedlist))
    f.close()
    ##This list is generated by counting a bigram multiple times if it appears in a transcript several times
    ##(i.e. multiple appearances in one transcript is counted as multiple times)
    alltext=alltext.strip()
    alltextlist=Counter(genngram(alltext, n)).most_common()[:1000]
    f=open("results/1000 "+str(n)+"grams by frequency.txt", "w+")
    f.seek(0)
    f.truncate()
    f.write('\n'.join('{} {}'.format(x[0],x[1]) for x in alltextlist))
    f.close()
    return None