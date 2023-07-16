test = int(input())

for _ in range(test):
    value = int(input())
    if value % 3 == 0:
        print(value // 3, value // 3)
    else:
        a = value // 3
        b = value % 3
        if b == 1:
            print(a + 1, a)
        else:
            print(a, a + 1)
