for i in range(5):
    # print(i)
    s=[int(x) for x in input().split()]
    for k in range(5):
        if s[k]==1:
            print((abs(k-2))+(abs(i-2)))
            break