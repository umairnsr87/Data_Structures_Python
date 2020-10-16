x=int(input())
y=input()
y=y.split(" ")
temp=0
for i in range(len(y)):
    temp+=int(y[i])

print(temp/len(y))