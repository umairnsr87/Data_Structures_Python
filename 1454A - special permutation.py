test = int(input())
for _ in range(test):
    n = int(input())
    a = list(range(1, n + 1))[::-1]

    for i in range(1, len(a)):
        if i == a[i - 1]:
            temp = a[i - 1]
            a[i - 1] = a[i]
            a[i] = temp

    print(*a)
