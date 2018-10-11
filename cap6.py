import csv
import os
import numpy as np
def takeSecond(elem):
    return elem[1]
def takeScore(elem):
    return elem[2]


def get_result(file_name):
  files=os.listdir('regions')
  reader = csv.reader(open('regions/' +file_name))
  filenum=len(list(reader))
  print(filenum)
  a=[]
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
      k=0
      reader = csv.reader(open('regions/' + name))
      for row in reader:
          a[k][0]=row[0]
          a[k][1]=(float(row[1])+float(row[3]))/2
          a[k][2]=(float(row[5]))
          k=k+1
      a.sort(key=takeScore,reverse=True)
      #print a
      b=a[0:filenum][:]
      #print b
      b.sort(key=takeSecond)
      s=str()
      for i in range(filenum):
          print(i)
          s+=str(b[i][0])
      print s
  return s
    # #a.sort()


if __name__=='__main__':
    key=get_result()
    print(key)