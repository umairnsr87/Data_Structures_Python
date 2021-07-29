from math import ceil

test = int(input())

for _ in range(test):
    sticks = int(input())
    print(ceil(sticks / 2))
