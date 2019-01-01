import os
import sys

dict={}

with open(sys.argv[1]) as file:
 for line in file:
  for words in line.split():
   dict[words]=dict.get(words,0)+1


sortedList=[ ]
l=[]
sortedList=sorted(dict.items(),key=lambda x : x[1],reverse=True)
for i in range(0,10):
 print(sortedList[i])
 l.append(sortedList[i])
 
print(l)
k=[]

for i in l:
 k.append(len(i[0]))

print(k)
m=[x**2 for x in k if x%2!=0]
print(m)

 #BY ABHIJEET SARAF :)