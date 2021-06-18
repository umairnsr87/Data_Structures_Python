def gifts_fixing():
    test = int(input())

    for _ in range(test):
        t = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        res = 0
        for i in range(t):
            res += max(a[i]-min(a), b[i]-min(b))

        print(res)


gifts_fixing()