y, w = map(int, input().split())

num = max(y, w)

l = [1, 2, 3, 4, 5, 6]
m = []
for i in range(len(l)):
    if l[i] >= num:
        m.append(l[i])
minimum = []
for i in l:
    if len(m) % i == 0 and 6 % i == 0:
        temp = [len(m) // i, 6 // i]
        minimum.append(temp)
x = min(minimum)
print(str(x[0]) + "/" + str(x[1]))
