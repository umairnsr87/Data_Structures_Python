test_case=int(input())

for i in range(test_case):
    num=int(input())
    number=[]
    for j in range(1,num+1):
        number.append(2**j)
    # print(number)
    if len(number)==2:
        print(abs(number[0]-number[1]))
    else:
        weight1=sum(number[:int(len(number)//2)-1],number[-1])
        weight2 = sum(number[int(len(number) // 2-1):len(number)-1])
        print(weight1-weight2)


    number=[]

