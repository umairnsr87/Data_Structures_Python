k, x = map(int, input().split())

for i in range(1, 9999999):
    if (k * i) % 10 == x or (k * i) % 10 == 0:
        print(i)
        break
