gene1=input()
gene2=input()

n=min(len(gene1),len(gene2))
z=0
if sorted(gene1)==sorted(gene2):
    for t in range(n):
        if gene1[t]!=gene2[t]:
            z+=1
    if z==2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")




# temp=gene1[:2]
# if temp[::-1]==gene2[:2]:
#     print("YES")
# else:
#     print("NO")


#     s1 = input()
#     s2 = input()
#     cnt = 0
#     n = min(len(s1), len(s2))
#     for i in range(n):
#         if s1[i] != s2[i]:
#             cnt += 1
     
     
#     if cnt == 2 and set(s1) == set(s2):
#         print('YES')
#     else:
#         print('NO')