def wrong_subtraction():

    x=input().split()
    for i in range(len(x)):
        x[i]=int(x[i])


    while(x[1]>0):
        if x[0]%10 == 0:
            x[0]=x[0]//10
        elif x[0]%10 != 0:
            x[0]=x[0]-1

        x[1]=x[1]-1

    return x[0]

print(wrong_subtraction())



