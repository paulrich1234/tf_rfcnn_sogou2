import csv
import os
import numpy as np
def takeSecond(elem):
    return elem[1]
def takeScore(elem):
    return elem[2]
files=os.listdir('regions')
a=[]
filenum=len(files)
for row in range(filenum):
    a.append([])
    for column in range(3):
        num = 0
        a[row].append(num)
b=[]
c=[]
for name in files:
    print name
    for row in range(filenum):
        for column in range(3):
            a[row][column]=0
    #print a
    reader=csv.reader(open('regions/'+name))
    k=0
    for row in reader:
        a[k][0]=row[0]
        a[k][1]=(float(row[1])+float(row[3]))/2
        a[k][2]=(float(row[5]))
        k=k+1
    #print a
    a.sort(key=takeScore,reverse=True)
    #print a
    b=a[0:6][:]
    #print b
    b.sort(key=takeSecond)
    print b[0][0],b[1][0],b[2][0],b[3][0],b[4][0],b[5][0]
    #a.sort()

