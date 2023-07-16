from collections import Counter

sticks = list(map(int, input().split()))

data = Counter(sticks)

if len(data) > 3 and data.keys():
    print("Alien")
else:
    if len(data) == 1:
        print("Elephant")
        exit()
    pos = -1
    for key, val in data.items():
        if val >= 4:
            pos = key
            break
    else:
        print("Alien")
        exit()
    if data[pos] > 4:
        temp = data[pos]
        data[pos] = temp - 1
    else:
        data.pop(pos)
    values = list(data.keys())
    if len(values) == 2 and abs(values[0] - values[1]) >= 1:
        print("Bear")
    else:
        print("Elephant")
