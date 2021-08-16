test = int(input())

for _ in range(test):
    pairs = int(input())

    nums = list(map(int, input().split()))

    odd, even = 0, 0
    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    flag = min(odd, even)
    if flag<pairs:
        print("NO")
    else:
        print("YES")
