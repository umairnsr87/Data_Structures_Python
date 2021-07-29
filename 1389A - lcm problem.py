test = int(input())


for _ in range(test):
    l, r = map(int, input().split())

    if (2 * l) <= r:
        print(l, 2 * l, sep=" ")
    else:
        print(-1, -1, sep=" ")
