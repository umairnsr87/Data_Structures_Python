from collections import Counter

test = int(input())

for _ in range(test):
    num = int(input())
    numbers = list(map(int, input().split()))

    if (numbers.count(1) % 2 == 0 and numbers.count(1) > 0) or len(numbers) == 0 or (
            numbers.count(2) % 2 == 0 and numbers.count(1) % 2 == 0):
        print("YES")
    else:
        print("NO")
