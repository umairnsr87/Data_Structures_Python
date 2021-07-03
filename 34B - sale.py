n, m = map(int,input().split())

prices = list(map(int,input().split()))

prices.sort()

profit=0
for i in range(m):
    if prices[i] <= 0:
        profit+=abs(prices[i])
    else:
        break

print(profit) 