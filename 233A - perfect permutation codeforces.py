x=int(input())
temp=''

if x%2==0:
    for i in range(1,x+1,2):
        temp+=str(i+1)+" "+str(i)+" "
    print( temp )
else:
    print(-1)







