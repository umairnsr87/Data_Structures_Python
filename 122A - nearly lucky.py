
number=int(input())

x=[4,7,47,74,447,474,477,747,774]

temp=0
for t in x:
    if number%t==0:
        temp+=1

if temp>0:
    print("YES")
else:
    print("NO")
        
