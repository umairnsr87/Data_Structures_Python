x=input().split(" ")
flag=0
temp1=int(x[0])
temp2=int(x[1])
while(temp2>=temp1):
    temp1=temp1*3
    temp2=temp2*2
    flag+=1

# print(temp1,temp2)
print(flag)