test = int(input())

for _ in range(test):
    n, d = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()
    for i in num:
        if i > d:
            if num[0] + num[1] <= d:
                print("YES")
                break
            else:
                print("NO")
                break
    else:
        print("YES")
