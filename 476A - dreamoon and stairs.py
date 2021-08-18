n, m = map(int, input().split())

if n < m:
    print(-1)
else:
    print((int((n - .5) / (2 * m)) + 1) * m)
