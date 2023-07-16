test = int(input())

count = 0
queue = list(map(int, input().split()))

d25 = 0
d50 = 0
for i in range(test):
    # if queue[i] - 25 == 0:
    #     count += 25
    # elif queue[i] - 25 != 0  :
    #     count -= (queue[i] - 25)
    #     if count < 0:
    #         break
    if queue[i] == 25:
        d25 += 1
    elif queue[i] == 50:
        if d25 > 0:
            d25 -= 1
            d50 += 1
        else:
            print("NO")
            exit()
    else:
        if d25 > 0 and d50 > 0:
            d25 -= 1
            d50 -= 1
        elif d50 == 0 and d25 >= 3:
            d25 -= 3
        else:
            print("NO")
            exit()

print("YES")
