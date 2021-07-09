boxes = int(input())

levels = 0
while boxes > 0:
    level = list(range(1, levels + 1))

    if boxes >= sum(list(level)):
        boxes -= sum(list(level))
        levels += 1
    else:
        break

print(levels - 1)
