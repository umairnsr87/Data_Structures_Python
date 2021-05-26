def candies_and_two_sisters():
    test_case = int(input())

    for i in range(test_case):
        candies = int(input())
        if candies == 1 or candies == 2:
            print(0)
        else:
            candies -= 1
            print(candies // 2)


candies_and_two_sisters()
