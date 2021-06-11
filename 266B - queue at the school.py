x, y = map(int, input().split())

queue = list(input())

for j in range(y):
    i = 0
    while i < len(queue) - 1:
        if queue[i] == "B" and queue[i + 1] == "G":
            temp = queue[i]
            queue[i] = queue[i + 1]
            queue[i + 1] = temp
            i += 2
        else:
            i+=1
print(''.join(queue))
