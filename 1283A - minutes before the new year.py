test = int(input())

for _ in range(test):
    hours, minutes = map(int,input().split())

    total_minutes_in_hours = (23-hours)*60
    total_minutes_in_hours+=60-minutes

    print(total_minutes_in_hours)