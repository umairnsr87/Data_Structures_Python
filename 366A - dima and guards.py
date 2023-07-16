n = int(input())

p, q = 1000000, 1000000
line = 0
abc = False
for i in range(4):
    a, b, c, d = map(int, input().split())
    r = min(a, b)
    s = min(c, d)
    if r < p and s < q and r + s <= n:
        p = r
        q = s
        line = i + 1
        abc = True
if abc:
    print(line, p, n - p)
else:
    print(-1)
