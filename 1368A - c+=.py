from typing import Counter


test = int(input())

for _ in range(test):
    a,b,n = map(int,input().split())
    count =0
    if a<b:
        a,b=b,a
    while a<=n :
        a,b=a+b,a
        count+=1
        
    print(count)

            
        