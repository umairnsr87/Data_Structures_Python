test = int(input())

num = []

count = 1
while True:
    if len(num) > 1000:
        break
    elif count % 3 != 0 and count % 10 != 3:
        num.append(count)
    count += 1

for _ in range(test):
    pos = int(input())
    print(num[pos - 1])
