t = int(input())

for j in range(t):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    for i in range(k):
        if min(x) < max(y):
            temp = min(x)
            x[x.index(min(x))], y[y.index(max(y))] = y[y.index(max(y))], temp
        else:
            break
    print(sum(x))
