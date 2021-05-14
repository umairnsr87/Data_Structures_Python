from math import ceil
#step:1- get the input
for i in range(int(input())):
    #step:2- get the numbers
    a,b=map(int,input().split())

    if a-b==0:
        print(0)
    elif (abs(a-b)%10)==0:
        print(abs(a-b)//10)
    else:
        print(ceil(abs(a-b)/10))

