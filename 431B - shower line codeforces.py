from itertools import permutations

# a=[]
# for i in range(5):
#     a.append(list(map(int,input().split())))

# print(a)
# # for p in permutations(range(5)):
# #     print(p)

# # By kumihimo
# from itertools import *
# a=[]
# for i in range(5):
#     a.append(list(map(int,input().split())))
# print(a)

# m=0
# for p in permutations(range(5)):
#     t=0
#     for i in range(4):
#         for j in range(i,5,2):
#             if j!=4:
#                 t+=a[p[j]][p[j+1]]+a[p[j+1]][p[j]]
#     if t>=m:
#         m=t
# print(m)

# help(permutations)


num=[]
for _ in range(5):
    num.append(list(map(int,input().split())))

print(num)

temp=0
for a,b,c,d,e in permutations([0,1,2,3,4],5):
    maximum=num[a][b]+num[b][a]
    +num[c][d]+num[d][c]
    +num[c][b]+num[b][c]
    +num[d][e]+num[e][d]
    +num[c][d]+num[d][c]
    +num[d][e]+num[e][d]

    temp=max(maximum,temp)
print(temp)