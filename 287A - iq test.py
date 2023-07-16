data = []
for i in range(4):
    inp = list(input())
    data.append(inp)

count = 0
if (data[1][1] + data[1][2] + data[2][1] + data[2][2]).count('#') >= 3:
    count += 1
else:
    for a in range(len(data) - 1):
        for b in range(0, 4, 2):
            if (data[a][b] + data[a][b + 1] + data[a + 1][b] + data[a + 1][b + 1]).count('#') >= 3 or (
                    data[a][b] + data[a][b + 1] + data[a + 1][b] + data[a + 1][b + 1]).count('.') >= 3:
                count += 1
                break

if count > 0:
    print("YES")
else:
    print("NO")
