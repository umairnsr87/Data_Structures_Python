from math import floor

test = int(input())

for _ in range(test):
    h, va, ls = map(int, input().split())

    while va > 0 and h > 20:
        h = (floor(h / 2)) + 10
        va -= 1
    while ls > 0:
        h -= 10
        ls -= 1

    if h <= 0:
        print("YES")
    else:
        print("NO")
