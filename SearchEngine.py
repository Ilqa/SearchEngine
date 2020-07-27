import numpy 
import glob
import os
 
filelist = glob.glob(os.path.join(os.getcwd(), "Files", "*.txt"))
alldata=""

for filepath in filelist:
    with open(filepath) as filein:
        alldata += filein.read().lower()
        alldata += " "

def removepunctuations(textdata):
    for j in textdata:
        if(j in (',','.','?','!','@','#','$','%','^','&','*','(',')','_','-',)):
            textdata=textdata.replace(j,"")
        if(j =='\n'):
            textdata=textdata.replace(j," ")
    return textdata

alldata = alldata[:-1]
alldata = removepunctuations(alldata)
listofalldata=alldata.split(" ")

dicwithfrequency = dict()
for c in listofalldata:
    if c not in dicwithfrequency:
        dicwithfrequency[c]=1
    else:
        dicwithfrequency[c]=dicwithfrequency[c]+1

#step3
dictnumbertoword = dict()
count=1
for word in dicwithfrequency:
    dictnumbertoword[count]= word
    count+=1

dictwordtonumber = dict()
count = 1
values = dictnumbertoword.values()
for word in values:
    dictwordtonumber[word]=count
    count+=1

countofuniquewords=len(dictnumbertoword)
numberoffiles=len(filelist)

#Step 4
tdm=numpy.zeros([numberoffiles,countofuniquewords])
fileindex = 0
for filepath in filelist:
    with open(filepath) as filein:
       filedata = filein.read().lower()
       filedata = removepunctuations(filedata)
       filedatalist = filedata.split(" ")
       filedatalist = list(set(filedatalist))
       for word in filedatalist:
           if(word in dictwordtonumber):
               wordindex = dictwordtonumber[word]
               tdm[fileindex][wordindex-1] = 1
       fileindex = fileindex+1

#Step 5
query=input("Search data in files: ").lower()
query = removepunctuations(query)
queryarray=numpy.zeros([1,countofuniquewords])
querylist = list()
querylist=query.split(" ")

for word in querylist:
    if(word in dictwordtonumber):
        a =  dictwordtonumber[word]
        queryarray[0][a-1] = 1

#Step 6
queryresult = queryarray*tdm
relevencedict = dict()
relevencedictsorted = dict()
rowIndex = 0
for row in queryresult:
    relevencedict[rowIndex] = sum(1 for f in row if f==1)
    rowIndex = rowIndex+1

for (key, value) in sorted(relevencedict.items() , reverse= True,  key=lambda x: x[1]):
    relevencedictsorted[key] =value

recordfound=1
for i in relevencedictsorted:
    if(relevencedictsorted[i] != 0):
        recordfound=0    
        print(os.path.basename(filelist[i]))

if(recordfound==1):
    print("No relevant files")    

print("******************************************************")





    