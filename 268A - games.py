n = int(input())
a = []
count = 0
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    for j in range(i+1, n):
        if i != j:
            if a[i][0] == a[j][1] and a[i][1] == a[j][0]:
                count += 2
            elif a[i][0] == a[j][1] or a[i][1] == a[j][0]:
                count += 1
print(count)