test = int(input())

for _ in range(test):
    number = int(input())
    numbers_list = list(map(int, input().split()))
    count = numbers_list[0]
    flag=0
    temp=-1
    for value in range(1,len(numbers_list)):
        if numbers_list[value] == count:
            flag=1
        else:
            temp=value

    if flag:
        print(temp+1)
    else:
        print(1)
        # if numbers_list[0]!= numbers_list[1]:
        #     print(i +1)
        #     break
        # elif numbers_list[i]!=numbers_list[i+1]:
        #     print(i+2)
        #     break
