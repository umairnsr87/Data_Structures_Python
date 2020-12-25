num_flowers=int(input())
s=input().split()

for temp in range(len(s)):
    s[temp]=int(s[temp])

t=max(s)
# print(t)
l=min(s)
# print(l)
if t!=l:
    print (t-l,s.count(t)*s.count(l))
else:
    print (0,num_flowers*(num_flowers-1)//2)