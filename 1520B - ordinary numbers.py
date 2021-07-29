test = int(input())

for _ in range(test):
    #sol:1 O(n)
    # number = int(input())
    # count = 0
    # if number <= 9:
    #     count += number
    # else:
    #     count += 9
    #     for i in range(10, number):
    #         temp = list(str(i))
    #         if temp[-1] == temp[-2]:
    #             count += 1
    # print(count)

    #sol;2 O(logn)
    n = int(input())
    count, temp = 0, n
    while n > 0:
        n //= 10
        count += 1
    t = int('1' * count)
    print(9 * (count - 1) + temp // t)
