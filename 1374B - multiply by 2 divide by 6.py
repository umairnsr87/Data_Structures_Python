test = int(input())

for _ in range(test):
    num = int(input())

    cnt2 = 0
    cnt3 = 0
    while num % 2 == 0:
        cnt2 += 1
        num //= 2
    while num % 3 == 0:
        cnt3 += 1
        num //= 3
    if num != 1 or cnt2 > cnt3:
        print(-1)
    else:
        print(2 * cnt3 - cnt2)

