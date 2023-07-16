length = int(input())

name = input()

count = 0
for i in range(len(name) - 2):
    if name[i:i + 3] == 'xxx':
        count += 1
print(count)
