test = int(input())

for _ in range(test):
    angle = int(input())
    print("YES" if 360 % (180-angle) == 0 else "NO")