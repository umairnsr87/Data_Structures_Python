test=int(input())
for _ in range(test):
    a, b, c, n = map(int, input().split())
    coins = [a, b, c]
    coins.sort()
    # print(coins)

    if n < (2 * coins[2] - coins[1] - coins[0]):
        print("NO")
    elif (n - (2 * coins[2] - coins[1] - coins[0])) % 3 == 0:
        print("YES")
    else:
        print("NO")
