t = int(input())

for i in range(t):
    o = []
    e = []
    x = int(input())
    arr = list(map(int, input().split()))
    for p, num in enumerate(arr):
        if p % 2 == 0:
            if num % 2 != 0:
                e.append(num)
        elif p % 2 != 0:
            if num % 2 == 0:
                o.append(num)

    if len(e) == len(o):
        print(len(o))
    else:
        print(-1)
