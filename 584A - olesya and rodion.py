n, t = map(int, input().split())

if len(str(t)) > n:
    print(-1)
else:
    if t == 10:
        print("1" * (n - 1) + "0")

    else:
        print(str(t) * n)
