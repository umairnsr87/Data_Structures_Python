import re

val=input()

flag=set(val)

list=["H","Q","9"]
pos=0
neg=0
for ele in flag:
    if ele in list:
        pos+=1
    else:
        neg+=1

if pos>0:
    print("YES")
else:
    print("NO")