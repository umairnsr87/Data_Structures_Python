dim, num = map(int, input().split())

count = 0
for i in range(1, dim + 1):
    # time complexity:O(n^2)
    # for j in range(1, dim+1):
    #     if i*j == num:
    #         count+=1
    #         break
    if (num / i == num // i) and (num / i <= dim):
        count +=1
print(count)
