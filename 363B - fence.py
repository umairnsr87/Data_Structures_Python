n, k= map(int,input().split())

blocks = list(map(int,input().split()))
minimum=sum(blocks[0:k])
temp=1
current=minimum
for i in range(1,n-k+1):
    current = current - blocks[i-1]+blocks[i-1+k]
    if current < minimum:
        current = minimum
        temp=i+1
        # minimum=min(minimum,sum(blocks[i:i+k]))
        # temp=i

print(temp)
