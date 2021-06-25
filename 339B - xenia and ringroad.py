a, b = map(int, input().split())
houses = list(map(int, input().split()))
units = 0
current_pos = 1
for val in houses:
    units += (val - current_pos) % a
    current_pos = val

print(units)