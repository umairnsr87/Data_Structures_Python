num = int(input())

table = []

row = []
for i in range(num):
    row.append(1)
else:
    table.append(row)

for i in range(1, num):
    row = []
    for j in range(num):
        row.append(sum(table[i - 1][:j + 1]))
    table.append(row)

print(table[-1][-1])
