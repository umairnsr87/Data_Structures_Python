from math import ceil

number = int(input())
groups = list(map(int, input().split()))

a = groups.count(4)
b = groups.count(3)
c = groups.count(2)
d = groups.count(1)

p = a + b

if d <= b:
    p = p + ceil(c / 2)
else:
    p = p + ceil((d - b + 2 * c) / 4)

print(p)
