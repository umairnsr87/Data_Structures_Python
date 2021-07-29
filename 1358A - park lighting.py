from math import ceil

test = int(input())

for i in range(test):
    r, c = map(int, input().split())

    print(ceil((r * c) / 2))
