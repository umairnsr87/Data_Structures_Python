flag=int(input())
x=input()
counter=0
for i in range(flag):
    if i+1<len(x):
        if x[i]==x[i+1]:
            counter+=1
print(counter)
