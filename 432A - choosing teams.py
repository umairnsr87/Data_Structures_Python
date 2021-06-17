def choosing_teams():
    n, k = map(int, input().split())

    students = list(map(int, input().split()))
    students.sort()
    team = 0
    for i in students:
        if 5 - i >= k:
            team += 1
    return team // 3


print(choosing_teams())
