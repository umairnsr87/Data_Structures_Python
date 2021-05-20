def new_year_and_hurry():
    n, k = map(int, input().split())
    problem_min = []
    for i in range(1, n + 1):
        problem_min.append(5 * i)

    flag = 0
    for count, i in enumerate(problem_min):
        if (i + k) <= 240:
            k += i
            flag += 1
        else:
            break

    if k < 240 and flag == n:
        return n
    else:
        return flag


print(new_year_and_hurry())
