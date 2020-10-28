import copy
pages=int(input())

days=input()

days=days.split(" ")
temp=copy.deepcopy(pages)
i=0
while(temp>0):
    if i<=6:
        p=int(days[i])
        temp-=p
        i+=1
    else:
        i=0

if i% 7==0:
    print(7)
else:
    print(i%7)