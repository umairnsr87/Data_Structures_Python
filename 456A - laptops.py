test = int(input())

x="Poor Alex"
for _ in range(test):
    temp=list(map(int,input().split()))
    if temp[0]< temp[1]:
        x="Happy Alex"    

print(x)