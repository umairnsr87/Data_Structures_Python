test=int(input())
for _ in range(test):
    number = int(input())

    if number & (number-1):
        print("YES")
    else:
        print("NO")


