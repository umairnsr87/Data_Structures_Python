t = int(input())
for i in range(t):
    x = int(input())
    for k in range(2, 30):
        if x % (2 ** k - 1) == 0:
            print(x // (2 ** k - 1))
            break
