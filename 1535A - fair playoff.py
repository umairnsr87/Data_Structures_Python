test = int(input())

for _ in range(test):
    players = list(map(int, input().split()))
    result = []
    for i in range(0, len(players), 2):
        if players[i] > players[i + 1]:
            result.append(players[i])
        else:
            result.append(players[i + 1])
    if result[0] > min(players[len(players) // 2:]) and result[1] > min(players[:len(players) // 2]):
        print("YES")
    else:
        print("NO")
