def round_numbers():
    test=int(input())
    for i in range(test):
        num=int(input())
        list1=[]
        count=0

        while(num>0):
            list1.append(num % 10)
            num -= (num % 10)
            num = num / 10
            count+=1

        list2=[]
        for i in range(len(list1)):
            if list1[i]==0:
                continue
            else:
                list2.append(int(list1[i])*(10**i))

        print(len(list2))
        for i in list2:
            print(i, end=" ")


round_numbers()
