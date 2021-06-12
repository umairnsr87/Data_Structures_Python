n = int(input())
numbers = list(map(int, input().split()))
# todo time complexity increasing
for i in numbers:
    count = 0
    for j in range(1, (i // 2) + 1):
        if i % j == 0:
            count += 1
            if count >= 3:
                break

    if count == 2:
        print("YES")
    else:
        print("NO")
    count = 0
