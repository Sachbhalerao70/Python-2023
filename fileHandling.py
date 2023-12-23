mobileNumber=[]
email=[]
yahoo=[]
word=[]

fp=open('file.txt','r')
rowData=fp.readlines()
for i in rowData:
    word.append(i.split())
#print(rowData)
#print(word)
# ------------------------------------------
for i in word:
    for x in i:
        if x.startswith('9') or x.startswith('7') or x.startswith('8'):
            if len(x)==10:
                if x not in mobileNumber:
                    mobileNumber.append(x)
        elif x.endswith("@gmail.com"):
            if x not in email:
                email.append(x)
        elif x.endswith("@yahoo.com"):
            if x not in yahoo:
                yahoo.append(x)

#Store this output in file
fp=open('mobileNumber.txt','w')
for i in mobileNumber:
    fp.writelines(i+'\n')

fp=open('email.txt','w')
for i in email:
        fp.writelines(i+'\n')

fp=open('yahoo.txt','w')
for i in yahoo:
    fp.writelines(i+'\n')

print("Successfully writes all filee")
