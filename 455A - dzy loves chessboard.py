flag=input().split()
    
temp=[]
for i in range(int(flag[0])):
    xx=list(input())
    temp.append(xx)
 
    
    
for x in range(int(flag[0])):
    for i in range(int(flag[1])):
        if temp[x][i]=='.' and (x+i)%2==0:
            temp[x][i]='B'
            
        elif temp[x][i]=='.' and (x+i)%2!=0:
            temp[x][i]='W'
 
# print(temp)
for i in range(int(flag[0])):
    for j in range(int(flag[1])):
        print(temp[i][j],end="")
    print()