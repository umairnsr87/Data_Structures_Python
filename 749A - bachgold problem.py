def bachgold_problem():
    n = int(input())

    if n % 2 == 0:
        print(n // 2)
        for i in range(n // 2):
            print("2", sep=" ")
    else:
        print(n // 2)
        for i in range((n // 2) - 1):
            print("2", sep=" ")
        print("3")


bachgold_problem()
