test = int(input())

for _ in range(test):
    a = int(input())
    b = list(map(int, input().split()))
    total_sum = sum(b)
    if total_sum > len(b):
        print(total_sum - len(b))
    elif total_sum < len(b):
        print(1)
    elif total_sum == len(b):
        print(0)
