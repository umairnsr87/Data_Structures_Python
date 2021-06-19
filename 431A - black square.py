x = list(map(int, input().split()))
touched_area = list(input())

cal_count = {}
for i in range(1, len(x) + 1):
    cal_count[i] = x[i - 1]

calories_burnt = 0
for value in touched_area:
    temp = cal_count.get(int(value))
    calories_burnt += temp

print(calories_burnt)
