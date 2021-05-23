def remove_smallest():
    for _ in range(int(input())):
        x = int(input())
        temp = list(map(int, input().split()))
        temp.sort()
        a = temp[0]

        for i in temp[1::]:
            if i == a or i == a + 1:
                a = i
            else:
                print("NO")
                break
        else:
            print("YES")

    # if len(temp) > 1:
    #     for i in range(1,len(temp)):
    #         if abs(temp[i-1]-temp[i])<=1:
    #             temp.pop(temp.index(temp[i]))
    #
    #         elif temp[i]-temp[i+1]>1:
    #             print("NO")
    #             break
    # elif len(temp) == 1:
    #     print("YES")


remove_smallest()
