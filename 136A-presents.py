n = int(input())
presents= {}
p = list(map(int, input().split()))
for i in range(n):
    presents[i] = p[i]
presents_inv = sorted(presents.items(), key = lambda x: (x[1], x[0]))
ans = [i[0]+1 for i in presents_inv]
print(*ans)