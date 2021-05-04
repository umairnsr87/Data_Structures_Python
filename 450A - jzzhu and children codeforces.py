#get the input
n,m=[int(x) for x in input().split()]

# print(n,m)

a=[(int(x)-1)//m for x in input().split()]

# print(a)
ind=max(a)
index_list=[]
for t in range(len(a)):
    if ind==a[t]:
       index_list.append(t)

# print(index_list)
if len(index_list)==1:
    print(a.index(ind)+1)
else:
    print(index_list[::-1][0]+1)
# a.reverse()
# print(a)

# print(n-a.index(max(a)))


# a,b=map(int,input().split())
# l=list(map(int,input().split()))
# r=1
# z=1
# for i in range(a):
#     c=l[i]//b
#     if l[i]%b!=0:
#     	c+=1
#     if c>=r:
#     	r=c
#     	z=i+1
# print(z)